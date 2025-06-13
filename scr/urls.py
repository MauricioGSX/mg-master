from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from base.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from scr.base.consumers import *

"""
    URL Configuration for the Django project.

    - Admin interface URLs.
    - Authentication routes: login, logout, and registration.
    - User-specific views for dashboard and profile management.
    - Receptionist-specific views for appointment handling, vehicle management,
    and points redemption.
    - Vehicle and appointment management URLs, including status changes,
    checklist updates, and vehicle registration.
    - Mechanic and branch management routes to list, add, update, and delete mechanics,
    as well as branch data retrieval.
    - Service and work management endpoints for loading services and managing work items.
    - User account settings including profile updates and password changes.

    Additionally, media files are served during development by appending the static URL pattern.
    Note: The static media serving configuration should be removed in production
    and handled by the web server.
    
"""
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path("", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", Registration.as_view(), name="register"),

    # User-specific views
    path("user/dashboard/", user_menu, name="user_menu"),
    path("profile/", profile_view, name="profile"),
    path('update_vehicle_info/<int:vehicle_id>/', update_vehicle_info, name='update_vehicle_info'),

    # Receptionist-specific views
    path("receptionist/dashboard/", receptionist_menu, name="receptionist_menu"),
    path("receptionist/details/<int:appointment_id>/", appointment_details, name="appointment_details"),
    path('create-appointment/', create_appointment, name='create_appointment'),
    path('delete-vehicle/<int:vehicle_id>/', delete_vehicle, name='delete_vehicle'),
    path('get_appointment_details/', get_appointment_details, name='get_appointment_details'),
    path('redeem-points/', redeem_points, name='redeem_points'),
    path('get_appointments/', get_appointments, name='get_appointments'),

    
    # Vehicle and appointment management views
    path('appointments/<int:appointment_id>/change_status/', change_status, name='change_status'),
    path('appointment/<int:appointment_id>/update_checklist/', update_checklist, name='update_checklist'),
    path('update_mileage/', update_mileage, name='update_mileage'),
    path('update_fuel/', update_fuel, name='update_fuel'),
    path('get-vehicle-models/', get_vehicle_models, name='get_vehicle_models'),
    path('register-vehicle/', register_vehicle, name='register_vehicle'),
    path('get-models-by-brand/<int:brand_id>/', get_models_by_brand, name='get_models_by_brand'),

    # Mechanic and branch management views
    path('mechanics/', list_mechanics, name='list_mechanics'),
    path('update-mechanic/', update_mechanic, name='update_mechanic'),
    path('add-mechanic/', add_mechanic, name='add_mechanic'),
    path('delete-mechanic/', delete_mechanic, name='delete_mechanic'),
    path('get-mechanic-details/', get_mechanic_details, name='get_mechanic_details'),
    path('load_branches/', load_branches, name='load_branches'),
    path('get-branches/', get_branches, name='get_branches'),

    # Service and work management views
    path('load_services/', load_services, name='load_services'),
    path('update-work/', update_work, name='update_work'),
    path('add-work-ajax/', add_work_ajax, name='add_work_ajax'),

    # User settings views
    path('settings/', account_settings, name='account_settings'),
    path('settings/update-user/', update_user, name='update_user'),
    path('settings/change-password/', change_password, name='change_password'),
    path('update_profile_picture/', update_profile_picture, name='update_profile_picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in development (configure this via web server in production)

