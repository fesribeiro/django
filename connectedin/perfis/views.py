from django.shortcuts import render
from perfis.models import Perfil
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfis.html', {"perfil" : perfil})
