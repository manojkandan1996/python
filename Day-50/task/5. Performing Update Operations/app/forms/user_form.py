from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Optional

class UserEditForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    is_active = BooleanField("Is Active")
    current_password = PasswordField("Current Password (required for changes)", validators=[Optional()])
    new_password = PasswordField("New Password", validators=[Optional()])
    submit = SubmitField("Update")
