from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services.facade import HBnBFacade
from .users import user_model
from .amenities import amenity_model
from .places import place_model

api = Namespace("Admin", description="Admin operations")

admin_model = api.inherit(
    "Admin",
    user_model,
    {"is_admin": fields.Boolean(required=True, description="The role of the user")},
)


facade = HBnBFacade()


@api.route("/users/")
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        user_data = request.json
        email = user_data.get("email")

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {"error": "Email already registered"}, 400

        # Logic to create a new user
        new_user = facade.create_user(user_data)
        try:
            return {
                "id": new_user.uuid,
                "message": "The user is successfully registered."
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400


@api.expect(admin_model, validation=True)
@api.route("/users/<user_id>")
class AdminUserModify(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()

        # If 'is_admin' is part of the identity payload
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        data = request.json
        email = data.get("email")

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.uuid != user_id:
                return {"error": "Email is already in use"}, 400

        # Logic to update user details, including email and password
        try:
            updated_user = facade.update_user(user_id, data)

            return {
                "id": updated_user.uuid,
                "first_name": updated_user.first_name,
                "last_name": updated_user.last_name,
                "email": updated_user.email,
                "updated_at": updated_user.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.expect(amenity_model, validation=True)
@api.route("/amenities/")
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        try:
            amenity_data = api.payload
            amenity = facade.create_amenity(amenity_data)
            return {"id": amenity.uuid, "name": amenity.name}, 201
        except ValueError as e:
            return {"message": {e}}, 400


@api.expect(amenity_model, validation=True)
@api.route("/amenities/<amenity_id>")
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        # Logic to update an amenity
        try:
            amenity_data = api.payload
            amenity = facade.update_amenity(amenity_id, amenity_data)
            if amenity is None:
                return {"message": "Amenity not found"}, 404
            return {"message": "Amenity updated successfully"}, 200
        except ValueError as e:
            return {"message": {e}}, 400


@api.expect(place_model, validation=True)
@api.route("/places/<place_id>")
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()

        # Set is_admin default to False if not exists
        is_admin = current_user.get("is_admin", False)
        user_id = current_user.get("id")

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {"error": "Unauthorized action"}, 403

        # Logic to update the place
        try:
            place_data = api.payload
            updated_place = facade.update_place(place_id, place_data)
            if not updated_place:
                return {"error": "Place not found"}, 404
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400