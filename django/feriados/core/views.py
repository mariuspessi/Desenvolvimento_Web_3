from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def natal(request):
    contexto = {
        'natal': True, 
        'tiradentes': False
    }
        
    return render(request, 'natal.html', contexto)