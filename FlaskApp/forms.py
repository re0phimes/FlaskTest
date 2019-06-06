from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta
from getPCmemory import process_list

processlist = process_list()

class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = DateTimeField('StartTime',format='%Y-%m-%d %H:%M:%S', render_kw={'placeholder':'StartTime in Format: %Y-%m-%d %H:%M:%S'},default=datetime.now() + timedelta(minutes=-5))
    et = DateTimeField('EndTime', format='%Y-%m-%d %H:%M:%S', render_kw={'placeholder':'EndTime in Format: %Y-%m-%d %H:%M:%S'},default=datetime.now())
    submit = SubmitField('Go')


class DBForm(FlaskForm):
        DBType = SelectField('DataBaseType', choices=[('mysql','MySql'),('sqlserver','SqlServer'),('posgresql','PosgreSQL')])
        username = StringField('username', validators=[DataRequired(message='username cannot be empty')],
                             render_kw={'placeholder': 'root'}, default='root')
        password = PasswordField('password', validators=[DataRequired(message='password cannot be empty')],
                             render_kw={'placeholder': 'enter your password here'}, default='123456')
        host = StringField('host/IP address', validators=[DataRequired(message='host cannot be empty')],
                             render_kw={'placeholder': 'localhost'},default='localhost')
        port = StringField('PORT', validators=[DataRequired(message='port cannot be empty')],
                             render_kw={'placeholder': '3306'},default='3306')
        DBname = StringField('DBname', render_kw={'placeholder':'Test'},default='test')
        Table = StringField('Table', render_kw={'placeholder':'memory'},default='memory')
        submit = SubmitField("connect")

class ProcessForm(FlaskForm):
        processName = SelectField('Select Your Process', choices=processlist)