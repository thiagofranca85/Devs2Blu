from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:aluno_id>', views.aluno, name='aluno'),
]