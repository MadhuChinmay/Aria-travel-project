from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicepackage

# Create your views here.

def index(request):

    services = Servicepackage.objects.all()

    return render(request, 'index.html', {'services': services})

