from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import (LoginView)
from django.urls import reverse_lazy, reverse
from .decorators import group_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormView
from django.contrib.auth.models import Group
from .forms import *
from .models import Vehicle, Appointment, Work, Checklist
from django.contrib.auth import update_session_auth_hash,logout
from django.http import HttpResponseRedirect
from django.contrib import messages,admin
from django.http import JsonResponse
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .templatetags.custom_badge import status_badge,custom_badge_work
from django.http import HttpResponse
import logging

class CustomLoginView(LoginView):
    """
    Custom login view that redirects users based on their group membership.
    """
    template_name = "login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name="User").exists():
                return reverse_lazy("user_menu")
            elif user.groups.filter(name="Receptionist").exists():
                return reverse_lazy("receptionist_menu")
    
        return super().get_success_url()
    
    def form_valid(self, form):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        response = super().form_valid(form)
        
        if next_url:
            return redirect(next_url)
        
        return response

class CustomLogoutView(View):
    def get(self, request):
        logout(request) 
        return redirect("login")

class Login(LoginView):
    template_name = "login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")

class Registration(FormView):
    template_name = "registration.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True

    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        desired_group = Group.objects.get(name="User")
        user.groups.add(desired_group)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

def is_user(user):
    return user.is_authenticated and user.groups.filter(name="User").exists()

def is_receptionist(user):
    return user.is_authenticated and user.groups.filter(name="Receptionist").exists()

@login_required
@user_passes_test(is_user, login_url="login")
def user_menu(request):
 
    user = request.user
    vehicles = Vehicle.objects.filter(client=user, status=True) 
    brands = VehicleBrand.objects.filter(status=False)  
    years = VehicleYear.objects.all()
    colors = VehicleColor.objects.all()
    user_profile = CustomUser.objects.get(id=user.id) 
    mechanics = Mechanic.objects.filter(status=Mechanic.AVAILABLE)
    max_points = 500
    points_percentage = (user_profile.accumulated_points / max_points) * 100

    context = {
        "user": user,
        "vehicles": vehicles,
        "brands": brands,
        "years": years,
        "colors": colors,
        "user_profile": user_profile,
        "points_percentage": points_percentage, 
        "mechanics": mechanics,
    }
    return render(request, "./user/index.html", context)

@login_required
def get_vehicle_models(request):
    """
    AJAX view that returns vehicle models filtered by brand ID.

    Parameters (GET):
        - brand_id: ID of the selected brand.

    Returns:
        JsonResponse: List of models for the selected brand.
    """

    brand_id = request.GET.get('brand_id')
    print(f"Received brand_id: {brand_id}")
    models = VehicleModel.objects.filter(brand_id=brand_id)
    options = [{'id': model.id, 'name': model.name} for model in models]
    return JsonResponse(options, safe=False)



@csrf_exempt  
def update_mileage(request):
    """
    Updates the mileage for a specific appointment.

    Expected POST parameters:
    - appointment_id: ID of the appointment to update.
    - mileage: New mileage value.

    """
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('appointment_id')
            new_mileage = request.POST.get('mileage')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.mileage = new_mileage
            appointment.save()
            
            return JsonResponse({'status': 'success', 'message': 'Kilometraje actualizado exitosamente.'})
        except Appointment.DoesNotExist:
            # When the appointment with the given ID does not exist,
            # it's important to return a clear error to help frontend handle gracefully.
            return JsonResponse({'status': 'error', 'message': 'Cita no encontrada.'})
        
    # If method is not POST, the endpoint returns 'Method not allowed' to inform clients of correct usage.
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})

@csrf_exempt
def update_fuel(request):
    """
    Expected POST parameters:
    - appointment_id: ID of the appointment to update.
    - fuel_entry: New fuel level value.
    """
    # Same logic as update_mileage function, adapted for fuel_entry field.
    # Important: These two functions could be refactored to avoid duplication.
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('appointment_id')
            new_fuel_entry = request.POST.get('fuel_entry')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.fuel_entry = new_fuel_entry
            appointment.save()
            
            return JsonResponse({'status': 'success', 'message': 'Nivel de combustible actualizado exitosamente.'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cita no encontrada.'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})


@csrf_exempt  
def update_work(request):
    if request.method == 'POST':
        work_id = request.POST.get('work_id')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        try:
            work = Work.objects.get(id=work_id)
            # Update only the fields that were provided in the request
            # This prevents overwriting existing data with None or empty values
            if end_date:
                work.end_date = end_date
            if priority:
                work.priority = priority
            if status:
                work.status = status

            work.save()

            return JsonResponse({'success': True, 'message': 'Trabajo actualizado con éxito.'})
        except Work.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Trabajo no encontrado.'})

    return JsonResponse({'success': False, 'message': 'Solicitud inválida.'})

@csrf_exempt
def add_work_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print(request.POST) # Debug: Print POST data for development
        form = WorkForm(request.POST)
        if form.is_valid():
            # Create Work instance but don't save yet to assign additional fields
            work = form.save(commit=False)

            # Manually assign the foreign key appointment from POST data
            work.appointment_id = request.POST.get('appointment')
            work.save()
            return JsonResponse({'status': 'success', 'message': 'Servicio agregado exitosamente.'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Solicitud no válida.'}, status=400)


def get_status_badge_class(status):
    badge_classes = {
        'Pending': 'badge-warning',
        'Received': 'badge-info',
        'In progress': 'badge-primary',
        'Completed': 'badge-success',
        'Cancelled': 'badge-danger',
    }
    return badge_classes.get(status, 'badge-secondary')

@csrf_exempt 
def change_status(request, appointment_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')

            print(f'Received new status: {new_status}')  

            if new_status not in dict(Appointment.STATUS_CHOICES).keys():
                return JsonResponse({'success': False, 'error': 'Invalid status.'}, status=400)

            appointment = Appointment.objects.get(id=appointment_id)
            print(f'Current status before change: {appointment.status}')  
            appointment.status = new_status

            client_profile = appointment.vehicle.client

            if new_status == 'Completed':
                client_profile.accumulated_points += 20
                client_profile.save()
                print(f'Added 20 points to client {client_profile.username}. Total points: {client_profile.accumulated_points}') 

            elif new_status == 'Cancelled':
                if client_profile.accumulated_points >= 20:
                    client_profile.accumulated_points -= 20
                    client_profile.save()
                    print(f'Subtracted 20 points from client {client_profile.username}. Total points: {client_profile.accumulated_points}')  
                appointment.mechanic = None
                appointment.time = None
                print("Removed mechanic and time for cancelled appointment.")

            appointment.save()

            print(f'New status after change: {appointment.status}')  

            return JsonResponse({
                'success': True,
                'new_status_display': new_status,
                'new_status_class': appointment.get_status_badge_class(),
            })
        except Appointment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Appointment not found.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON.'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'CustomUser not found for the client.'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)

@login_required
def register_vehicle(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand')
        model_id = request.POST.get('model')
        plate = request.POST.get('plate')
        year_id = request.POST.get('year')
        color_id = request.POST.get('color')

        try:
            brand = VehicleBrand.objects.get(id=brand_id)
            model = VehicleModel.objects.get(id=model_id)
            year = VehicleYear.objects.get(id=year_id)
            color = VehicleColor.objects.get(id=color_id)

            # Create vehicle linked to user, set status active by default
            vehicle = Vehicle.objects.create(
                client=request.user, 
                brand=brand,
                model=model,
                plate=plate,
                year=year,
                color=color,
                status=True
            )
            return JsonResponse({'success': True, 'message': 'Vehículo registrado exitosamente.', 'reload': True})

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Ocurrió un error: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Método no permitido.'})


@login_required
def get_appointment_details(request):
    appointment_id = request.GET.get('appointment_id')

    if not appointment_id:
        return JsonResponse({'error': 'Appointment ID is required.'}, status=400)

    try:
        appointment = Appointment.objects.get(id=appointment_id)
        try:
            checklist = Checklist.objects.get(appointment=appointment)
            checklist_details = {
                'Gata': checklist.jack,  
                'Documentos': checklist.documents, 
                'Herramientas': checklist.tools,  
                'Llave de rueda': checklist.wheel_key,  
                'Extintor': checklist.extinguisher,  
                'Botiquín': checklist.first_aid_kit, 
                'Triángulos': checklist.triangles,  
                'Neumático de repuesto': checklist.spare_tire, 
            }
        except Checklist.DoesNotExist:
            checklist_details = 'No checklist available'

        work_list = []
        works = Work.objects.filter(appointment=appointment)
        for work in works:
            work_list.append({
                'description': work.description,
                'status': custom_badge_work(work.status),
                'status_text': work.status, 
            })

        appointment_details = {
            'mileage': appointment.mileage,
            'fuelLevel': appointment.fuel_entry,  
            'inventory': ['Gata', 'Documentos', 'Herramientas', 'Llave de rueda'],  
            'service': appointment.service.name if appointment.service else 'N/A',  
            'date': appointment.date,  
            'status': appointment.status,  
            'checklist': checklist_details, 
            'works': work_list, 
        }

        return JsonResponse(appointment_details)

    except Appointment.DoesNotExist:
        return JsonResponse({'error': 'Appointment not found.'}, status=404)
    

@login_required
def create_appointment(request):
    if request.method == "POST":
        try:
            data = request.POST      # Use request.POST to convert the form data into a dictionary
            vehicle_id = data.get('vehicle_id')
            date = data.get('date')
            time = data.get('time')
            mechanic_id = data.get('mechanic')
            service_id = data.get('service') 
            branch_id = data.get('branch')   

            if not (vehicle_id and date and time and mechanic_id and service_id and branch_id):
                            html = """
                            <div class="alert alert-danger">Todos los campos son obligatorios.</div>
                            <script>
                                setTimeout(() => {
                                    const modal = bootstrap.Modal.getInstance(document.getElementById('createAppointmentModal'));
                                    if (modal) modal.hide();
                                }, 3000);
                            </script>
                            """
                            return HttpResponse(html, status=400)
            
            appointment = Appointment(
                vehicle_id=vehicle_id,
                date=date,
                time=time,
                mechanic_id=mechanic_id,
                branch_id=branch_id,
                service_id=service_id
            )
            appointment.save()
            """ debo ver como pagarlo al front """
            html = """
            <div class="alert alert-success">Appointment created successfully</div>
            <script>
                setTimeout(() => {
                const modal = bootstrap.Modal.getInstance(document.getElementById('createAppointmentModal'));
                if (modal) modal.hide();

                location.reload();
                }, 2000);

                // Mostrar toast o alerta, si usas librerías como Toastr o Bootstrap Toast
            </script>
            """
            return HttpResponse(html)

        except Exception as e:
            print("Error al crear la cita:", str(e))
            html = f"""
            <div class="alert alert-danger">Ocurrió un error al crear la cita: {str(e)}</div>
            <script>
                setTimeout(() => {{
                    const modal = bootstrap.Modal.getInstance(document.getElementById('createAppointmentModal'));
                    if (modal) modal.hide();
                }}, 3000);
            </script>
            """
            return HttpResponse(html, status=500)
    else:
        html = """
            <div class="alert alert-danger">Método no permitido.</div>
            <script>
                setTimeout(() => {
                    const modal = bootstrap.Modal.getInstance(document.getElementById('createAppointmentModal'));
                    if (modal) modal.hide();
                }, 3000);
            </script>
            """
        return HttpResponse(html, status=405)

@login_required
def update_vehicle_info(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle_data = {
        'name': f"{vehicle.brand.name} {vehicle.model.name}",
        'plate': vehicle.plate,
        'logo': request.build_absolute_uri(f"/static/images/vehicle_brand/{vehicle.brand.logo}")  
    }
    return JsonResponse(vehicle_data)


@login_required
@group_required("Receptionist")
def add_mechanic(request):
    """
    Handles POST request to create a new mechanic linked to an existing branch.

    Note:
    - Only accessible to authenticated users in the "Receptionist" group.
    - Expects 'branch' as an ID referencing an existing Branch; 404 if not found.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        specialty = request.POST.get('specialty')
        experience_years = request.POST.get('experience_years')
        branch_id = request.POST.get('branch') 

        branch = get_object_or_404(Branch, id=branch_id)

        mechanic = Mechanic(
            name=name,
            email=email,
            phone=phone,
            specialty=specialty,
            experience_years=experience_years,
            branch=branch 
        )
        mechanic.save()

        return JsonResponse({'message': 'Mecánico agregado exitosamente.'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def get_branches(request):
    branches = Branch.objects.all()
    branch_list = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse(branch_list, safe=False)

@login_required
def load_services(request):
    services = Service.objects.all().values('id', 'name')
    return JsonResponse(list(services), safe=False)

@login_required
def load_branches(request):
    branches = Branch.objects.all().values('id', 'name')
    return JsonResponse(list(branches), safe=False)


@login_required
@require_http_methods(["DELETE"])
def delete_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.delete() 
        return JsonResponse({'message': 'Vehículo eliminado correctamente'}, status=200)
    except Vehicle.DoesNotExist:
        return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)
    except Exception as e:
        print(f"Error al eliminar el vehículo: {e}")
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)

@login_required
def get_models_by_brand(request, brand_id):
    models = VehicleModel.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse({'models': list(models)})

logger = logging.getLogger(__name__)

@login_required
def get_appointments(request):
    """
    Retrieves appointments for a given vehicle and sends updates via WebSocket.

    Important details:
    - Expects 'vehicle_id' as a GET parameter; returns 400 if missing.
    - Uses select_related for efficient query of related service, vehicle, and branch.
    - Formats appointment data with fallback "N/A" if related objects are missing.
    - Sends appointment list to a WebSocket group named 'appointments_{vehicle_id}'
    """
    vehicle_id = request.GET.get('vehicle_id')
    if not vehicle_id:
        return JsonResponse({"error": "vehicle_id is required"}, status=400)

    appointments = Appointment.objects.filter(vehicle_id=vehicle_id).select_related('service', 'vehicle', 'branch')

    print(f"Se encontraron {appointments.count()} citas para el vehículo {vehicle_id}")

    appointment_list = [
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

    print(f"Datos de citas generados: {appointment_list}")

    try:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(f'appointments_{vehicle_id}', {
            'type': 'send_appointment_update',
            'appointments': appointment_list  
        })

        print(f"Datos enviados al grupo WebSocket: appointments_{vehicle_id}")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(appointment_list, safe=False)


@login_required
def redeem_points(request):
    """
    Key points:
    - Expects 'points_to_redeem' in POST data; defaults to 0 if missing or invalid.
    - Calls user's redeem_points method; may raise ValueError on invalid redemption.
    - Handles CustomUser.DoesNotExist if user profile is not found.
    - Returns plain text response with success or error message.
    - Redirects to 'user_menu' if accessed via non-POST methods.
    """
    if request.method == "POST":
        points_to_redeem = int(request.POST.get('points_to_redeem', 0)) 

        try:
            user_profile = request.user
            redemption_code = user_profile.redeem_points(points_to_redeem)
            message = f"Canjeaste {points_to_redeem} puntos. Tu código de canje es: {redemption_code}"
            return HttpResponse(message) 
        except ValueError as e:
            return HttpResponse(str(e))  
        except CustomUser.DoesNotExist:
            return HttpResponse("No se encontraron puntos para el usuario.") 

    return redirect('user_menu')

@login_required
@group_required("Receptionist")
def receptionist_menu(request):
    user = request.user
    today = timezone.now().date()
    week_later = today + timedelta(days=7)
    appointments = Appointment.objects.all().order_by("date", "time")
    appointments_json = [
        {
            "id": appointment.id, 
            "date": appointment.date.strftime("%d/%m/%Y"),
            "time": appointment.time,
            "vehicle": f"{appointment.vehicle.plate} - {appointment.service.name}",  
            "status": appointment.get_status_display()  
        }
        for appointment in appointments
    ]
    
    context = {
        "user": user,
        "appointments_json": json.dumps(appointments_json), 
    }
    return render(request, "./receptionist/index.html", context)

@login_required
@group_required("Receptionist")
def appointment_details(request, appointment_id):
    """
    Display detailed information for a specific appointment.

    Key points:
    - Requires "Receptionist" group membership.
    - Includes related vehicle and client info (if available).
    - Fetches associated work items and an optional checklist.
    - Passes all data to the 'receptionist/details.html' template.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    vehicle = appointment.vehicle
    client = vehicle.client if vehicle else None  
    works = Work.objects.filter(appointment=appointment)
    checklist = getattr(appointment, 'checklist', None)

    context = {
        'appointment': appointment,
        'client': client,
        'vehicle': vehicle,
        'works': works,
        'checklist': checklist,
    }

    return render(request, 'receptionist/details.html', context)

@login_required
@group_required("Receptionist")
@csrf_exempt  
def update_checklist(request, appointment_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        field = data.get('field')
        checklist = get_object_or_404(Checklist, appointment_id=appointment_id)
        if field in ['jack', 'documents', 'tools', 'wheel_key', 'extinguisher', 'first_aid_kit', 'triangles', 'spare_tire']:
            current_value = getattr(checklist, field)
            setattr(checklist, field, not current_value) 
            checklist.save()

            return JsonResponse({'status': not current_value}) 

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
@group_required("Receptionist")
def list_mechanics(request):
    """
    - Supports filtering by 'status' and 'branch' via GET parameters:
      - 'filterStatus' filters mechanics by their status.
      - 'filterBranch' filters mechanics by branch ID.
    - Uses Django Paginator to display 10 mechanics per page.
    - Validates 'page' GET parameter; defaults to page 1 if invalid or out of range.
    - Passes filtered and paginated mechanics, all branches, and current filters to the template.
    - Logs filtered queryset for debugging.
    """
    filter_status = request.GET.get('filterStatus', '')
    filter_branch = request.GET.get('filterBranch', '')
    mechanics = Mechanic.objects.all()

    if filter_status:
        mechanics = mechanics.filter(status=filter_status)

    if filter_branch:
        mechanics = mechanics.filter(branch__id=filter_branch)

    print("Mecánicos filtrados:", mechanics) 

    paginator = Paginator(mechanics, 10)  
    page_number = request.GET.get('page', 1)
    try:
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1
    except ValueError:
        page_number = 1  

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    branches = Branch.objects.all()

    context = {
        'mechanics': page_obj,  
        'page_obj': page_obj,   
        'branches': branches,
        'filter_status': filter_status,
        'filter_branch': filter_branch,
    }

    return render(request, './mechanic/index.html', context)


@login_required
@group_required("Receptionist")
def get_mechanic_details(request):
    """
    - Expects 'id' parameter in query string to identify the mechanic.
    - Returns mechanic details including human-readable specialty and status.
    - If mechanic has no assigned branch, returns 'No asignada' for branch.
    """
    if request.method == 'GET':
        mechanic_id = request.GET.get('id')
        mechanic = get_object_or_404(Mechanic, id=mechanic_id)
        mechanic_data = {
            'id': mechanic.id,
            'name': mechanic.name,
            'email': mechanic.email,
            'phone': mechanic.phone,
            'specialty': mechanic.get_specialty_display(),
            'experience_years': mechanic.experience_years,
            'status': mechanic.get_status_display(),
            'branch': mechanic.branch.name if mechanic.branch else 'No asignada', 
        }
        return JsonResponse(mechanic_data)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
    
@login_required
@group_required("Receptionist")
def update_mechanic(request):
    """
    - Expects 'mechanicId' and updated fields in POST data.
    - Updates name, email, phone, specialty, experience years, and status.
    - Returns success status if updated, 404 if mechanic not found.
    - Does not handle methods other than POST.
    """
    if request.method == 'POST':
        mechanic_id = request.POST.get('mechanicId')
        try:
            mechanic = Mechanic.objects.get(id=mechanic_id)
            mechanic.name = request.POST.get('name')
            mechanic.email = request.POST.get('email')
            mechanic.phone = request.POST.get('phone')
            mechanic.specialty = request.POST.get('specialty')
            mechanic.experience_years = request.POST.get('experience_years')
            mechanic.status = request.POST.get('status')
            mechanic.save()
            return JsonResponse({'status': 'success'})
        except Mechanic.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Mecánico no encontrado'}, status=404)


@login_required
@group_required("Receptionist")
def delete_mechanic(request):
    if request.method == 'POST':
        mechanic_id = request.POST.get('id')
        Mechanic.objects.filter(id=mechanic_id).delete()
        return JsonResponse({'status': 'success'})

@login_required
def account_settings(request):
    return render(request, 'accounts/account_settings.html')

@login_required
def update_user(request):
    """
    Handles updating the logged-in user's profile via a POST form.

    - Uses UserUpdateForm bound to the current user instance.
    - Validates and saves user data on POST.
    - Supports updating profile picture if included in request.FILES.
    - Shows success or error messages using Django's messages framework.
    """
    user = request.user  

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()

            # Process the image file if it was sent 
            if 'foto_perfil' in request.FILES:
                user.foto_perfil = request.FILES['foto_perfil']
                user.save()

            messages.success(request, '¡Tus datos se han actualizado correctamente!')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Ocurrió un error. Por favor corrige los errores en el formulario.')

    else:
        user_form = UserUpdateForm(instance=user)

    return render(request, 'accounts/user_form.html', {
        'user_form': user_form,
        'messages': messages.get_messages(request),
        'perfil_usuario': user, 
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully!')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/password_form.html', {'password_form': form})


@login_required
def profile_view(request):
    if request.user.groups.filter(name='Receptionist').exists():
        template_name = 'accounts/receptionist _settings.html'
        back_link = reverse('receptionist_menu') 
    elif request.user.groups.filter(name='User').exists():
        template_name = 'accounts/user_settings.html'
        back_link = reverse('user_menu')  
    else:
        template_name = 'design/default_profile.html'
        back_link = reverse('home') 

    return render(request, template_name, {'back_link': back_link})

@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        user_profile = CustomUser.objects.get(user=request.user)
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            user_profile.profile_picture = profile_picture
            user_profile.save()
            return JsonResponse({'message': 'Profile picture updated successfully.'})
        else:
            return JsonResponse({'error': 'No profile picture was received.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
