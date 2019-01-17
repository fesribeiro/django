from django.shortcuts import render
from perfis.models import Perfil
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    if perfil_id == '1':
        perfil = Perfil('Felipe Ribeiro', 'felipe.ribeiro@fortbrasil.com.br', '997969128', 'Fortbrasil')
    elif perfil_id == '2':
        perfil = Perfil('Wellyngton.braz', 'Wellyngton.braz@fortbrasil.com.br', '89876554', 'Fortbrasil')
    return render(request, 'perfis.html', {"perfil" : perfil})



