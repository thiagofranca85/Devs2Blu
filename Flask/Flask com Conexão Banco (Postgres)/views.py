from flask import Flask, render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Pessoas, Usuarios

@app.route('/')
def index():
    lista = Pessoas.query.order_by(Pessoas.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("lista.html", pessoas = lista)



#return redirect('/login')
@app.route('/novo')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        
        #recurso querystring
        return redirect(url_for('login', proximo= url_for('novo')))

    return render_template('novo.html', titulo='Nova Pessoa')




@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    #variavel nova recebendo classe pessoa e filtrando pelo nome
    pessoa = Pessoas(nome, idade, altura)

    #if condicional recebendo a variavel caso exista jogos cadastrados
    if pessoa:
        flash('Pessoa já existente')
        return redirect(url_for('index'))

    # variavel criada recebendo variaveis e as variaveis referente ao form
    nova_pessoa = Pessoas(nome=nome, idade=idade, altura=altura)
    # acessando a variavel db e o recurso session e adicionando dados a variavel nova_pessoa
    db.session.add(nova_pessoa)
    # acessando variavel db e o recurso session e comintado dados no banco
    db.session.commit()
    # redirecionando para a lista de pessoas
    return redirect(url_for('lista'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('editar')))
    # Fazer um query do banco
    pessoa = Pessoas.query.filter_by(id=id).first()
    return render_template('editar.html', titulo = 'Editar Pessoas', pessoa = pessoa)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    pass

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Voce foi desconectado.')

    return redirect(url_for('login'))

@app.route('/login')
def login():
        proximo = request.args.get('proximo')
        return render_template('login.html', proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + ' - Logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('Usuario ou Senha Incorretos - Tente Novamente.')
        #dinamizando url

        return redirect(url_for('login'))

