from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.pessoa import Pessoa
from models.usuario import Usuario

pessoa1 = Pessoa('Thiago', 37, 1.88)
pessoa2 = Pessoa('Gisele', 25, 1.56)
pessoa3 = Pessoa('Vander', 40, 1.80)

lista = [pessoa1, pessoa2, pessoa3]

usuario1 = Usuario('Thiago','xDraKx','123')
usuario2 = Usuario('Vander','Vlaus','123')
usuario3 = Usuario('Larissa','Lari','123')

usuarios = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def inicio():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'), )
    return render_template('index.html', titulo = 'Tabela de Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')

    return render_template('novo.html', titulo = 'Cadastro de Pessoas')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    pessoa = Pessoa(nome, idade, altura)
    lista.append(pessoa)
    return redirect(url_for('inicio'))

@app.route('/login')
def login():

    return render_template('login.html', titulo = 'Login Usuario')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:

        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash(usuario.nickname + ' - Usuario Logado')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    else:
        flash('Usuario ou Senha Inválidos')
        return redirect('login')

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    session.clear()
    flash('Voce foi desconectado.')
    return redirect(url_for('login'))

app.run(debug=True)