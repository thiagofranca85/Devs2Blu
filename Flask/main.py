from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('Thiago', 37, 1.88)
pessoa2 = Pessoa('Gisele', 25, 1.56)
pessoa3 = Pessoa('Vander', 40, 1.80)

lista = [pessoa1, pessoa2, pessoa3]

app = Flask(__name__)

@app.route('/')
def inicio():

    return render_template('index.html', titulo = 'Tabela de Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Cadastro de Pessoas')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    pessoa = Pessoa(nome, idade, altura)
    lista.append(pessoa)
    return redirect('/')


app.run(debug=True)