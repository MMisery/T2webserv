#Attemps to set up API Management

from flask.ext.restless import APIManager
from townsquare import TownSquare
import townsquare.db


apimanager = APIManager(flask_sqlalchemy_db=db)
apimanager.init_app(app)

