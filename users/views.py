from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from reviews.models import Review
from django.shortcuts import get_object_or_404


def registro(request):
    if request.method == "POST":
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistroFormulario()

    return render(request, "registrar.html", {"form": form}) 

def ingreso(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Iniciar sesión al usuario
                return redirect('explore:home') 
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrecta.')
    else:
        form = AuthenticationForm()
    return render(request, 'ingresar.html', {'form': form})

def salir(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('explore:home')

def mostrar_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    reseñas = Review.objects.filter(usuario=usuario)
    return render(request, 'perfil.html', {'usuario': usuario, 'reseñas': reseñas})

