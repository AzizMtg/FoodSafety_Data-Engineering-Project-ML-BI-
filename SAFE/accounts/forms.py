from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('inspector', 'Inspector'),
        ('owner', 'Owner'),
        ('client', 'Client'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if not username:
            self.add_error('username', 'Username is required.')
        if not password1 or not password2:
            self.add_error('password1', 'Both password fields are required.')
        if password1 != password2:
            self.add_error('password2', 'Passwords do not match.')
        
        return cleaned_data
