# 1. Créer un utilisateur
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "Regular",
    "last_name": "User",
    "email": "user@example.com",
    "password": "userpassword123",
    "admin": false
}'

# 2. Se connecter et recevoir le token
curl -X POST "http://127.0.0.1:5000/api/v1/auth/login" -H "Content-Type: application/json" -d '{
    "email": "user@example.com",
    "password": "userpassword123"
}'

# 3. Créer un lieu (place)
# Remplace "owner_id" par l'ID de l'utilisateur et $TOKEN par le token 
curl -X POST "http://127.0.0.1:5000/api/v1/places/" -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{
    "title": "Cozy Apartment",
    "description": "A nice place to stay",
    "price": 100.0,
    "latitude": 37.7749,
    "longitude": -122.4194,
    "owner_id": "$ID",
    "amenities": ["wifi", "pool"]
}'