#!/usr/bin/env python
"""
application.py

This is the file that is responsible for running the application and
and other commands like the database migrations.

It shouldn't have any extensive logic.

"""

from townsquare import TownSquare
from flask_script import Manager

app = TownSquare.create_app()
manager = Manager(app)


if __name__ == '__main__':

    manager.run(default_command='runserver')


