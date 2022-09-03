from django.shortcuts import render, redirect
from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from AppFinal.forms import *
from AppFinal.models import Impuestos, Monotributista, ResponsableInscripto



def inicio(request):
    
    return render(request, 'index.html')


def monotributista(request):
    
    monotributista1 = Monotributista(categoria="A", nombre="José", apellido="Hernandez", edad=55 , mail="josehernandez@gmail.com")
    monotributista1.save()
    
    monotributistas = Monotributista.objects.all()[:3]
    
    contexto = {
        "monotributistas":monotributistas,
            }
    return render(request, 'AppFinal/monotributistas.html', contexto)


def responsable_inscripto(request):
    
    responsable_inscripto1 = ResponsableInscripto(sociedad="S.R.L.", nombre="Maria", apellido="Gomez", edad=44 , mail="mariagomez@gmail.com")
    responsable_inscripto1.save()
    
    responsables = ResponsableInscripto.objects.all()[:3]
    
    contexto = {
        "responsables":responsables,
            }
    return render(request, 'AppFinal/responsables_inscriptos.html', contexto)


def impuestos(request):
    
    impuestos1 = Impuestos(asesoramientofiscal="I.V.A", nombre="Marcos", apellido="Fernandez", edad=65 , mail="marcosfernandez@gmail.com")
    impuestos1.save()
    
    impuestos = Impuestos.objects.all()[:3]
    
    contexto = {
        "impuestos":impuestos,
            }
    return render(request, 'AppFinal/impuestos.html', contexto)


def formulario(request):
    
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            formulario1 = Monotributista(nombre=data.get('nombre'), apellido=data.get('apellido'))
            formulario1.save()
            
            return redirect('AppFinalFormulario')
        
   
    
    contexto = {
        
        'form':Formulario(),
        
       
    }
    
    return render (request, 'AppFinal/formulario.html', contexto)


def busqueda_nombre(request):
    
    contexto = {
        
        'form': BusquedaNombreFormulario(),
    
    }
    
    return render(request, 'AppFinal/busqueda_nombre.html', contexto)


def busqueda_nombre_post(request):
    
    nombre = request.GET.get('nombre')
    
    monotributista = Monotributista.objects.filter(nombre__icontains=nombre)
    
    contexto = {
        
        'monotributista':monotributista
    }
    
    return render (request, 'AppFinal/formulario_filtrado.html', contexto)