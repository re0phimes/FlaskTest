from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired



class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = StringField('StartTime', render_kw={'placeholder':'StartTime'})
    et = StringField('EndTime', render_kw={'placeholder':'EndTime'})
    submit = SubmitField('Go')


class DBForm(FlaskForm):
        DBType = SelectField(u'DataBaseType', choices=[('mysql','MySql'),('sqlserver','SqlServer'),('posgresql','PosgreSQL')])
        username = StringField('username', validators=[DataRequired(message='username cannot be empty')],
                             render_kw={'placeholder': 'root'})
        password = StringField('password', validators=[DataRequired(message='password cannot be empty')],
                             render_kw={'placeholder': '123456'})
        host = StringField('host/IP address', validators=[DataRequired(message='host cannot be empty')],
                             render_kw={'placeholder': 'localhost'})
        submit = SubmitField("connect")
