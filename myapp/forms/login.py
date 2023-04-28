from wtforms import StringField, BooleanField , Form 
from wtforms.validators import Length , Email
from myapp.forms.BaseForm import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators = [Email()])
    password = StringField(validators = [Length(min=4 ,max=20)])