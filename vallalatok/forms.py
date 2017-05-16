from django import forms
from django.forms import ModelForm
from vallalatok.models import Telepules,Vezeto,TermeloVallalat,Telephely



class VezetoReg(forms.Form):
    nev = forms.CharField(label="Felelős neve:", required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    beosztas = forms.CharField(label="Felelős beosztása:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))

class TelepulesReg(forms.Form):
    nev = forms.CharField(label="Település neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    # megyek = forms.CharField(label="Megye:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
   # FEJER =forms.CharField(label="Vezető neve",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    #megye = forms.IntegerField(label="Megye:", required=False, widget=forms.Select(choices=(enumerate(megyek))) ))
    #min_iranyitoszam = forms.IntegerField(label="Irányítószám",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    #max_iranyitoszam = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))

class TermeloVallalatReg(forms.Form):
    KUJ = forms.CharField(label="KUJ szám:",required=True, max_length=9, help_text='Maximum 9 karakter!', widget=forms.TextInput(attrs={'class': 'form-control'} ))
    KSH = forms.CharField(label="KSH szám:",required=True, max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    nev = forms.CharField(label="Termelőválallat neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    iranyitoszam = forms.IntegerField(label="Irányítószám:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    telepules = forms.CharField(label="Település:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    kozterulet_nev = forms.CharField(label="Közterület neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    kozterulet_tipus = forms.CharField(label="Közterület típusa:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    hazszam = forms.IntegerField(label="Házszám:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))

class TelephelyReg(forms.Form):
    KTJ = forms.CharField(label="KTJ szám:",required=True, max_length=9, help_text='Maximum 9 karakter!', widget=forms.TextInput(attrs={'class': 'form-control'} ))
    nev = forms.CharField(label="Telephely neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    tipus = forms.CharField(label="Telephely típusa:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    iranyitoszam = forms.IntegerField(label="Irányítószám:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    telepules = forms.CharField(label="Település:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    kozterulet_nev = forms.CharField(label="Közterület neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    kozterulet_tipus = forms.CharField(label="Közterület típusa:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    hazszam = forms.IntegerField(label="Házszám:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    foglalkoztatottak_szama = forms.IntegerField(label="Foglalkoztatottak száma:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    felelos_nev = forms.CharField(label="Felelős neve:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    felelos_beosztas = forms.CharField(label="Felelős beosztása:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))

