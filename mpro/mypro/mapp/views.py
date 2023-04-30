from django.shortcuts import render
from django.http import HttpResponse
from .models import patient, clinic
import random


# Create your views here.

def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html' )

def cregister(request):
    return render(request, 'cregister.html' )

def pform(request):
    if request.method=="POST":
        img=request.POST.get('img')
        gender=request.POST.get('gender')
        type=request.POST.get('type')
        kind=request.POST.get('kind')
        stage=request.POST.get('stage')
        clid = request.POST.get('clid')
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        age =request.POST.get('age') 
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address_a = request.POST.get('address_a')
        address_b = request.POST.get('address_b')
    return render(request, 'pform.html', )

def help(request):
    return render(request, 'help.html' )