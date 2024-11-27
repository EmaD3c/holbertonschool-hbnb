import unittest
from app.models.review import (
    Review,
)
from datetime import datetime
from app.models.place import Place
from app.models.user import User


class TestReview(unittest.TestCase):
    def setUp(self):
        """Initialisation of User and Place objects for tests.."""
        self.valid_user = User("John", "Doe", "john.doe@gmail.com")
        self.valid_place = Place(
            "Beautiful House", 150.0, 34.05, -118.25, self.valid_user.uuid
        )
        self.valid_text = "This place is amazing!"
        self.valid_rating = 5
        self.review = Review(
            self.valid_text,
            self.valid_rating,
            self.valid_user.uuid,
            self.valid_place.uuid,
        )

    def test_create_review(self):
        """Test the creation of a review with valid attributes."""
        self.assertEqual(self.review.text, self.valid_text)
        self.assertEqual(self.review.rating, self.valid_rating)
        self.assertIsNotNone(self.review.uuid)  # Vérifie que l'UUID est généré
        self.assertIsInstance(
            self.review.created_at, datetime
        )  # Vérifie que created_at est un datetime

    def test_empty_text(self):
        """Test la création d'une revue avec un texte vide."""
        with self.assertRaises(ValueError):
            Review("", self.valid_rating, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_too_low(self):
        """TTest the creation of a review with empty text."""
        with self.assertRaises(ValueError):
            Review("Great place!", 0, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_too_high(self):
        """Test the creation of a review with too high a rating."""
        with self.assertRaises(ValueError):
            Review("Great place!", 6, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_type(self):
        """Test the creation of a review with an invalid note type."""
        with self.assertRaises(ValueError):
            Review("Great place!", "five", self.valid_user.uuid, self.valid_place.uuid)

    def test_update_review(self):
        """Test the creation of a review with an invalid note type."""
        data = {"text": "Updated review", "rating": 4}
        self.review.update(data)
        self.assertEqual(self.review.text, "Updated review")
        self.assertEqual(self.review.rating, 4)

    def test_update_empty_text(self):
        """Test updating a review with empty text."""
        with self.assertRaises(ValueError):
            self.review.update({"text": ""})

    def test_update_invalid_rating(self):
        """Test updating a review with an invalid rating."""
        with self.assertRaises(ValueError):
            self.review.update({"text": "HA!", "rating": 10})


if __name__ == "__main__":
    unittest.main()