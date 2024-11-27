from app.models.place_amenity import PlaceAmenity
from app.persistence.repository import SQLAlchemyRepository


class PlaceAmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(PlaceAmenity)
