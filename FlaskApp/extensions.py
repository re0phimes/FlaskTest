from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrp = Bootstrap()
db = SQLAlchemy()