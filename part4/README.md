# HBnB Project: A Clone of ABnB

## Overview of the setup

The project is organize in the following structure :
```bash
hbnb/
├── app/
│ ├── __init__.py
│ ├── api/
│ │ ├── __init__.py
│ │ ├── v1/
│ │ ├── __init__.py
│ │ ├── users.py
│ │ ├── places.py
│ │ ├── reviews.py
│ │ ├── amenities.py
│ ├── models/
│ │ ├── __init__.py
│ │ ├── user.py
│ │ ├── place.py
│ │ ├── review.py
│ │ ├── amenity.py
│ ├── services/
│ │ ├── __init__.py
│ │ ├── facade.py
│ ├── persistence/
│ ├── __init__.py
│ ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

## Purpose of each directories and files:

- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the API endpoints, organized by version (v1/).
- The `models/` subdirectory contains the business logic classes (e.g., user.py, place.py).
- The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` contains a brief overview of the project.

## Installation instructions

#### Create an environment

```macOS/Linux
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

```Windows
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

#### Activate the environment

```macOS/Linux
$ . .venv/bin/activate
```

```Windows
> .venv\Scripts\activate
```

#### Install all dependancies

```
pip install -r requirements.txt
```

#### Test the Initial setup

```
python run.py
```

#### Entity-Relationship (ER) diagrams

##### Actual Relationships

```mermaid
    erDiagram
    User {
        string id
        string first_name
        string last_name
        string email
        string password
        boolean is_admin
        datetime created_at
        datetime updated_at
    }

    Place {
        string id
        string title
        text description
        float price
        float latitude
        float longitude
        string owner_id
        datetime created_at
        datetime updated_at
    }

    Review {
        string id
        text text
        float rating
        string user_id
        string place_id
        datetime created_at
        datetime updated_at
    }

    Amenity {
        string id
        string name
        datetime created_at
        datetime updated_at
    }

    Place_Amenity {
        string place_id
        string amenity_id
    }

    User ||--o{ Place : "owns"
    User ||--o{ Review : "writes"

    Place ||--o{ Review : "receives"
    Place ||--o{ Place_Amenity : "has"

    Amenity ||--o{ Place_Amenity : "belongs to"
```

##### Possible future Relationships

```mermaid
    erDiagram
    User {
        string id
        string first_name
        string last_name
        string email
        string password
        boolean is_admin
        datetime created_at
        datetime updated_at
        string phone_number
        string profile_picture
    }

    Place {
        string id
        string title
        text description
        float price
        float latitude
        float longitude
        string owner_id
        int max_guests
        time check_in_time
        time check_out_time
        boolean instant_booking
        datetime created_at
        datetime updated_at
    }

    Review {
        string id
        text text
        float rating
        string user_id
        string place_id
        datetime created_a
        datetime updated_at
        boolean is_verified
    }

    Amenity {
        string id
        string name
        string icon
        string category
        datetime created_a
        datetime updated_at    
    }

    Place_Amenity {
        string place_id
        string amenity_id
    }

    Booking {
        string id
        string user_id
        string place_id
        datetime check_in
        datetime check_out
        float total_price
        enum status
        int guests_count
        datetime created_at
        boolean is_cancelled
        text cancellation_reason
    }

    Payment {
        string id
        string booking_id
        float amount
        enum status
        string transaction_id
        datetime payment_date
        string payment_method
    }

    Availability {
        string id
        string place_id
        date start_date
        date end_date
        boolean is_blocked
        float special_price
    }

    Message {
        string id
        string sender_id
        string receiver_id
        string booking_id
        text content
        datetime sent_at
        boolean is_read
    }

    User ||--o{ Place : "owns"
    User ||--o{ Review : "writes"
    User ||--o{ Booking : "makes"
    User ||--o{ Message : "sends/receives"

    Place ||--o{ Review : "receives"
    Place ||--o{ Booking : "has"
    Place ||--o{ Availability : "has"
    Place ||--o{ Place_Amenity : "has"

    Amenity ||--o{ Place_Amenity : "belongs to"
    Booking ||--o{ Payment : "has"
    Booking ||--o{ Message : "has"
```
