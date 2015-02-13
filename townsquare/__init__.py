
from flask import Flask
from . import config

class TownSquare(Flask):

    def init_extension(self, ext, *args, **kwargs):
        """
        Flask extensions follow a pattern where they need to be
        initialized with the application. This method is just an
        alias to ext.init_app(application).

        """
        return ext.init_app(self, *args, **kwargs)

    @staticmethod
    #Create the application
    def create_app(config_name=None):

        app = TownSquare(__name__)

        #Set config on app
        app.config.from_object(config)

        from townsquare.index import index
        app.register_blueprint(index)

        from townsquare.db import db
        app.init_extension(db)
        db.init_app(app)

        with app.app_context():
            db.create_all()


        return app
