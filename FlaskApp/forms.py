from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta



class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = DateTimeField('StartTime',format='%Y-%m-%d %H:%M:%S', render_kw={'placeholder':'StartTime in Format: %Y-%m-%d %H:%M:%S'},default=datetime.now() + timedelta(minutes=-5))
    et = DateTimeField('EndTime', format='%Y-%m-%d %H:%M:%S', render_kw={'placeholder':'EndTime in Format: %Y-%m-%d %H:%M:%S'},default=datetime.now())
    submit = SubmitField('Go')


class DBForm(FlaskForm):
        DBType = SelectField('DataBaseType', choices=[('mysql','MySql'),('sqlserver','SqlServer'),('posgresql','PosgreSQL')])
        username = StringField('username', validators=[DataRequired(message='username cannot be empty')],
                             render_kw={'placeholder': 'root'})
        password = PasswordField('password', validators=[DataRequired(message='password cannot be empty')],
                             render_kw={'placeholder': 'enter your password here'})
        host = StringField('host/IP address', validators=[DataRequired(message='host cannot be empty')],
                             render_kw={'placeholder': 'localhost'})
        submit = SubmitField("connect")
