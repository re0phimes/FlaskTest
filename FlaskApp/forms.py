from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = StringField('StartTime', render_kw={'placeholder':'StartTime'})
    et = StringField('EndTime', render_kw={'placeholder':'EndTime'})
    submit = SubmitField('Go')


class DBForm(FlaskForm):
        DBType = StringField('DBType', validators=[DataRequired(message='DBType cannot be empty')], render_kw={'placeholder':'mysql'})
        username = StringField('username', validators=[DataRequired(message='username cannot be empty')],
                             render_kw={'placeholder': 'root'})
        password = StringField('password', validators=[DataRequired(message='password cannot be empty')],
                             render_kw={'placeholder': '123456'})
        host = StringField('host/IP address', validators=[DataRequired(message='host cannot be empty')],
                             render_kw={'placeholder': 'localhost'})
        submit = SubmitField("connect")
