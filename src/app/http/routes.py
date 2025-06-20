from flask import Blueprint, request, redirect, flash
from flask_inertia import render_inertia


app_blueprint = Blueprint('app', __name__, url_prefix='/')


@app_blueprint.get('/')
def index():
    return redirect('/about')

@app_blueprint.get('/dashboard')
def dashboard():
    return render_inertia('Home')

@app_blueprint.get('/about')
def about():
    return render_inertia('About')