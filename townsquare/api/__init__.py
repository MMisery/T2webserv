#Attemps to set up API Management

from flask_restless import APIManager
import townsquare.db


apimanager = APIManager(flask_sqlalchemy_db=townsquare.db.db)


role_blueprint = apimanager.create_api(townsquare.db.Role)
user_blueprint = apimanager.create_api(townsquare.db.User, methods=['GET', 'POST', 'PUT'])
