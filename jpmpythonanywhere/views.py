from django.http import HttpResponse
from django.template import Template , Context , loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def inicio (request):
    
    
    return render(request, "inicio.html")

@login_required
def ejemplos (request):
    
    
    return render(request, "ejemplos.html")

@login_required
def agro (request):
    
    
    return render(request, "ej_agro.html")

@login_required
def agro_presupuestolp (request):
    
    
    return render(request, "ej_agro_presuplp.html")

@login_required
def mgba (request):
    
    
    return render(request, "ej_mgba.html")

@login_required
def agro_erdos (request):
    
    
    return render(request, "ej_agro_erdos.html")

@login_required
def agro_dashb (request):
    
    
    return render(request, "ej_agro_dashb.html")

@login_required
def spub (request):
    
    
    return render(request, "ej_spub.html")

@login_required
def nube (request):

    return render(request, "ej_nubepal.html")

def alta_usuario(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            
            return redirect('/')
        else:
            print(user_creation_form.errors)
        
    else:
        print("falló primer if")
    return render(request,"register.html",data )

def exit(request):
    logout(request)
    return redirect('/')