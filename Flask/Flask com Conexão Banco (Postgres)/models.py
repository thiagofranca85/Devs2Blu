from main import db
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