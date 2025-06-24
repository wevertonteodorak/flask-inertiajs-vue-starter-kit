from flask import Blueprint, request, redirect, flash
from flask_inertia import render_inertia
from src.auth.models import User
from src.auth.http.requests import CreateUserRequest
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.get('/login')
def login():
    return render_inertia('auth/Login')

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
        raise e
        return redirect('/register')

    return redirect('/register')
