from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Comment,Pitch

class PitchForm(FlaskForm):

    title = StringField('Enter pitch category',validators=[Required()])
    description= TextAreaField('pitch description')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = TextAreaField('Enter comment.',validators = [Required()])
    submit = SubmitField('Submit')

