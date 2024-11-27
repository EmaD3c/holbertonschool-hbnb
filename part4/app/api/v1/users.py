from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace("Users", description="User operations")

# Define the user model for input validation and documentation
user_model = api.model(
    "User",
    {
        "first_name": fields.String(
            required=True, description="First name of the user"
        ),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
        "password": fields.String(
            required=True, format="password", description="Password of the user"
        ),
    },
)

facade = HBnBFacade()


@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(400, "Email already registered")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new user."""
        try:
            user_data = api.payload

            # Simulate email uniqueness check (to be replaced by real validation with persistence)
            existing_user = facade.get_user_by_email(user_data["email"])
            if existing_user:
                return {"error": "Email already registered"}, 400

            new_user = facade.create_user(user_data)
            return {
                "id": new_user.uuid,
                "message": "The user is successfully registered."
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "List of users retrieved successfully")
    @api.response(404, "User not found")
    def get(self):
        """Retrieve a list of all users."""
        try:
            users_list = facade.get_all_users()

            if not users_list:
                return {"message": "No user found"}, 404

            # Get the name of each user
            return [
                {
                    "id": user.uuid,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "reviews": len(user.reviews),
                    "places": len(user.places),
                }
                for user in users_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<user_id>")
class UserResource(Resource):
    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user details by ID."""
        try:
            user = facade.get_user(user_id)

            if not user:
                return {"error": "User not found"}, 404

            return {
                "id": user.uuid,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                #                "places": user.places,
                #                "reviews": user.reviews,
                "created_at": user.created_at.isoformat(),
                "updated_at": user.updated_at.isoformat(),
            }, 200

        except ValueError as e:
            return {"error": str(e)}, 400

    @api.expect(user_model, validation=True)
    @api.response(200, "User details updated successfully")
    @api.response(404, "User not found")
    @jwt_required()
    def put(self, user_id):
        """Modify user details."""
        current_user = get_jwt_identity()

        user = facade.get_user(user_id)

        # Check if user exists
        if not user:
            return {"error": "User not found"}, 404

        # Check if user has modification rights
        if current_user["id"] != user.uuid:
            return {"error": "Unauthorized action."}, 403

        try:
            # Get the query's data
            user_data = api.payload

            # Prevents changes to email address or password
            try:
                password_is_valid = user.verify_password(user_data.get("password", ""))

            except ValueError:
                password_is_valid = False
            if user_data["email"] != user.email or not password_is_valid:
                return {"error": "You cannot modify email or password."}, 400

            # Update the user
            updated_user = facade.update_user(user_id, user_data)

            return {
                "id": updated_user.uuid,
                "first_name": updated_user.first_name,
                "last_name": updated_user.last_name,
                "updated_at": updated_user.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    @jwt_required()
    def delete(self, user_id):
        """Delete user details."""
        current_user = get_jwt_identity()

        user = facade.get_user(user_id)

        # Check if user exists
        if not user:
            return {"error": "User not found"}, 404

        # Check if user has modification rights
        if current_user["id"] != user.uuid:
            return {"error": "Unauthorized action."}, 403

        try:
            # Update the user
            is_deleted = facade.delete_user(user_id)

            if is_deleted:
                return {
                    "message": "The user has been successfully deleted"
                }, 200

            raise Exception("The user cannot be deleted.")
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<user_id>/reviews")
class UserReview(Resource):
    @api.response(200, "User's reviews retrieved successfully")
    @api.response(404, "User not found or no reviews")
    def get(self, user_id):
        """Get user's reviews by ID."""
        try:
            user = facade.get_user(user_id)
            if not user:
                return {"error": "User not found"}, 404
            reviews_list = user.reviews

            if not reviews_list:
                return {"message": "No reviews found for this user"}, 404
            return [
                {
                    "id": review_id,
                    "place id": facade.get_review(review_id).place_id,
                    "text": facade.get_review(review_id).text,
                    "rating": facade.get_review(review_id).rating,
                }
                for review_id in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400