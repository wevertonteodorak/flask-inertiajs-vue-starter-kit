

def register_http_error_handlers(app):
    """
    Register custom error handlers for HTTP errors.
    """
    @app.errorhandler(404)
    def not_found_error(error):
        return {"error": "Not Found"}, 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return {"error": "Internal Server Error"}, 500

    @app.errorhandler(400)
    def bad_request_error(error):
        return {"error": "Bad Request"}, 400

def register_routes(app, routes):
    """
    Register all routes for the application.
    """
    app.before_request_funcs = {}
    for route in routes:
        app.before_request_funcs.update({
            route['blueprint'].name: route['middlewares']
        })

        #### Register blueprint
        app.register_blueprint(route['blueprint'])
