from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name',
            'description',
            'url',
            'taiga_key',
            'associated_users',
            'permissions',
            ]