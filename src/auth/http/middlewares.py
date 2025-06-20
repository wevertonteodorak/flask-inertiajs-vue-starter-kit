from flask import flash, request, redirect
from flask_login import login_user, logout_user, current_user


def guard_auth_routes():
    """
    Middleware to guard authentication routes.
    This function can be used to check if the user is authenticated
    or to perform any other pre-request logic.
    """
    
    # Example: Check if user is authenticated
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page.', category='error')
        return redirect('/login?next=' + request.path)
    
    return None 