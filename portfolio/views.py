# views.py
from django.shortcuts import render
from .models import Photo

def home(request, lang='pl'):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos, 'lang': lang})

def galeria(request, lang='pl'):
    photos = Photo.objects.all()
    return render(request, 'galeria.html', {'photos': photos, 'lang': lang})

def kontakt(request, lang='pl'):
    return render(request, 'kontakt.html', {'lang': lang})