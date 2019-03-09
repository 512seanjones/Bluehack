from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    state = StringField('Street', validators=[DataRequired()])
    street = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Submit')
