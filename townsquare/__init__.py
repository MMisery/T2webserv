
from flask import Flask


class TownSquare(Flask):

    def init_extension(self, ext, *args, **kwargs):
        """
        Flask extensions follow a pattern where they need to be
        initialized with the application. This method is just an
        alias to ext.init_app(application).

        """
        return ext.init_app(self, *args, **kwargs)

    @staticmethod
    def create_app(config_name=None):

        app = TownSquare(__name__)

        from townsquare.index import index

        app.register_blueprint(index)

        return app
