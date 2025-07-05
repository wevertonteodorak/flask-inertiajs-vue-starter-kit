from flask import get_flashed_messages
from flask_login import LoginManager, current_user

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