from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from pydantic import BaseModel, field_validator, StringConstraints
import string
from typing_extensions import Annotated
from post_list import password_list


# Custom password validation class with pydantic
# Chwilowo bezużyteczne
class PasswordStr(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def password_validation(cls, password: str):
        if not any(letter in password for letter in string.punctuation):
            raise ValueError(
                "Password must contain at least one special punctuation character"
            )
        elif len(password) <= 5:
            raise ValueError("Password must be at least 6 characters long")
        elif not any(letter.isupper() for letter in password):
            raise ValueError("Password must contain at least one capital letter")
        elif not any(letter.isnumeric() for letter in password):
            raise ValueError("Password must contain at least one digit")
        elif password.lower() in [p.lower() for p in password_list]:
            raise ValueError("Come on, come up with something better!")
        else:
            return password


# Another pydantic, more cohesive, better designed
class Usernamestr(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=30,
            pattern=r"^[a-zA-Z0-9_]+$",
        ),
    ]


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Length(min=1, max=30), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=30)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up!")


class Loginform(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Keep you logged in?")
    submit = SubmitField("Sign Up!")
