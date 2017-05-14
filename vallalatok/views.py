from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.template import loader
from django.http import HttpResponse  
from django.urls import reverse
from django.views import generic
from django.shortcuts import render

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


class NyilvView(generic.ListView):
   # model = TermeloVallalat
    template_name = 'vallalatok/nyilva.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return TermeloVallalat.objects.order_by('-pub_date')[:5]



def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_telep=Telepules.objects.all().count()
    num_term=TermeloVallalat.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render( request, 'index.html',context={'num_telep':num_telep,'num_term':num_term},
    )


def adatfel(request):
   # question = get_object_or_404(TermeloVallalat, pk=KUJ)
    num_telep=Telepules.objects.all().count()
    num_term=TermeloVallalat.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render( request, 'adatfel.html',context={'num_telep':num_telep,'num_term':num_term},
    )

def nyilvantart(request):
    return render(request, 'nyilva.html')




