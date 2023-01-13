from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aluno', views.aluno, name='aluno'),
]