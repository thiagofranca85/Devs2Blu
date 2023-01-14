from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    alunos = {
        1:'Thiago',
        2:'Jean',
        3:'Gisele'
    }
    dados = {
        'nome_do_aluno' : alunos
    }
    return render(request, 'index.html', dados)

def aluno(request):
    return render(request, 'aluno.html')