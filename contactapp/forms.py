from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['first_name', 'last_name', 'email','phone_number','address']

    address = forms.CharField(widget=forms.TextInput)
