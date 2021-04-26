from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class contactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    number = IntegerField('number', validators=[DataRequired()])
    web = StringField('website',)
    message = StringField('enter your message', validators=[DataRequired()])


class subscribeEmail(FlaskForm):
    emailName = StringField('name', validators=[DataRequired()])
    emailNemail = StringField('email', validators=[DataRequired()])