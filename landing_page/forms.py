from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UserCreateForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password_repeat',
            'first_name',
            'last_name',
            'email',
        )

        labels = {
            'username': 'Nazwa użytkownika',
            'password': 'Hasło',
            'password_repeat': 'Powtórz hasło',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Adres e-mail',
        }

        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
            raise ValidationError('Passwords need to match')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Imię i nazwisko")
    email = forms.EmailField(label="Adres e-mail")
    message = forms.CharField(widget=forms.Textarea, label="Wiadomość")


class CustomAuthForm(AuthenticationForm):
    username = UsernameField(
        label="Użytkownik",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Hasło",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
