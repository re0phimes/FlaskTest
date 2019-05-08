from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = StringField('StartTime', render_kw={'placeholder':'StartTime'})
    et = StringField('EndTime', render_kw={'placeholder':'EndTime'})
    submit = SubmitField('Go')