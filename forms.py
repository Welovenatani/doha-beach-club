from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    event = StringField('Event', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Book Now')

