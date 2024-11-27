import uuid
from datetime import datetime
from app import db
from sqlalchemy.orm import validates, relationship


class Amenity(db.Model):
    """Represent an Amenity."""

    __tablename__ = "amenities"

    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    name = db.Column(db.String(50), nullable=False)

    places = relationship(
        "Place",
        secondary="place_amenities",
        back_populates="amenities",
        viewonly=True
    )

    amenity_places = relationship(
        "PlaceAmenity",
        cascade="all, delete-orphan"
    )

    def update(self, data):
        """Update name."""
        self.is_valid_length("name", data["name"])

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Amenity id={self.uuid}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at}>"

    @validates("name")
    def is_valid_length(self, key, name):
        """Check the length of the name."""
        if not (1 <= len(name) <= 50):
            raise ValueError(f"{name} be between 1 and 50 characters.")
        return name