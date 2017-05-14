from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.template import loader
from django.http import HttpResponse  
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from vallalatok import models
from .models import Telepules, TermeloVallalat

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'vallalatok/index.html'
    #context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return TermeloVallalat.objects.order_by('-pub_date')[:5]


class AdatFelView(generic.ListView):
    #model = TermeloVallalat
    template_name = 'vallalatok/adatfel.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return TermeloVallalat.objects.order_by('-pub_date')[:5]


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
      context={
          'telep':telep
      }
      return render(request, 'vallalatok/nyilva.html', context)

def adatfel(request):
    return render( request, 'adatfel.html')

#def nyilvantart(request):
  #  return render(request, 'nyilva.html')






