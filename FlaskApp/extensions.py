from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
from flask_nav.elements import *
from forms import QueryForm
from flask_sqlalchemy import SQLAlchemy


bootstrp = Bootstrap()
db = SQLAlchemy()