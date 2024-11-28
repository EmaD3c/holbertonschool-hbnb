from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

from app.api.v1.users import api as users_api
from app.api.v1.places import api as places_api
from app.api.v1.amenities import api as amenities_api
from app.api.v1.reviews import api as reviews_api
from app.api.v1.auth import api as auth_api
from app.api.v1.admin import api as admin_api


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    api = Api(app, version="1.0", title="HBnB API", description="HBnB Application API")
    api.add_namespace(users_api, path="/api/v1/users")
    api.add_namespace(places_api, path="/api/v1/places")
    api.add_namespace(amenities_api, path="/api/v1/amenities")
    api.add_namespace(reviews_api, path="/api/v1/reviews")
    api.add_namespace(auth_api, path="/api/v1/auth")
    api.add_namespace(admin_api, path="/api/v1/admin")

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    return app
