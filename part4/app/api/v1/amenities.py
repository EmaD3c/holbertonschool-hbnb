from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("Amenities", description="Amenity operations")

# Define the amenity model for input validation and documentation
amenity_model = api.model(
    "Amenity", {"name": fields.String(required=True, description="Name of the amenity")}
)

facade = HBnBFacade()


@api.route("/")
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(201, "Amenity successfully created")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new amenity."""
        try:
            amenity_data = api.payload
            amenity = facade.create_amenity(amenity_data)
            return {"id": amenity.uuid, "name": amenity.name}, 201
        except ValueError as e:
            return {"message": {e}}, 400

    @api.response(200, "List of amenities retrieved successfully")
    def get(self):
        """Retrieve a list of all amenities."""
        amenity_list = facade.get_all_amenities()
        return [
            {"id": amenity.uuid, "name": amenity.name} for amenity in amenity_list
        ], 200


@api.route("/<amenity_id>")
class AmenityResource(Resource):
    @api.response(200, "Amenity details retrieved successfully")
    @api.response(404, "Amenity not found")
    def get(self, amenity_id):
        """Get amenity details by ID."""
        amenity = facade.get_amenity(amenity_id)
        if amenity is None:
            return {"message": "Amenity not found"}, 404
        return {"id": amenity.uuid, "name": amenity.name, "places": amenity.places}, 200

    @api.expect(amenity_model)
    @api.response(200, "Amenity updated successfully")
    @api.response(404, "Amenity not found")
    @api.response(400, "Invalid input data")
    def put(self, amenity_id):
        """Update an amenity's information"""
        try:
            amenity_data = api.payload
            amenity = facade.update_amenity(amenity_id, amenity_data)
            if amenity is None:
                return {"message": "Amenity not found"}, 404
            return {"message": "Amenity updated successfully"}, 200
        except ValueError as e:
            return {"message": {e}}, 400