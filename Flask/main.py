from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)

@app.route('/')
def inicio():
    pessoa1 = Pessoa('Thiago', 37, 1.88)
    pessoa2 = Pessoa('Gisele', 25, 1.56)
    pessoa3 = Pessoa('Vander', 40, 1.80)

    lista = [pessoa1, pessoa2, pessoa3]

    return render_template('index.html', titulo = 'Thiago', pessoas = lista)

@app.route('/novo')
def novo():
    return '<h1>Rota Nova</h1>'


app.run()