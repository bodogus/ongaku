from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
        path('', views.crear_reseña, name='crear_reseña'),
]
