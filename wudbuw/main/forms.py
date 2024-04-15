from .models import User
from django.forms import ModelForm, TextInput



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['mail', 'password']
        widgets = {
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'mail'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'password'
            })
        }
