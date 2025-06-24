
import click
import os
from flask import Flask, get_flashed_messages, flash, redirect
from flask_inertia import Inertia, render_inertia
from flask_login import LoginManager, current_user
from src.app.http.routes import app_blueprint as app_routes
from src.auth.http.routes import auth as auth_routes
from src.user.routes import user as user_routes
from src.auth.http.middlewares import guard_auth_routes
from config.app import app_config
from config.auth import auth_config
from src.app.database import db
from src.auth.models import User


data_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

def app_props():
    if current_user.is_authenticated:
        user = {
            'name': current_user.name,
            'email': current_user.email,
        }
    else:
        user = {
            'name': 'Guest',
            'email': 'guest@domain.local'
        }

    return {
        'user': user,
        'flash': get_flashed_messages(with_categories=True, category_filter=['success', 'info']),
        'errors': get_flashed_messages(with_categories=True, category_filter=['error']),
        'csrf_token': 'dummy-token'
    }


def create_app():
    app = Flask(
        __name__, 
        static_folder='static/public', 
        template_folder='templates',
        instance_path=data_path
    )
    app.config.update(app_config)
    app.config.update(auth_config)
    db.init_app(app)

    app.login_manager = LoginManager(app)
    app.login_manager.login_view = "auth.login"
    app.inertia = Inertia(app)
    app.inertia.share('auth', app_props)
    app.inertia.share('app', app_props)
    return app

app = create_app()

@app.cli.command('db:migrate')
def db_migrate():
    import config.models
    with app.app_context():
        db.create_all()

@app.cli.command('db:fresh')
def db_fresh():
    """Reset and Initialize the database."""
    import config.models
    db.drop_all()
    click.echo('Dropped database.')
    db.create_all()
    click.echo('Initialized database.')

## Register middlewares
app.before_request_funcs = {
    'user': [
        guard_auth_routes
    ]
}

#### Register blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(user_routes)
app.register_blueprint(app_routes)

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)