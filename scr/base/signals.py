from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from datetime import date 
from .templatetags.custom_badge import status_badge

@receiver(post_save, sender=Appointment)
def generate_checklist(sender, instance, created, **kwargs):
    """
    Automatically creates a Checklist object when a new Appointment is created.
    """
    if created: 
        Checklist.objects.create(appointment=instance)

@receiver(post_save, sender=Appointment)
def notify_appointment_change(sender, instance, **kwargs):
    """
    Sends real-time WebSocket updates whenever an Appointment is created or updated.
    """
    channel_layer = get_channel_layer()
    vehicle_id = instance.vehicle.id

    # Fetch all appointments for the same vehicle
    appointments = Appointment.objects.filter(vehicle=instance.vehicle)

    # Serialize appointment data to be sent through WebSocket
    appointments_data = [
        {
            "id": appointment.id,
            "service": appointment.service.name if appointment.service else "N/A",
            "plate": appointment.vehicle.plate if appointment.vehicle else "N/A",
            "date": appointment.date.strftime('%Y-%m-%d'),
            "time": appointment.get_time_display(),
            "branch": appointment.branch.name if appointment.branch else "N/A",
            "status": status_badge(appointment.status) 
        }
        for appointment in appointments
    ]

    # Enviar todas las citas al grupo WebSocket asociado con el vehículo
    async_to_sync(channel_layer.group_send)(
        f'appointments_{vehicle_id}',  # El nombre del grupo de WebSocket
        {
            'type': 'send_appointment_update',  # El tipo de mensaje que manejará el consumidor
            'appointments': appointments_data  # Lista con todas las citas
        }
    )

@receiver(post_save, sender=Work)
@receiver(post_save, sender=Checklist)
def notify_checklist_and_works(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    group_name = f'appointment_details_{instance.appointment.id}'
    
    # Obtener la cita (Appointment) relacionada con el trabajo o checklist
    appointment = instance.appointment
    
    # Verificar si el checklist ha cambiado antes de enviar los datos
    checklist = Checklist.objects.filter(appointment=appointment).first()
    checklist_data = {}
    if checklist:
        checklist_data = {
            'Gata': checklist.jack,
            'Documentos': checklist.documents,
            'Herramientas': checklist.tools,
            'Llave de rueda': checklist.wheel_key,
            'Extintor': checklist.extinguisher,
            'Botiquín': checklist.first_aid_kit,
            'Triángulos': checklist.triangles,
            'Neumático de repuesto': checklist.spare_tire,
        }

    # Obtener todos los trabajos relacionados con la cita
    works = Work.objects.filter(appointment=appointment)
    
    # Serializa los trabajos, asegurándote de convertir las fechas a cadenas ISO
    works_data = [{
        'description': work.description,
        'status': work.status,
        'priority': work.priority,
        'start_date': work.start_date.isoformat() if isinstance(work.start_date, date) else str(work.start_date),
        'end_date': work.end_date.isoformat() if isinstance(work.end_date, date) else str(work.end_date),
    } for work in works]

    # Obtener el mileage y fuel_entry de la cita
    mileage = appointment.mileage
    fuel_entry = appointment.fuel_entry

    # Enviar los datos al grupo WebSocket solo si ha habido cambios en los works o en el checklist
    if checklist_data:
        async_to_sync(channel_layer.group_send)( 
            group_name, 
            {
                'type': 'send_checklist', 
                'checklist': checklist_data,
                'should_open_modal': False  # No abrir modal al actualizar checklist
            }
        )

    if works_data:
        async_to_sync(channel_layer.group_send)( 
            group_name, 
            {
                'type': 'send_works', 
                'works': works_data,
                'should_open_modal': True  # Abrir modal al actualizar work
            }
        )

    # Enviar los datos del mileage y fuel_entry si han cambiado
    async_to_sync(channel_layer.group_send)(
        group_name, 
        {
            'type': 'send_mileage_and_fuel', 
            'mileage': mileage,
            'fuel_entry': fuel_entry
        }
    )
