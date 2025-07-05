from flask import Blueprint, request, redirect, flash, abort
from flask_login import current_user, logout_user
from flask_inertia import render_inertia
from src.auth.models import User
from src.auth.http.requests import CreateUserRequest, UpdateUserRequest, UpdatePasswordRequest

user = Blueprint('user', __name__, url_prefix='/profile')

@user.get('/')
def profile():
    return render_inertia('user/Profile')

@user.post('/')
def update_profile():
    try:
        data = UpdateUserRequest(request).validate()
        user = User.update_user(name=data['name'], email=data['email'], original_email=data['original_email'])
        flash('Profile updated successfully', category='success')
        if user:
            return redirect('/profile?success=updated')
    except Exception as e:
        return redirect('/profile')

    return redirect('/profile')

@user.get('/password')
def change_password():
    return render_inertia('user/Password')

@user.post('/password')
def update_password():
    try:
        data = UpdatePasswordRequest(request).validate()
        if current_user.password and not current_user.check_password(data['current_password']):
            flash({'current_password': 'Original password is incorrect'}, category='error')
            return redirect('/profile/password')
        
        user = User.update_user(password=data['password'], original_email=current_user.email)
        logout_user()
        flash('Password updated successfully', category='success')
        if user:
            return redirect('/login')
    except Exception as e:
        #raise e
        return redirect('/profile/password')

    return redirect('/profile/password')    