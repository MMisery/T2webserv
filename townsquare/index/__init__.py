"""
index

This package handles the server side logic behind the home page.

"""

from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
def home():
    return "Yo."

