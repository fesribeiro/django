from django.shortcuts import render
from perfis.models import Perfil
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfis.html', {"perfil" : perfil})

def teste(request, perfil_nome):
    perfil_nome = Perfil.objects.get(nome=perfil_nome)
    return render(request, 'perfis.html', {"perfil" : perfil_nome})
    


