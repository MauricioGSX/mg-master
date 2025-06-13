from django.db import models
from django.contrib.auth.models import User,AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
import random
import string
from datetime import datetime,timedelta
from django.conf import settings

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    accumulated_points = models.PositiveIntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def redeem_points(self, amount):
        if self.accumulated_points >= amount:
            self.accumulated_points -= amount
            self.save()

            points_record = Points.objects.create(client=self, points=amount, redemption_code=self.generate_redemption_code())
            return points_record.redemption_code
        else:
            raise ValueError("No tienes suficientes puntos para canjear.")

    def generate_redemption_code(self):
        import random
        import string
        return ''.join(random.choices(string.hexdigits.lower(), k=8))


class VehicleBrand(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    logo = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class VehicleYear(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)

class VehicleColor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    year = models.ForeignKey(VehicleYear, on_delete=models.CASCADE, null=True)  
    color = models.ForeignKey(VehicleColor, on_delete=models.CASCADE , null=True)  
    status = models.BooleanField(default=True)
    vin = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.brand.name} {self.model.name} - {self.plate}"

class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mechanic(models.Model):
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not available"
    DELETED = "Deleted"

    STATUS_CHOICES = [
        (AVAILABLE, "Available"),
        (NOT_AVAILABLE, "Not available"),
        (DELETED, "Deleted"),
    ]

    SPECIALTY_CHOICES = [
        ("Electricista", "Electricista"),
        ("Mecánico", "Mecánico"),
        ("Mecatrónico", "Mecatrónico"),
        ("Lubricador", "Lubricador"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, blank=True, null=True) 
    hire_date = models.DateField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)  

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='mechanics' , null=True) 

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Mechanic"
        verbose_name_plural = "Mechanics"
        ordering = ['name']

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the choices for time periods: AM and PM
TIME_PERIOD_CHOICE = (
    ("AM", "AM"),  # Morning period
    ("PM", "PM"),  # Afternoon/evening period
)


class Appointment(models.Model):
    # Define the possible statuses for an appointment
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Received', 'Received'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)  
    time = models.CharField(max_length=2, choices=TIME_PERIOD_CHOICE, default="AM", null=True, blank=True)  
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, null=True, blank=True)  
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)  
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")  
    fuel_entry = models.PositiveIntegerField(default=0, null=True, blank=True) 
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True) 

    # Method to return the appropriate badge class based on appointment status
    def get_status_badge_class(self):
        if self.status == "Pending":
            return "badge-warning"
        elif self.status == "Received":
            return "badge-info"
        elif self.status == "In progress":
            return "badge-primary"
        elif self.status == "Completed":
            return "badge-success"
        elif self.status == "Cancelled":
            return "badge-danger"
        else:
            return "badge-secondary"

    # This method verifies that the fuel entry is between 0 and 100, and checks that the mechanic does not have another appointment at the same date and time.
    def clean(self):
        if self.fuel_entry is not None and not (0 <= self.fuel_entry <= 100):
            raise ValidationError("Fuel entry must be between 0 and 100.")
        
        if self.mechanic and self.date and self.time:
            existing_appointment = (
                Appointment.objects.filter(
                    mechanic=self.mechanic, date=self.date, time=self.time
                )
                .exclude(pk=self.pk)
                .first()
            )
            if existing_appointment:
                raise ValidationError("This mechanic already has an appointment at this time.")

    def __str__(self):
        return f"Appointment for vehicle {self.vehicle} on {self.date} at {self.get_time_display()}"


class Work(models.Model):
    STATUS_JOB_CHOICES = (
        ("En progreso", "En progreso"),
        ("Esperando Repuestos", "Esperando Repuestos"),
        ("Completado", "Completado"),
    )

    PRIORITY_CHOICES = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
)

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField(default=datetime.now) 
    end_date = models.DateField(null=True, blank=True) 
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="Medium")
    status = models.CharField(max_length=50, choices=STATUS_JOB_CHOICES, default="En progreso")


    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = timezone.now().date() + timedelta(days=5)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.appointment} - {self.status}"


class Points(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    points = models.PositiveIntegerField(default=0)  
    redemption_code = models.CharField(max_length=8, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.client} - Points: {self.points}"
    
# This method generates a random 8-character redemption code, consisting of valid hexadecimal characters, to validate that the redemption is valid.
    def generate_redemption_code(self):
        return ''.join(random.choices(string.hexdigits.lower(), k=8))


class Checklist(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="checklist")
    jack = models.BooleanField(default=False) 
    documents = models.BooleanField(default=False)  
    tools = models.BooleanField(default=False)  
    wheel_key = models.BooleanField(default=False) 
    extinguisher = models.BooleanField(default=False)  
    first_aid_kit = models.BooleanField(default=False)  
    triangles = models.BooleanField(default=False)  
    spare_tire = models.BooleanField(default=False)  

    def __str__(self):
        return f"Checklist (inventory) for appointment {self.appointment.id}"


# This class is not available at the moment because I will use it in a future task.

class VehiclePhoto(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicle_photos/') 

    def __str__(self):
        return f"Photo for appointment {self.appointment.id}"
    
class DamagePosition(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='damage_positions', on_delete=models.CASCADE)
    position_x = models.FloatField()
    position_y = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Damage position for appointment {self.appointment.id} at ({self.position_x}, {self.position_y})"
