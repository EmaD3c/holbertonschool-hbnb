import uuid
from datetime import datetime
from app import db
from sqlalchemy.orm import validates


class Review(db.Model):
    """Represent a review."""

    __tablename__ = "reviews"

    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    place_id = db.Column(db.String(36),
                         db.ForeignKey("places.uuid", ondelete="CASCADE"),
                         nullable=False)
    user_id = db.Column(db.String(36),
                        db.ForeignKey("users.uuid", ondelete="CASCADE"),
                        nullable=False,)

    def update(self, data):
        """Update review."""
        self.text_exists(data["text"])
        self.is_valid_rating(data["rating"])

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    # def delete_review(self):

    def __repr__(self):
        return f"<Review id={self.uuid}, rating={self.rating}"

    @validates("text")
    def text_exists(self, key, text):
        """Check if the user has entered the fieldheck if the user has entered the field."""
        if not text:
            raise ValueError("Review text is required")
        return text

    @validates("rating")
    def is_valid_rating(self, key, rating):
        """Bound the value of the rating between 1 and 5."""
        try:
            rating_int = self.convert_to_int(rating)
            if rating_int is None or not (1 <= rating_int <= 5):
                raise ValueError
            return rating_int
        except ValueError:
            raise ValueError("Rating must be an integer between 1 and 5")

    def convert_to_int(self, rating):
        """Convert the user's rating into an integer."""
        try:
            return int(rating)
        except (TypeError, ValueError):
            return None
