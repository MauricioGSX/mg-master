from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):  # heredar de UserAdmin
    list_display = ('username', 'email', 'phone_number', 'address', 'birth_date', 'accumulated_points')

    fieldsets = UserAdmin.fieldsets + (
        ("Información adicional", {
            "fields": ("phone_number", "address", "birth_date", "accumulated_points"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Información adicional", {
            "fields": ("phone_number", "address", "birth_date", "accumulated_points"),
        }),
    )

# Register VehicleBrand model
@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'logo')
    search_fields = ('name',)
    list_filter = ('status',)

# Register Vehicle model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('client', 'brand', 'model', 'plate', 'year', 'color', 'status')
    search_fields = ('client__username', 'plate', 'vin')
    list_filter = ('brand', 'status', 'year')
    list_select_related = True  # Optimizes queries when using related fields

# Register Mechanic model
@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'specialty', 'branch', 'experience_years')
    search_fields = ('name', 'email')
    list_filter = ('status', 'specialty', 'branch')
    ordering = ('name',)

# Register Appointment model with custom actions
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    Admin interface for managing appointments.
    Includes custom actions to update appointment statuses.
    """
    list_display = ('vehicle', 'date', 'time', 'mechanic', 'branch', 'status')
    search_fields = ('vehicle__plate', 'mechanic__name')
    list_filter = ('date', 'status', 'branch')
    actions = ['mark_as_available', 'mark_as_completed']

    def mark_as_available(self, request, queryset):
        """
        Custom admin action to mark selected appointments as available.
        """
        updated = queryset.update(status=True)
        self.message_user(request, f"{updated} appointments have been marked as available.")
    mark_as_available.short_description = "Mark selected appointments as available" 

# Register Work model
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'status', 'priority', 'start_date', 'end_date')
    search_fields = ('appointment__vehicle__plate',)
    list_filter = ('status', 'priority', 'start_date')

# Register Points model
@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('client', 'points', 'redemption_code')
    search_fields = ('client__username', 'redemption_code')

# Register Checklist model
@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'jack', 'documents', 'tools', 'extinguisher', 'triangles', 'spare_tire')
    search_fields = ('appointment__vehicle__plate',)

# Register Service model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register VehicleModel model
@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'status')
    search_fields = ('name', 'brand__name')
    list_filter = ('status', 'brand')

# Register Branch model
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
