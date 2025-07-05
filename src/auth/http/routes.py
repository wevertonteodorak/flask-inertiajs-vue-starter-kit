import secrets
from flask import Blueprint, request, redirect, flash, current_app, url_for, session
from flask_inertia import render_inertia
from src.auth.models import User
from src.auth.http.requests import CreateUserRequest
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from src._core.auth_utils import get_auth_vars

auth = Blueprint('auth', __name__)

@auth.get('/login')
def login():
    providers = get_auth_vars()
    return render_inertia('auth/Login', props={
        "providers": lambda: list(providers),
    })

@auth.get('/login/<provider>')
def loginwith(provider):
    oauth = current_app.oauth
    nonce = secrets.token_urlsafe(16)
    session['nonce'] = nonce
    #try:
    redirect_uri = url_for('auth.authorize', provider=provider, _external=True)
    return oauth[provider].authorize_redirect(redirect_uri, nonce=nonce)
    #except:
    #    return  'Provedor não suportado', 400

@auth.get('/authorize/<provider>')
def authorize(provider):
    oauth = current_app.oauth
    nonce = session.get('nonce')
    token = oauth[provider].authorize_access_token()
    user_info = oauth[provider].parse_id_token(token,  nonce=nonce)
    user = User.query.filter_by(email=user_info.email).first()
    if user:
        login_user(user)
        return redirect('/dashboard')
    flash('Sua conta não está autorizada a acessar. Contate o administrador.', category='error')
    return redirect('/login')

@auth.post('/login')
def authenticate_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect('/dashboard')
    else:
        flash('Invalid email or password', category='error')
        return redirect('/login')

@auth.post('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfully', category='success')
    return redirect('/login')

@auth.get('/reset-password')
def reset_password():
    return render_inertia('auth/ResetPassword')

@auth.get('/forgot-password')
def forgot_password():
    return render_inertia('auth/ForgotPassword')   

@auth.get('/register')
def register():
    return render_inertia('auth/Register')

@auth.post('/register')
def create_user():
    try:
        data = CreateUserRequest(request).validate()
        password_hash = generate_password_hash(data['password'])
        user = User.create_user(name=data['name'], email=data['email'], password=password_hash)
        flash('User created successfully', category='success')
        if user:
            return redirect('/login?success=registered')
    except Exception as e:
        #raise e
        return redirect('/register')

    return redirect('/register')
