from pydantic import BaseModel, validator, EmailStr


class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    username: str
    email: str
