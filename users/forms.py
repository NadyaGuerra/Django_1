from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail

from config import settings
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save()
        send_mail(subject='Активация профиля',
                  message=f'Для активации пройдите по ссылке - http://127.0.0.1:8000/users/activate/{user.id}/',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user.email])
        user.is_active = False
        user.save()
        return user

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone', 'email', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'