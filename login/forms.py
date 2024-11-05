from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_password

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'id': 'password1', 'onkeyup': 'checkPasswordStrength()'}),
        validators=[validate_password],
        help_text="Sua senha deve ter pelo menos 8 caracteres, incluir números e letras.",
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')