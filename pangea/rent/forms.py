from django import forms
from .models import Rent

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('sell',)
