from flask import flash
from pydantic import ValidationError

class BaseRequest():
    
    def __init__(self, request):
        self.request = request
    
    @property
    def schema(self):
        """
        This property should be overridden by subclasses to return the Pydantic schema class.
        """
        raise NotImplementedError("Subclasses must implement this property")
    
    def validate(self):
        try:
            data = self.request.get_json()
            schema = self.schema()
            return schema(**data).__dict__
        except ValidationError as e:
            errors = self.parse_pydantic_errors(e)
            flash(errors, category='error')
            raise ValueError(f"Validation failed: {errors}")
    
    def parse_pydantic_errors(self, e):
        """
        Parses Pydantic validation errors and returns a dictionary of error messages.
        """
        errors = {}
        for error in e.errors():
            try:
                field = error.get('loc')[0]
            except Exception as ex:
                field = 'unknown'
                print(f"Error parsing field location: {ex}")
            if errors.get(field):
                errors[field] += f", {error.get('msg')}"
            else:
                errors[field] = error.get('msg')
        return errors