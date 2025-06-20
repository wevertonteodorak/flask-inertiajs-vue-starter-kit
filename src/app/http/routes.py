from flask import Blueprint, request, redirect, flash
from flask_inertia import render_inertia


app_blueprint = Blueprint('app', __name__, url_prefix='/')


@app_blueprint.get('/')
def index():
    return redirect('/dashboard')

@app_blueprint.get('/dashboard')
def dashboard():
    return render_inertia('Home')