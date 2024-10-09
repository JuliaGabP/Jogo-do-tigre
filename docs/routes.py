# docs/routes.py
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from docs import app, db, bcrypt
from docs.forms import LoginForm, RegistrationForm, UpdateAccountForm
from docs.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Sua conta foi criada! Agora você pode entrar', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login não realizado. Por favor, verifique o usuário e a senha', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/view_registration')
@login_required
def view_registration():
    return render_template('view_registration.html', title='View Registration', user=current_user)

@app.route('/change_registration', methods=['GET', 'POST'])
@login_required
def change_registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Atualiza username e email
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        # Atualiza a senha apenas se uma nova senha for fornecida
        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.password = hashed_password
        
        db.session.commit()
        flash('Sua conta foi atualizada com sucesso!', 'success')
        return redirect(url_for('view_registration'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    return render_template('change_registration.html', title='Change Registration', form=form)

@app.route('/delete_registration', methods=['GET', 'POST'])
@login_required
def delete_registration():
    form = LoginForm()  # Utiliza o LoginForm para confirmar a senha
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.password.data):
            db.session.delete(current_user)
            db.session.commit()
            flash('Sua conta foi deletada com sucesso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Senha incorreta. Tente novamente.', 'danger')
    return render_template('delete_registration.html', title='Delete Registration', form=form)

@app.route('/game')
@login_required
def game():
    return render_template('game.html')  # Você pode criar um arquivo game.html para essa página
