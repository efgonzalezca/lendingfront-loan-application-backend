import json
from pathlib import Path
from functools import wraps
from jsonschema import Draft7Validator, draft7_format_checker

from flaskr.exceptions.validation_exception import RequestValidationError

ROUTES = {
    'loan_evaluation': 'flaskr/schemas/loan/loan_evaluation.json'
}

VALIDATION_MESSAGES = {
    'required': 'is required',
    'minLength': 'must be at least {value} characters',
    'maxLength': 'must be at most {value} characters',
    'pattern': 'has an invalid format',
    'type': 'must be of type {value}'
}

def format_validation_message(error):
    """Genera un mensaje de error legible basado en el validador."""
    validator = error.validator
    value = error.validator_value

    if validator == 'required':
        return error.message.split("'")[1], VALIDATION_MESSAGES['required']
    
    if error.path:
        field = str(error.path[0])
        if validator in VALIDATION_MESSAGES:
            message = VALIDATION_MESSAGES[validator].format(value=value)
            return field, message
        return field, error.message
    
    return 'general', error.message

def validate_schema(route, request, validate_form=False, validate_args=False):
    """
    Validate the structure of the request.

    Parameters:
    route : str
        Key of the ROUTES dictionary pointing to the corresponding JSON schema file.
    request : flask.Request
        The Flask request object.
    validate_form : bool, optional
        If True, validates request.json body. Default is False.
    validate_args : bool, optional
        If True, validates request.args (URL parameters). Default is False.

    Returns:
    function
        Decorated function that runs schema validation before executing the view.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if route not in ROUTES:
                raise FileNotFoundError(f"No schema defined for route '{route}'")
            
            schema_path_str = ROUTES[route]
            schema_path = Path(schema_path_str)

            if not schema_path.exists():
                raise FileNotFoundError(f"Schema file not found at '{schema_path}'")

            with open(schema_path) as schema_file:
                schema = json.load(schema_file)

            if validate_args:
                data = request.args.to_dict()
            elif validate_form:
                data = request.get_json()
            else:
                data = {}

            validator = Draft7Validator(schema, format_checker=draft7_format_checker)
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

            error_dict = {}
            for error in errors:
                field, message = format_validation_message(error)
                if field not in error_dict:
                    error_dict[field] = message

            if error_dict:
                raise RequestValidationError(error_dict)

            return f(*args, **kwargs)
        return wrapper
    return decorator
