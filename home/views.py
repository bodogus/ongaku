from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def home(request):
    return render(request, 'home.html', {'usrname': request.user.username})
