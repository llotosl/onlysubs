from pydantic import BaseModel, EmailStr, Field


class ActivateUserModel(BaseModel):
    activation_token: str


class RegisterUserModel(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3)
    first_name: str
    last_name: str
    password: str = Field(min_length=6)


class PublicUserModel(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    is_active: bool


class ResendActivationEmailModel(BaseModel):
    email: EmailStr
