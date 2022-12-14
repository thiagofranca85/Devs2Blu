from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.pessoa import Pessoa
from models.usuario import Usuario

pessoa1 = Pessoa('Haiko', '15', '1.50')
pessoa2 = Pessoa('Jean', '42', '1.84')
pessoa3 = Pessoa('Gisele', '16', '1.56')

lista = [
    pessoa1,
    pessoa2,
    pessoa3
    ]

usuario1 = Usuario('Vander','Luis','123')
usuario2 = Usuario('Thiago','Thiago','123')
usuario3 = Usuario('Gisele','Gigi','123')

usuarios = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3,
}

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def inicio():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proximo= url_for('novo')))
    
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return redirect(url_for('login', proximo= url_for('novo')))

    return render_template('novo.html', titulo = 'Cadastro Pessoa')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa(nome, idade, altura)

    lista.append(pessoas)

    return redirect(url_for('inicio'))

@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo = 'Login Usuario', proximo=proximo)


@app.route('/autenticar', methods=['POST',])
def autenticar():

    if request.form['usuario'] in usuarios:

        usuario = usuarios[request.form['usuario']]
        
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            
            flash(usuario.nickname + ' - Logado')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
        else:
            flash('Usuario ou senha invalidos')
            return redirect(url_for('login'))
    else:
        flash('Usuario ou senha invalidos')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():

    session['usuario_logado'] = None

    flash('Você foi Desconectado')
    return redirect(url_for('login'))

app.run(debug=True)