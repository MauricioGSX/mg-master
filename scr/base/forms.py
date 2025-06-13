from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=True,
        help_text="Porfavor, Ingrese su Nombre.",
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=30,
        required=True,
        help_text="Porfavor, Ingrese un Apellido.",
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
        help_text="Porfavor Ingrese un Correo Valido.",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )


class AppointmentForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["vehicle"].queryset = Vehicle.objects.filter(client=user)

        self.fields["mechanic"].queryset = Mechanic.objects.filter(
            status=Mechanic.AVAILABLE
        )

    class Meta:
        model = Appointment
        fields = ["vehicle", "date", "time", "mechanic", "branch"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['description', 'appointment']



class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field_name in ['first_name', 'last_name', 'email']:
            self.fields[field_name].widget.attrs.update({
                'class': 'w-full py-2 px-3 border border-gray-300 rounded focus:outline-none focus:ring'
            })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control block w-full px-3 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            'placeholder': 'Old Password'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control block w-full px-3 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            'placeholder': 'New Password'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control block w-full px-3 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            'placeholder': 'Confirm New Password'
        })

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise forms.ValidationError('The password must be at least 8 characters long.')
        return password1
