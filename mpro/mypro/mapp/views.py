from django.shortcuts import render
from django.http import HttpResponse
from .models import patient, clinic, k, t
import random


# Create your views here.

def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html' )

def cregister(request):
    #cid=clinic.objects.all
    #cid=clinic()
    #cid.id=random.randrange(1000000000,9999999999)
    #cid = 
    #cname =
    #cemail=
    return render(request, 'cregister.html' )

def pform(request):
    id=random.randrange(1000000000,9999999999)
    if request.method=="POST":
        img=request.POST.get('img')
        gender=request.POST.get('gender')
        type=request.POST.get('type')
        kind=request.POST.get('kind')
        stage=request.POST.get('stage')
        cid = request.POST.get('cid')
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        age =request.POST.get('age') 
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address_a = request.POST.get('address_a')
        address_b = request.POST.get('address_b')
    #pid=patient.objects.all
    #pid=patient()
    #pid.id=random.randrange(1000000000,9999999999)
    
    return render(request, 'pform.html', )


def help(request):
    return render(request, 'help.html' )