from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review
from app.models.place import Place

class HBnBFacade:
    """Represent a facade."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Override __new__ to control instance creation (Singleton)."""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        print(f"Looking for user with ID {user_id}, found: {user}")
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        print(email)
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        return self.user_repo.update(user_id, user_data)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)

    def create_place(self, place_data):
        # Suppression des vérifications de `owner_id`
        if place_data['price'] < 0:
            raise ValueError("Price must be a non-negative float")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        
        # Création du lieu sans vérification de `owner_id`
        place = Place(**place_data)
        self.place_repo.add(place)
        return place
    

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        owner = self.user_repo.get(place.owner)
        amenities = [self.amenity_repo.get(amenity_id) for amenity_id in place.amenities]
        place.owner = owner
        place.amenities = amenities
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        if 'price' in place_data and place_data['price'] < 0:
            raise ValueError("Price must be a non-negative float")
        if 'latitude' in place_data and not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if 'longitude' in place_data and not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        for key, value in place_data.items():
            setattr(place, key, value)
        self.place_repo.update(place_id, place)
        return place

    def create_review(self, review_data):
         try:
            # Récupérer le place_id et le owner_id des données de l'avis
            place_id = review_data.get('place_id')
            owner_id = review_data.get('owner_id')

            if not owner_id:
              raise ValueError("owner_id is needed")
            if not place_id:
              raise ValueError("place_id is needed")
            
             # Vérifier l'existence du lieu (Place) associé
            place = self.place_repo.get(place_id)
            if not place:
                raise ValueError(f"place {place_id} does not exist")
            
            # Vérifier l'existence de l'utilisateur (Owner) associé
            user = self.user_repo.get(owner_id)
            if not user:
                raise ValueError(f"owner {owner_id} does not exist")
            
            # Créer l'avis et l'ajouter au depot
            review = Review(**review_data)

            self.review_repo.add(review)

            # Ajouter l'avis au lieu et mettre à jour le lieu dans le dépôt
            place.reviews.append(review)

            # Retourner l'avis sous forme de dictionnaire
            return review
         
         except (ValueError, TypeError) as e:
              raise ValueError(f"error when creating review : {str(e)}")
         except Exception as e:
              raise RuntimeError(f"error when creating review : {str(e)}")


    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute('place', place_id)

    def update_review(self, review_id, review_data):
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
