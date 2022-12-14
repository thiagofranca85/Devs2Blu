from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# encriptar os passwords do usuario
app.secret_key = '123'

#string conexao
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "thiagoaf",
    senha = "123456",
    servidor = "localhost",
    database = "postgres"
)

db = SQLAlchemy(app)

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), primary_key=True)
    idade = db.Column(db.String(40), nullable=False)
    altura = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

lista = Pessoas.query.order_by(Pessoas.id)

@app.route('/')
def index():
    lista = Pessoas.query.order_by(Pessoas.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("lista.html", titulo = 'jogos', jogos = lista)



#return redirect('/login')
@app.route('/novo')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        
        #recurso querystring
        return redirect(url_for('login2', proximo= url_for('novo')))

    return render_template('novo.html', titulo='Novo Jogo')




@app.route('/criar2', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoas(nome, idade, altura)

    lista.append(pessoa)

    return redirect(url_for('index'))





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
            

            flash(usuario.nickname + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))




app.run(debug=True)