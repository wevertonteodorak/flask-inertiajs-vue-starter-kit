from src.app.http.routes import app_blueprint as app_routes
from src.auth.http.routes import auth as auth_routes
from src.user.routes import user as user_routes
from src.auth.http.middlewares import guard_auth_routes

routes = [
    {'blueprint': app_routes, 'middlewares': [guard_auth_routes]},
    {'blueprint': user_routes, 'middlewares': [guard_auth_routes]},
    {'blueprint': auth_routes, 'middlewares': []},
]