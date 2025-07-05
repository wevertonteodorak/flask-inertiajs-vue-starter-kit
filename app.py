
import os
from dotenv import load_dotenv
from flask import Flask
from flask_inertia import Inertia
from flask_login import LoginManager
from src.user.routes import user as user_routes
from src.auth.http.middlewares import guard_auth_routes
from config.app import app_config
from config.auth import auth_config
from config.routes import routes
from src.app.database import db
from src.auth.models import User
from src._core.http_utils import register_routes
from src._core.auth_utils import create_oauth, register_enabled_providers
from src._core.app_utils import app_props

load_dotenv()
data_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

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
    register_routes(app, routes)
    
    oauth = create_oauth(app)
    register_enabled_providers(oauth, app)
    with app.app_context():
        import config.commands
    return app

app = create_app()

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)