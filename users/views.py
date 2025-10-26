from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from .forms import LogInForm
from .models import User

# View for the list of users.
def show_users(request):
    users = User.objects.all()
    return render(request, "list.html", {"users": users})

# View for logging in.
def login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            # Debe redireccionar a la página de perfil del usuario.
            return redirect("list_if_users")
    else:
        form = LogInForm()
    return render(request, "login.html", {"form": form})

# View for signing up.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_of_users")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form}) 


