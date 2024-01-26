
from django import forms
from .models import Region, Parameter

class MetOfficeForm(forms.Form):
    ORDER_CHOICES = [
        ('ranked', 'Ranked Order Statistics'),
        ('date', 'Year Order Statistics'),
    ]

    order = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Region')
    parameter = forms.ModelChoiceField(queryset=Parameter.objects.all(), label='Parameter')
