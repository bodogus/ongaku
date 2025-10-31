from django.shortcuts import render, redirect
from .forms import FormularioReseña

def crear_reseña(request):
    if not request.user.is_authenticated:
            mensaje = "Debes iniciar sesión para crear una reseña."
            return render(request, "no_autenticado.html", {"mensaje": mensaje})
    if request.method == 'POST':
        form = FormularioReseña(request.POST)
        if form.is_valid():
            # Crea el objeto pero no lo guarda
            reseña = form.save(commit=False) 
            # Asigna el usuario que hace la reseña
            reseña.usuario = request.user      
            reseña.save()                      
            return redirect('users:perfil', username=request.user.username)
    else:
        form = FormularioReseña()
    return render(request, 'reseñar.html', {'form': form})
