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
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class CustomLoginView(LoginView):
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
    vehicles = Vehicle.objects.filter(client=user, status=False) 
    brands = VehicleBrand.objects.filter(status=False)  
    years = VehicleYear.objects.all()
    colors = VehicleColor.objects.all()
    user_profile = UserProfile.objects.get(user=user)
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
    }
    return render(request, "./user/index.html", context)

@csrf_exempt  
def update_mileage(request):
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('appointment_id')
            new_mileage = request.POST.get('mileage')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.mileage = new_mileage
            appointment.save()
            
            return JsonResponse({'status': 'success', 'message': 'Kilometraje actualizado exitosamente.'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cita no encontrada.'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})

@csrf_exempt
def update_fuel(request):
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
@login_required
def get_vehicle_models(request):
    brand_id = request.GET.get('brand_id')
    models = VehicleModel.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse(list(models), safe=False)


@csrf_exempt  
def update_work(request):
    if request.method == 'POST':
        work_id = request.POST.get('work_id')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        try:
            work = Work.objects.get(id=work_id)

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
        print(request.POST) 
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
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

            client_profile = appointment.vehicle.client.userprofile

            if new_status == 'Completed':
                client_profile.accumulated_points += 20
                client_profile.save()
                print(f'Added 20 points to client {client_profile.user.username}. Total points: {client_profile.accumulated_points}') 

            elif new_status == 'Cancelled':
                if client_profile.accumulated_points >= 20:
                    client_profile.accumulated_points -= 20
                    client_profile.save()
                    print(f'Subtracted 20 points from client {client_profile.user.username}. Total points: {client_profile.accumulated_points}')  
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
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'UserProfile not found for the client.'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)




@login_required
@csrf_exempt  
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

            vehicle = Vehicle.objects.create(
                client=request.user, 
                brand=brand,
                model=model,
                plate=plate,
                year=year,
                color=color,
                status=False
            )

            return JsonResponse({'success': True, 'message': 'Vehículo registrado exitosamente.'})

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
                'status': work.status,
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
            print("Request body:", request.body) 

            data = json.loads(request.body) 
            print("Parsed JSON:", data)  

            vehicle_id = data.get('vehicle_id')
            date = data.get('date')
            time = data.get('time')
            mechanic_id = data.get('mechanic')
            service_id = data.get('service') 
            branch_id = data.get('branch')   

            print("Vehicle ID:", vehicle_id)
            print("Date:", date)
            print("Time:", time)
            print("Mechanic ID:", mechanic_id)
            print("Service ID:", service_id)  
            print("Branch ID:", branch_id)

            if not (vehicle_id and date and time and mechanic_id):
                return JsonResponse({'success': False, 'message': 'Missing required fields'}, status=400)
            
            appointment = Appointment(
                vehicle_id=vehicle_id,
                date=date,
                time=time,
                mechanic_id=mechanic_id,
                branch_id=branch_id,
                service_id=service_id
            )
            appointment.save()

            return JsonResponse({'success': True, 'message': 'Appointment created successfully'})

        except json.JSONDecodeError:
            print("Failed to parse JSON")
            return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print("Error while creating appointment:", str(e))
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)



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
def load_mechanics_json(request):
    mechanics = Mechanic.objects.filter(status=Mechanic.AVAILABLE)
    data = {
        'mechanics': [{'id': mechanic.id, 'name': mechanic.name} for mechanic in mechanics]
    }
        
    return JsonResponse(data)

@login_required
@group_required("Receptionist")
def add_mechanic(request):
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
@require_http_methods(["PATCH"])
def delete_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        data = json.loads(request.body)
        vehicle.status = data.get('status', True) 
        vehicle.save()
        return JsonResponse({'message': 'Estado del vehículo actualizado correctamente'}, status=200)
    except Vehicle.DoesNotExist:
        return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)
    except Exception as e:
        print(f"Error al eliminar el vehículo: {e}") 
        return JsonResponse({'error': 'Error interno del servidor'}, status=500)


@login_required
def get_models_by_brand(request, brand_id):
    models = VehicleModel.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse({'models': list(models)})

import logging

logger = logging.getLogger(__name__)

@login_required
def get_appointments(request):
    vehicle_id = request.GET.get('vehicle_id')
    appointments = Appointment.objects.filter(vehicle_id=vehicle_id)

    # Construye la lista de citas
    appointment_list = [
        {
            "id": appointment.id,
            "service": appointment.service.name if appointment.service else "N/A",
            "plate": appointment.vehicle.plate if appointment.vehicle else "N/A",
            "date": appointment.date.strftime('%Y-%m-%d'),
            "time": appointment.get_time_display(),
            "branch": appointment.branch.name if appointment.branch else "N/A",
            "status": appointment.status
        }
        for appointment in appointments
    ]

    logger.debug("Appointment List: %s", json.dumps(appointment_list, indent=4))

    return JsonResponse(appointment_list, safe=False)

@login_required
def redeem_points(request):
    if request.method == "POST":
        points_to_redeem = int(request.POST.get('points_to_redeem', 0)) 

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            redemption_code = user_profile.redeem_points(points_to_redeem)
            messages.success(request, f"Canjeaste {points_to_redeem} puntos. Tu código de canje es: {redemption_code}")
        except ValueError as e:
            messages.error(request, str(e))
        except UserProfile.DoesNotExist:
            messages.error(request, "No se encontraron puntos para el usuario.")
        
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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.username = request.user.username

            if 'foto_perfil' in request.FILES: 
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.foto_perfil = request.FILES['foto_perfil']  
                user_profile.save()
            
            user.save()
            messages.success(request, 'Your data has been updated successfully!')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'An error occurred. Please correct the errors in the form.')
    else:
        user_form = UserUpdateForm(instance=request.user)

    user_profile = UserProfile.objects.get(user=request.user) 
    return render(request, 'accounts/user_form.html', {
        'user_form': user_form,
        'messages': messages.get_messages(request),
        'perfil_usuario': user_profile 
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
        user_profile = UserProfile.objects.get(user=request.user)
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            user_profile.profile_picture = profile_picture
            user_profile.save()
            return JsonResponse({'message': 'Profile picture updated successfully.'})
        else:
            return JsonResponse({'error': 'No profile picture was received.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
