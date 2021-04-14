from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criando a API flask
app = Flask(__name__)
# Criando a instancia de sql alchemy
app.config['SECRET_KEY'] = 'senha123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'

db = SQLAlchemy(app)
db:SQLAlchemy
# Definindo a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


# Defininindo a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')
    

# Criando o banco
def inicializar_banco():
    db.drop_all()
    db.create_all()

    # Adicionando um autor à tabela Autor
    autor = Autor(nome='vagner', email='teste@gmail.com', senha=123, admin=True)
    db.session.add(autor)
    db.session.commit()


if __name__ == '__main__':
    inicializar_banco()