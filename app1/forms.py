from django import forms
from .models import login
class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'
