from django.shortcuts import render
from .models import Photo

def home(request, lang='en'):
    return render(request, 'home.html', {'photos': Photo.objects.all(), 'lang': lang})

def galeria(request, lang='en'):
    return render(request, 'galeria.html', {'photos': Photo.objects.all(), 'lang': lang})

def kontakt(request, lang='en'):
    return render(request, 'kontakt.html', {'lang': lang})

def privacy_policy(request, lang='en'):
    return render(request, 'privacy_policy.html', {'lang': lang})