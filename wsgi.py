#!/usr/bin/env python3.4
"""
wsgi.py

This is the file that is responsible for running the application and
and other commands like the database migrations.

It shouldn't have any extensive logic.

"""

from townsquare import TownSquare
from flask_script import Manager
#from townsquare.api import apimanager
import townsquare.api

application = TownSquare.create_app()
manager = Manager(application)
townsquare.api.apimanager.init_app(application)


if __name__ == '__main__':

    manager.run(default_command='runserver')


