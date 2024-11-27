import uuid
from datetime import datetime
from app import db
from sqlalchemy.orm import validates, relationship


class Place(db.Model):
    """Represent an place."""

    __tablename__ = "places"

    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    _price = db.Column(db.Float, nullable=False)
    _latitude = db.Column(db.Float, nullable=False)
    _longitude = db.Column(db.Float, nullable=False)

    owner_id = db.Column(db.String(36), db.ForeignKey("users.uuid"), nullable=False)
    reviews = relationship("Review",
                           backref="place",
                           lazy=True,
                           cascade="all, delete-orphan")

    amenities = relationship(
        "Amenity",
        secondary="place_amenities",
        back_populates="places",
        cascade="all, delete",
        viewonly=True
    )

    place_amenities = relationship(
        "PlaceAmenity",
        back_populates="place",
        cascade="all, delete-orphan"
    )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("The price must be positive")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90 or not isinstance(value, float):
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180 or not isinstance(value, float):
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    def update(self, data):
        """Update place."""
        self.is_valid_length("title", data["title"])

        data["price"] = float(data["price"])
        data["latitude"] = float(data["latitude"])
        data["longitude"] = float(data["longitude"])

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Remove a review."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add a review to the place."""
        self.amenities.append(amenity)

    @validates("title")
    def is_valid_length(self, key, title):
        """Check the length of the title."""
        if title is None or not (1 <= len(title) <= 100):
            raise ValueError(f"{title} be between 1 and 100 characters.")
        return title