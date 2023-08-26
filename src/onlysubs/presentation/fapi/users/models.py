from pydantic import BaseModel, EmailStr, Field


class ActivateUserModel(BaseModel):
    activation_token: str


class RegisterUserModel(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3)
    first_name: str
    last_name: str
    password: str = Field(min_length=6)
