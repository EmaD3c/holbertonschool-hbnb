# Testing Process Documentation: User, Amenity, Place, and Review Endpoints

## Postman

- This tests was perform with Postman.
- Click on the link to se the collection of tests : [Endpoints testing].(https://hbnb11.postman.co/workspace/HBnB-Workspace~39992131-109f-4104-8883-4b824d56cc88/collection/38801940-38979a27-2e72-40ac-9c32-cdad033cd95b?action=share&creator=38801940)

### **User**

#### **GET: List all users (no users initially)**

- **Endpoint:** `GET /api/v1/users/`
- **Description:** Retrieve a list of all users. Initially, the list will be empty since no users exist yet.
- **Expected Output:** Empty array `[]` with status code `200 OK`.

#### **POST: Create user1**

- **Endpoint:** `POST /api/v1/users/`
- **Description:** Create a new user (`user1`) with first name, last name, and email.
- **Input Data:**

```json
{
  "first_name": "user1",
  "last_name": "user",
  "email": "user1.user@gmail.com"
}
```

- **Expected Output:** User created with a unique `id` and the provided details. Status code `201 Created`.

#### **POST: Create user2 and strore his id**

- **Endpoint:** `POST /api/v1/users/`
- **Description:** Create another user (`user2`) and store their ID for future requests.
- **Input Data:**

```json
{
  "first_name": "user2",
  "last_name": "user",
  "email": "user2.user@gmail.com"
}
```

- **Expected Output:** User created with a unique `id` and the provided details. Status code `201 Created`.

#### **POST: Create user3 and store his ID**

- **Endpoint:** `POST /api/v1/users/`
- **Description:** Create a third user (`user3`) and store their ID for future requests.
- **Input Data:**

```json
{
  "first_name": "user3",
  "last_name": "user",
  "email": "user3.user@gmail.com"
}
```

- **Expected Output:** User created with a unique `id`. Status code `201 Created`.

#### **POST: Create user3 again (duplicate user)**

- **Endpoint:** `POST /api/v1/users/`
- **Description:** Attempt to create a duplicate user (`user3`). This should trigger an error because the user already exists.
- **Expected Output:** Error message with status code `400 Bad Request`.

#### **GET: List all users**

- **Endpoint:** `GET /api/v1/users/`
- **Description:** Retrieve a list of all created users, including `user1`, `user2`, and `user3`.
- **Expected Output:** A list of users with their respective `id`, `first_name`, `last_name`, and `email`. Status code `200 OK`.

#### **GET: User by ID**

- **Endpoint:** `GET /api/v1/users/{{userId}}`
- **Description:** Retrieve the details of a specific user by their `id`.
- **Expected Output:** The user's details including `id`, `first_name`, `last_name`, `email`, `places`, and `reviews`. Status code `200 OK`.

#### **GET: User by invalid ID**

- **Endpoint:** `GET /api/v1/users/invalid_id`
- **Description:** Attempt to retrieve a user by an invalid `id`.
- **Expected Output:** Error message stating "User not found" with status code `404 Not Found`.

#### **PUT: Update user**

- **Endpoint:** `PUT /api/v1/users/{{userId}}`
- **Description:** Update the user's email address to a new one.
- **Input Data:**

```json
{
  "first_name": "user1",
  "last_name": "user",
  "email": "user1.user@orange.fr"
}
```

- **Expected Output:** Updated user details. Status code `200 OK`.

#### **GET: User by ID after update**

- **Endpoint:** `GET /api/v1/users/{{userId}}`
- **Description:** Retrieve the details of a specific user by their `id`.
- **Expected Output:** The user's details including `id`, `first_name`, `last_name`, `email`, `places`, and `reviews`. Status code `200 OK`.

#### **PUT: Update user with invalid ID**

- **Endpoint:** `PUT /api/v1/users/invalid_id`
- **Description:** Attempt to update a user using an invalid `id`.
- **Expected Output:** Error message stating "User not found" with status code `404 Not Found`.

---

### **Amenity**

#### **POST: Create amenity**

- **Endpoint:** `POST /api/v1/amenities/`
- **Description:** Create a new amenity with a name (e.g., `WiFi`).
- **Input Data:**

```json
{
  "name": "WiFi"
}
```

- **Expected Output:** Amenity created with a unique `id` and the name. Status code `201 Created`.

#### **GET: List all amenities**

- **Endpoint:** `GET /api/v1/amenities/`
- **Description:** Retrieve a list of all amenities.
- **Expected Output:** A list of amenities with their `id` and `name`. Status code `200 OK`.

#### **GET: Amenity by ID**

- **Endpoint:** `GET /api/v1/amenities/{{amenityId}}`
- **Description:** Retrieve an amenity's details by its `id`.
- **Expected Output:** The amenity's details including `id` and `name`. Status code `200 OK`.

#### **GET: Amenity by ID**

- **Endpoint:** `GET /api/v1/amenities/{{amenityId}}`
- **Description:** Attempt to update an amenity using an invalid `id`.
- **Expected Output:** The amenity's details including `id` and `name`. Status code `200 OK`.

#### **PUT: Update amenity**

- **Endpoint:** `PUT /api/v1/amenities/{{amenityId}}`
- **Description:** Update an amenity's name.
- **Input Data:**

```json
{
  "name": "Piscine"
}
```

- **Expected Output:** Updated amenity details. Status code `200 OK`.

#### **GET: Amenity by ID after update**

- **Endpoint:** `GET /api/v1/amenities/{{amenityId}}`
- **Description:** Retrieve an amenity's details by its `id`.
- **Expected Output:** The amenity's details including `id` and `name`. Status code `200 OK`.

---

### **Place**

#### **POST: Create place with out-of-range latitude**

- **Endpoint:** `POST /api/v1/places/`
- **Description:** Create a new place (e.g., a villa) with out-of-range latitude.
- **Input Data:**

```json
{
  "title": "Invalid Place",
  "price": 500,
  "description": "Invalid latitude test",
  "latitude": 100, // Out of range
  "longitude": 1.4,
  "owner_id": "{{userId}}"
}
```

#### **POST: Create place with out-of-range longitude**

- **Endpoint:** `POST /api/v1/places/`
- **Description:** Create a new place (e.g., a villa) with out-of-range latitude.
- **Input Data:**

```json
{
  "title": "Invalid Place",
  "price": 500,
  "description": "Invalid longitude test",
  "latitude": 39.02,
  "longitude": 200, // Out of range
  "owner_id": "{{userId}}"
}
```

#### **POST: Create place**

- **Endpoint:** `POST /api/v1/places/`
- **Description:** Create a new place (e.g., a villa) with details like `title`, `price`, `latitude`, `longitude`, `owner_id`, and `description`.
- **Input Data:**

```json
{
  "title": "Villa",
  "price": 500,
  "description": "Une magnifique villa dans une magnifique ville",
  "latitude": 39.02,
  "longitude": 1.4,
  "owner_id": "{{userId}}"
}
```

- **Expected Output:** Place created with a unique `id` and the provided details. Status code `201 Created`.

#### **GET: List all places**

- **Endpoint:** `GET /api/v1/places/`
- **Description:** Retrieve a list of all created places.
- **Expected Output:** A list of places with their details. Status code `200 OK`.

#### **GET: Place by ID**

- **Endpoint:** `GET /api/v1/places/{{placeId}}`
- **Description:** Retrieve a place's details by its `id`.
- **Expected Output:** The place's details including `id`, `title`, `price`, `owner`, and `description`. Status code `200 OK`.

#### **GET: Place by ID with invalid id**

- **Endpoint:** `GET /api/v1/places/{{placeId}}`
- **Description:** Attempt to get a place using an invalid `id`.
- **Expected Output:** The place's details including `id`, `title`, `price`, `owner`, and `description`. Status code `200 OK`.

#### **PUT: Update place**

- **Endpoint:** `PUT /api/v1/places/{{placeId}}`
- **Description:** Update the details of a place.
- **Input Data:**

```json
{
  "title": "Chateau",
  "price": 1000,
  "latitude": 15,
  "longitude": 15,
  "owner": "owner",
  "description": "Mais pourquoi louer un Chateau ???"
}
```

#### **GET: Place by ID after update**

- **Endpoint:** `GET /api/v1/places/{{placeId}}`
- **Description:** Retrieve a place's details by its `id`.
- **Expected Output:** The place's details including `id`, `title`, `price`, `owner`, and `description`. Status code `200 OK`.
- **Expected Output:** Updated place details. Status code `200 OK`.

#### **POST: Associate amenity to place**

- **Endpoint:** `POST /api/v1/places/{{placeId}}/add_amenity/{{amenityId}}`
- **Description:** Add an amenity (e.g., WiFi or Piscine) to a specific place.
- **Expected Output:** Success message confirming the association. Status code `200 OK`.

---

#### **GET: Place by ID whith amenity**

- **Endpoint:** `GET /api/v1/places/{{placeId}}`
- **Description:** Retrieve a place's details by its `id`.
- **Expected Output:** The place's details including `id`, `title`, `price`, `owner`, and `description`. Status code `200 OK`.
- **Expected Output:** Updated place details. Status code `200 OK`.

### **Review**

#### **POST: Create review with missing fields**

- **Endpoint:** `POST /api/v1/reviews/`
- **Description:** Create a new review for a place with a rating and text.
- **Input Data:**

```json
{
  "text": "",
  "rating": "5",
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

#### **POST: Create review with out-of-range rating**

- **Endpoint:** `POST /api/v1/reviews/`
- **Description:** Create a new review for a place with a rating and text.
- **Input Data:**

```json
{
  "text": "Not great.",
  "rating": "6", // Out of range
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

#### **POST: Create review**

- **Endpoint:** `POST /api/v1/reviews/`
- **Description:** Create a new review for a place with a rating and text.
- **Input Data:**

```json
{
  "text": "Magnifique endroit, je reviendrai!",
  "rating": "5",
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

#### **POST: Create review 2**

- **Endpoint:** `POST /api/v1/reviews/`
- **Description:** Create a new review for a place with a rating and text.
- **Input Data:**

```json
{
  "text": "Magnifique endroit, je reviendrai!",
  "rating": "5",
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

#### **POST: Create review 3**

- **Endpoint:** `POST /api/v1/reviews/`
- **Description:** Create a new review for a place with a rating and text.
- **Input Data:**

```json
{
  "text": "Magnifique endroit, je reviendrai!",
  "rating": "5",
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

- **Expected Output:** Review created with a unique `id` and the provided details. Status code `201 Created`.

#### **GET: List all reviews**

- **Endpoint:** `GET /api/v1/reviews/`
- **Description:** Retrieve a list of all reviews.
- **Expected Output:** A list of reviews with their details. Status code `200 OK`.

#### **GET: Review by ID**

- **Endpoint:** `GET /api/v1/reviews/{{reviewId}}`
- **Description:** Retrieve the details of a specific review by its `id`.
- **Expected Output:** The review's details including `id`, `text`, `rating`, `place_id`, and `user_id`. Status code `200 OK`.

#### **PUT: Update review**

- **Endpoint:** `PUT /api/v1/reviews/{{reviewId}}`
- **Description:** Update the review details (e.g., change the rating or review text).
- **Input Data:**

```json
{
  "text": "Un endroit correct.",
  "rating": "4",
  "place_id": "{{placeId}}",
  "user_id": "{{userId}}"
}
```

#### **GET: Place by ID after review input**

- **Endpoint:** `GET /api/v1/places/{{placeId}}`
- **Description:** Retrieve a place's details by its `id`.
- **Expected Output:** The place's details including `id`, `title`, `price`, `owner`, and `description`. Status code `200 OK`.
- **Expected Output:** Updated review details. Status code `200 OK`.

#### **DELETE: Delete review**

- **Endpoint:** `DELETE /api/v1/reviews/{{reviewId}}`
- **Description:** Delete a specific review by its `id

#### **GET: List reviews by user**

- **Endpoint:** `GET /api/v1/users/{{userId}}/reviews`
- **Description:** Retrieve a list of all created reviews by user.
- **Expected Output:** A list of reviews with their details. Status code `200 OK`.

#### **GET: List reviews by place**

- **Endpoint:** `GET /api/v1/places/{{placeId}}/reviews`
- **Description:** Retrieve a list of all created reviews by place.
- **Expected Output:** A list of reviews with their details. Status code `200 OK`.