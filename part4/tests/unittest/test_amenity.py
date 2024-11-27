import unittest
from datetime import datetime
from app.models.amenity import (
    Amenity,
)


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Initialisation d'un objet Amenity valide pour les tests."""
        self.valid_name = "Swimming Pool"
        self.amenity = Amenity(self.valid_name)

    def test_create_amenity(self):
        """Test la création d'un amenity avec un nom valide."""
        self.assertEqual(self.amenity.name, self.valid_name)
        self.assertIsNotNone(self.amenity.uuid)  # Vérifie que l'UUID est généré
        self.assertIsInstance(
            self.amenity.created_at, datetime
        )  # Vérifie que created_at est un datetime

    def test_update_name(self):
        """Test la mise à jour du nom de l'amenity."""
        new_name = {"name": "Jacuzzi"}
        self.amenity.update(new_name)
        self.assertEqual(self.amenity.name, new_name["name"])

    def test_invalid_name_length_too_short(self):
        """Test la création d'un amenity avec un nom trop court."""
        with self.assertRaises(ValueError):
            Amenity("")  # Nom trop court

    def test_invalid_name_length_too_long(self):
        """Test la création d'un amenity avec un nom trop long."""
        with self.assertRaises(ValueError):
            Amenity("A" * 51)  # Nom trop long


if __name__ == "__main__":
    unittest.main()