from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.template import loader
from django.http import HttpResponse  
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from vallalatok import models,forms
from .models import Telepules, TermeloVallalat,Telephely,Tevekenyseg
from django.core.exceptions import ValidationError

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'vallalatok/index.html'
    def get_queryset(self):
        return TermeloVallalat.objects.order_by('-pub_date')[:5]

#class AdatFelView(generic.ListView):
 #   template_name = 'vallalatok/adatfel.html'
  #  def get_queryset(self):
   #     return TermeloVallalat.objects.order_by('-pub_date')[:5]

#class NyilvView(generic.ListView):
   # model = TermeloVallalat
    #template_name = 'vallalatok/nyilva.html'
    #def get_queryset(self):
    #    """Return the last five published questions."""
     #   return TermeloVallalat.objects.order_by('-pub_date')[:5]

def index(request):
    return render( request, 'index.html')

def nyilvantart(request):
    telep = models.Telepules.objects.all()
    termv = models.TermeloVallalat.objects.all()
    vez=models.Vezeto.objects.all()
    telhely=models.Telephely.objects.all()
    context={
    'telep':telep,
    'termv':termv,
    'vez':vez,
    'telhely':telhely,
      }
    return render(request, 'vallalatok/nyilva.html', context)

def adatfel(request):
    form_data=forms.VezetoReg(request.POST or None)
    form_data2=forms.TelepulesReg(request.POST or None)
    form_data3 = forms.TermeloVallalatReg(request.POST or None)
    form_data4 = forms.TelephelyReg(request.POST or None)
  
    msg=''
    if form_data.is_valid():
        felelos = models.Vezeto()
        felelos.nev = form_data.cleaned_data['nev']
        felelos.beosztas = form_data.cleaned_data['beosztas']
        felelos.save()

    if form_data2.is_valid():
        telep = models.Telepules()
        telep.nev = form_data2.cleaned_data['nev']

        #telep.megye = form_data2.cleaned_data['megye']
        #telep.FEJER = form_data.cleaned_data['nev']
        #telep.min_iranyitoszam = form_data.cleaned_data['nev']
        #telep.max_iranyitoszam = form_data.cleaned_data['nev']
        telep.save()

    if form_data3.is_valid():
        termval = models.TermeloVallalat()
        termval.KUJ = form_data3.cleaned_data['KUJ']
        termval.KSH = form_data3.cleaned_data['KSH']
        termval.nev = form_data3.cleaned_data['nev']
        termval.iranyitoszam = form_data3.cleaned_data['iranyitoszam']
        #termval.telepules = form_data3.cleaned_data['telepules']

       # termval.telepules=form_data3.cleaned_data['telepules']
        termval.telepules=Telepules.nev
        termval.kozterulet_nev = form_data3.cleaned_data['kozterulet_nev']
        termval.kozterulet_tipus = form_data3.cleaned_data['kozterulet_tipus']
        termval.hazszam = form_data3.cleaned_data['hazszam']
        termval.save()

    if form_data4.is_valid():
        teleph = models.Telephely()
        teleph.KTJ = form_data4.cleaned_data['KTJ']
        teleph.nev = form_data4.cleaned_data['nev']
        teleph.iranyitoszam = form_data4.cleaned_data['iranyitoszam']
        #teleph.telepules = form_data4.cleaned_data['telepules']
        teleph.telepules=Telepules.nev
        teleph.telepules=form_data4.cleaned_data['telepules']
        teleph.kozterulet_nev = form_data4.cleaned_data['kozterulet_nev']
        teleph.kozterulet_tipus = form_data4.cleaned_data['kozterulet_tipus']
        teleph.hazszam = form_data4.cleaned_data['hazszam']
        teleph.foglalkoztatottak_szama = form_data4.cleaned_data['foglalkoztatottak_szama']
        teleph.felelos_nev = form_data4.cleaned_data['felelos_nev']
        teleph.felelos_beosztas = form_data4.cleaned_data['felelos_beosztas']
        teleph.save()
        msg='Elmentettük az adatokat!'
    context={
        'formregister':form_data,
        'formregister2':form_data2,
        'formregister3':form_data3,
        'formregister4':form_data4,
        'msg':msg
    }
    return render( request, 'vallalatok/adatfel.html', context)






