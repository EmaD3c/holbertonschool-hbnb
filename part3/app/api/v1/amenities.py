from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')
facade = HBnBFacade()


# Define the amenity model for input validation and documentation
amenity_model = api.model(
    'Amenity',
    {'name': fields.String(
        required=True,
        description='Name of the amenity')})


@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity updated successfully')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        try:
            new_amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {"error": "Input data invalid"}, 400
        return {"id": new_amenity.id, "name": new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        return [{"id": i.id, "name": i.name} for i in facade.get_all_amenities()], 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        obj = facade.get_amenity(amenity_id)
        if not obj:
            return {"error": "Amenity not found"}, 404
        return { "id": obj.id, "name": obj.name }

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        obj = facade.get_amenity(amenity_id)
        if not obj:
            return {"error": "Amenity not found"}, 404

        facade.update_amenity(amenity_id, api.payload)
        return {"message": "Amenity successful updated"}, 200