from authlib.integrations.flask_client import OAuth
from config.auth import auth_config

def create_oauth(app):
    oauth = OAuth(app)
    return oauth

def get_auth_vars():
    auth_enables = []
    for key, value in auth_config.items():
        auth_enables.append(key)
    return auth_enables

def register_enabled_providers(oauth, app):
    app.oauth = {}
    for key, auth_provider in auth_config.items():
        app.oauth[key.lower()] = oauth.register(
            name=key.lower(),
            client_id=auth_provider['client_id'],
            client_secret=auth_provider['client_secret'],
            #access_token_url=auth_provider['token_url'],
            #access_token_params=None,
            #authorize_url=auth_provider['auth_url'],
            #authorize_params=None,
            #api_base_url=auth_provider['base_url'],
            server_metadata_url=auth_provider['meta_url'],
            client_kwargs={'scope': 'openid email profile'}
        )