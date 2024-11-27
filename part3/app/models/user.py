from .base import BaseModel
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, owner_id=None, admin=False):
        super().__init__()
        self.owner_id = owner_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.admin = admin
        self.places = []
        self.password = None
        self.hash_password(password)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value is None:
            raise ValueError("You must enter a first name")

        if len(value) > 50:
            raise ValueError("First name must not exceed 50 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None:
            raise ValueError("You must enter a last name")

        if len(value) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ValueError("You must enter an email")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid input data")
        self._email = value

    def add_place(self, place):
        self.places.append(place)

    def hash_password(self, password):
        if not password:
            raise ValueError("Password cannot be empty")
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        if not self.password:
            raise ValueError("Password hash is missing.")
        return bcrypt.check_password_hash(self.password, password)
