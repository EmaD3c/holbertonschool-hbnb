from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace("Reviews", description="Review operations")

review_model = api.model(
    "Review",
    {
        "text": fields.String(required=True, description="Text of the review"),
        "rating": fields.String(required=True, description="Rating of the review"),
        "place_id": fields.String(required=True, description="Place of the review"),
        "user_id": fields.String(required=True, description="User writing the review"),
    },
)

facade = HBnBFacade()


@api.route("/")
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @api.response(201, "Review successfully created")
    @api.response(400, "Invalid input data")
    @jwt_required()
    def post(self):
        """Register a new review."""
        current_user = get_jwt_identity()

        try:
            review_data = api.payload

            # Check that the reviewer don't own the place
            place = facade.get_place(review_data["place_id"])
            if place.owner_id == current_user["id"]:
                return {"error": "You cannot review your own place"}, 400

            # Check that the user has not already reviewed this place
            user = facade.get_user(current_user["id"])
            for review in user.reviews:
                if place.uuid == review.place_id:
                    return {"error": "You have already reviewed this place"}, 400

            new_review = facade.create_review(review_data)

            return {
                "id": new_review.uuid,
                "text": new_review.text,
                "rating": new_review.rating,
                "place_id": new_review.place_id,
                "user_id": new_review.user_id,
                "created_at": new_review.created_at.isoformat(),
                "updated_at": new_review.updated_at.isoformat(),
            }, 201

        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "List of reviews retrieved successfully")
    @api.response(404, "Any review found")
    def get(self):
        """Retrieve a list of all reviews."""
        try:
            reviews_list = facade.get_all_reviews()
            if not reviews_list:
                return {"message": "No review found"}, 404
            return [
                {
                    "id": review.uuid,
                    "user_id": review.user_id,
                    "place_id": review.place_id,
                    "rating": review.rating,
                    "text": review.text,
                }
                for review in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<review_id>")
class ReviewResource(Resource):
    @api.response(200, "Display review details by ID.")
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Display review detail by ID."""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404
            return {
                "id": review.uuid,
                "user_id": review.user_id,
                "place_id": review.place_id,
                "rating": review.rating,
                "text": review.text,
                "created_at": review.created_at.isoformat(),
                "updated_at": review.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "Review details modified successfully")
    @api.response(404, "Review not found")
    @jwt_required()
    def put(self, review_id):
        """Modify review detail by ID."""
        current_user = get_jwt_identity()

        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404

            if current_user["id"] != review.user_id:
                return {"error": "Unauthorized action"}, 403

            review_data = api.payload

            # Ensure to keep the good user_id
            review_data["id"] = current_user["id"]

            facade.update_review(review_id, review_data)

            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(204, "Review successfully deleted")
    @api.response(404, "Review not found")
    @jwt_required()
    def delete(self, review_id):
        """Delete review by ID."""
        current_user = get_jwt_identity()

        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404

            # Check if the review belong to authenticated user
            if review.user_id != current_user["id"]:
                return {"error": "Unauthorized action"}

            facade.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 200

        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/user/<user_id>")
class UserReview(Resource):
    @api.response(200, "User's reviews retrieved successfully")
    @api.response(404, "User not found or no reviews")
    def get(self, user_id):
        """Get user reviews by ID."""
        try:
            user = facade.get_user(user_id)
            if not user:
                return {"error": "User not found"}, 404
            reviews_list = user.reviews
            if not reviews_list:
                return {"message": "No reviews found for this user"}, 404
            return [
                {
                    "reviews": review,
                }
                for review in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400