from app import db
from sqlalchemy.orm import relationship


class PlaceAmenity(db.Model):
    """Represent an associative table for Place and Amenity."""

    __tablename__ = "place_amenities"

    place_id = db.Column(db.String(36), db.ForeignKey("places.uuid"), primary_key=True)
    amenity_id = db.Column(
        db.String(36), db.ForeignKey("amenities.uuid"), primary_key=True
    )
    place = relationship("Place", back_populates="place_amenities", overlaps="amenities,places")
    amenity = relationship("Amenity", back_populates="amenity_places", overlaps="amenities,places")