from django import forms
from vallalatok.models import Telepules

class VezetoReg(forms.Form):
    nev = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    beosztas = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))

class TelepulesReg(forms.Form):
    nev = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    megyek = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    FEJER =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    megye = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    min_iranyitoszam = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    max_iranyitoszam = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))