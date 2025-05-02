from flask import jsonify
from werkzeug.exceptions import InternalServerError, NotFound

from flaskr.exceptions.validation_exception import RequestValidationError

def register_error_handlers(app):
    @app.errorhandler(RequestValidationError)
    def handle_request_validation(e):
        return jsonify({
            'errors': e.errors
        }), 400

    @app.errorhandler(NotFound)
    def not_found(e):
        return jsonify({
            'message': 'The requested URL was not found on the server'
        }), 404

    @app.errorhandler(InternalServerError)
    def handel_internal_server_error(e):
        return jsonify({
            'message': 'Internal server error',
        }), 500
    
    @app.errorhandler(Exception)
    def handle_unexpected(e):
        return jsonify({
            'message': 'Internal server error',
        }), 500
