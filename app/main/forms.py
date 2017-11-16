from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    username = StringField('UserName', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Login')
