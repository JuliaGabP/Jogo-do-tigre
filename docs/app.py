from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random
import requests
from flask_migrate import Migrate

# Depois de inicializar o app e o db


# Inicialização do Flask
app = Flask(__name__)

# Configurações básicas
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost/tigre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização de extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
migrate = Migrate(app, db)

# Definição do modelo User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Integer, default=1000)
    results = db.relationship('GameResult', backref='user', lazy=True)  # Relacionamento com GameResult

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.balance}')"

# Novo modelo GameResult para armazenar os resultados das apostas
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"GameResult('{self.balance}', '{self.timestamp}', User ID: {self.user_id})"

# Carregar usuário com Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/chart-data')
@login_required
def chart_data():
    results = GameResult.query.filter_by(user_id=current_user.id).order_by(GameResult.timestamp).all()

    # Gerando os dados para o gráfico
    x = list(range(1, len(results) + 1))
    y = [result.balance for result in results]

    # Retornando os dados como JSON
    return jsonify({'x': x, 'y': y})

# Importações locais após a inicialização para evitar problemas de importação circular
from docs.forms import LoginForm, RegistrationForm

if __name__ == '__main__':
    app.run(debug=True)
