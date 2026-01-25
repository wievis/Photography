from django.shortcuts import render
from .models import Photo

def home(request, lang='pl'):
    return render(request, 'home.html', {'photos': Photo.objects.order_by('order', '-created'), 'lang': lang})

def galeria(request, lang='pl'):
    return render(request, 'galeria.html', {'photos': Photo.objects.order_by('order', '-created'), 'lang': lang})

def kontakt(request, lang='pl'):
    return render(request, 'kontakt.html', {'lang': lang})

def privacy_policy(request, lang='pl'):
    return render(request, 'privacy_policy.html', {'lang': lang})