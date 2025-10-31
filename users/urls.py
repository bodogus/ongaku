from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
        #path('list/', views.show_users, name='list_of_users'), 
        path('registro/', views.registro, name='registro'),
        path('ingreso/', views.ingreso, name='ingreso'),
        path('salir/', views.salir, name='salir'),
        path('<str:username>/', views.mostrar_perfil, name='perfil'),
        ]
