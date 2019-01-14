from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfis(request):
    return render(request, 'perfis.html')

