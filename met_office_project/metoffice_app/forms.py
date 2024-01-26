# forms.py
from django import forms
from .models import Region, Parameter

class MetOfficeForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    parameter = forms.ModelChoiceField(queryset=Parameter.objects.all())
    year_or_rank = forms.IntegerField(required=False, label='Year or Rank')
