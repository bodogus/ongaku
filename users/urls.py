from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.login, name='login'),
        path('list/', views.show_users, name='list_of_users'), 
        path('signup/', views.signup, name='signup'),
        ]
