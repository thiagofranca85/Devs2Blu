# encuiptar as senhas (passwords) do usuario
SECRET_KEY = '123'

#string conexao
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "thiagoaf",
    senha = "123456",
    servidor = "localhost:5435",
    database = "postgres"
)