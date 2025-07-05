from src.app.http.base_request import BaseRequest
from src.auth.schemas import CreateUserSchema, UpdateUserSchema, UpdateUserPasswordSchema

class CreateUserRequest(BaseRequest):
    def schema(self):
        return CreateUserSchema
        

class UpdateUserRequest(BaseRequest):
    def schema(self):
        return UpdateUserSchema
    
class UpdatePasswordRequest(BaseRequest):
    def schema(self):
        return UpdateUserPasswordSchema