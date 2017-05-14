from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Telepules
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('vallalatok/index.html')
    return HttpResponse(template.render(request))