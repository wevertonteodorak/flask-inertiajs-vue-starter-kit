from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, validator, field_validator, model_validator
from src.auth.models import User


class CreateUserSchema(BaseModel):
    name: str = Field(..., min_length=10, max_length=50, description="The name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=6, max_length=128, description="The password for the user")
    password_confirmation: str = Field(..., min_length=6, max_length=128, description="The password for the user")

    @field_validator('email')
    @classmethod
    def email_must_be_unique(cls, email: str):
        if User.get_user_by_email(email):
            raise ValueError('Email already exists')
        return email
        
    # @field_validator('email')
    # @classmethod
    # def email_must_in_list(cls, email: str):
    #     print(f"Validating email: {email}")
    #     if not email in ['@sonda.com']:
    #         raise ValueError('Email domain is not allowed')
    #     return email
    
    @model_validator(mode='after')
    def passwords_must_match(self):
        if self.password and self.password != self.password_confirmation:
            raise ValueError('Passwords do not match')
        return self
        
class UpdateUserSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=10, max_length=50, description="The name of the user")
    email: Optional[EmailStr] = Field(None, description="The email address of the user")
    original_email: Optional[EmailStr] = Field(None, description="The email address of the user")

class UpdateUserPasswordSchema(BaseModel):
    password: str = Field(..., min_length=6, max_length=128, description="The new password for the user")
    password_confirmation: str = Field(..., min_length=6, max_length=128, description="The confirmation of the new password")
    current_password: str = Field(None, min_length=6, max_length=128, description="The password for the user")

    @model_validator(mode='after')
    def passwords_must_match(self):
        if self.password and self.password != self.password_confirmation:
            raise ValueError('Passwords do not match')
        return self