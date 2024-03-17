from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, 'index'),
    path('login', views.login, name='login')
]
