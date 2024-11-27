import unittest
from app.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up some valid data for testing."""
        self.valid_first_name = "John"
        self.valid_last_name = "Doe"
        self.valid_email = "john.doe@gmail.com"

    def test_first_name_not_empty(self):
        """Test that first_name is not empty."""
        with self.assertRaises(ValueError):
            User("", self.valid_last_name, self.valid_email)

    def test_last_name_not_empty(self):
        """Test that last_name is not empty."""
        with self.assertRaises(ValueError):
            User(self.valid_first_name, "", self.valid_email)

    def test_email_not_empty(self):
        """Test that email is not empty."""
        with self.assertRaises(ValueError):
            User(self.valid_first_name, self.valid_last_name, "")

    def test_valid_email_format(self):
        """Test that email is in a valid format."""
        invalid_email = "john.doe@invalid"
        with self.assertRaises(ValueError):
            User(self.valid_first_name, self.valid_last_name, invalid_email)

    def test_valid_user_creation(self):
        """Test creating a user with valid attributes."""
        user = User(self.valid_first_name, self.valid_last_name, self.valid_email)
        self.assertEqual(user.first_name, self.valid_first_name)
        self.assertEqual(user.last_name, self.valid_last_name)
        self.assertEqual(user.email, self.valid_email)


if __name__ == "__main__":
    unittest.main()