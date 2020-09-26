from django.shortcuts import render, redirect
from pip._vendor.requests import Response

from .models import Persona
from .forms import PersonaForm

def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html', contexto)

def registro(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
        'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form': form
        }
    if form.is_valid():
        if (form) == '4' or '5' or '6' or '7' or '8' or '9' or '10':
            form.save()
            return redirect('index')
        elif (form) == '1' or '2' or '3':
            return Response('Debes de caminar más!')


    return render(request, 'registros.html', contexto)

