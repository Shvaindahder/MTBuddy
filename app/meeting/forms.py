from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, StringField, DateField, TimeField, TextField, SelectField, SubmitField
# from wtforms.validators import 


class CreateMeetingForm(FlaskForm):
    num_of_bikers = IntegerField("Number of bikers")
    area = StringField("Area")
    trail = StringField("Trail")
    date = DateField("Date")
    time = TimeField("Starting time")
    title = StringField("Add a title")
    description = TextField("Add a description")
    min_skill = SelectField("Skill level required", choices=list(range(1, 6)))
    submit = SubmitField("Create your meeting!")