-- Delete database
DROP DATABASE IF EXISTS db_test;

-- Create a database
CREATE DATABASE IF NOT EXISTS db_test;
USE db_test;

-- Define an user table
CREATE TABLE IF NOT EXISTS user (
  id CHAR(36) PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  is_admin BOOLEAN DEFAULT FALSE
);

-- Define a place table
CREATE TABLE IF NOT EXISTS place (
  id CHAR(36) PRIMARY KEY,
  title VARCHAR(256) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  owner_id CHAR(36) NOT NULL,
  FOREIGN KEY(owner_id) REFERENCES user(id)
    ON DELETE CASCADE
);

-- Define a review table
CREATE TABLE IF NOT EXISTS review (
  id CHAR(36) PRIMARY KEY,
  text TEXT NOT NULL,
  rating INT NOT NULL,
  user_id CHAR(36) NOT NULL,
  place_id CHAR(36) NOT NULL,
  FOREIGN KEY(user_id) REFERENCES user(id)
    ON DELETE CASCADE,    
  FOREIGN KEY(place_id) REFERENCES place(id)
    ON DELETE CASCADE,    
  CHECK(rating >= 1 AND rating <= 5)
);

-- Define a amenity table
CREATE TABLE IF NOT EXISTS amenity (
  id CHAR(36) PRIMARY KEY,
  name VARCHAR(255) UNIQUE
);

-- Define a place amenity table
CREATE TABLE IF NOT EXISTS place_amenity (
  place_id CHAR(36) NOT NULL,
  amenity_id CHAR(36) NOT NULL,
  FOREIGN KEY(place_id) REFERENCES place(id)
    ON DELETE CASCADE,    
  FOREIGN KEY(amenity_id) REFERENCES amenity(id)
    ON DELETE CASCADE,    
  PRIMARY KEY(place_id, amenity_id)
);

-- Use online tool bcrypt-generator
-- admin1234 = $2a$12$A8oSBlT0.kX85Yahlh48PumQcPtwNfHjLVtoefBK62dLlnzb5BEwK
-- Add values to user table
INSERT IGNORE INTO user VALUES(
  "36c9050e-ddd3-4c3b-9731-9f487208bbc1",
  "Admin", "HBnB", "admin@hbnb.io",
  "$2a$12$A8oSBlT0.kX85Yahlh48PumQcPtwNfHjLVtoefBK62dLlnzb5BEwK",
  TRUE);
-- Check role of user
SELECT '-----------Admin User is created(is_admin = 1 is TRUE)-------------' as ____________________;
SELECT * FROM user \G;

-- Use online tool UUID bcrypt-generator
-- UUID1: 8a6bcb29-9c09-4a7f-9150-a0614800674f
-- UUID2: 2ad65ebc-2200-4d00-a21d-372dc9d4246c
-- UUID3: b23013b2-1155-415f-be02-16228ce73992
-- Add values to amenity table
INSERT IGNORE INTO amenity (id, name) VALUES
  ("8a6bcb29-9c09-4a7f-9150-a0614800674f", "WIFI"),
  ("2ad65ebc-2200-4d00-a21d-372dc9d4246c", "Swimming Pool"),
  ("b23013b2-1155-415f-be02-16228ce73992", "Air Conditioning");
SELECT '------------------Amenites are created.-----------------' as ____________________;
SELECT * FROM amenity \G;

-- Detail of all tables with all constraints and all relationships
SELECT '------------------USER CONTRAINTS AND RELATIONSHIPS------------------' as ____________________;
DESCRIBE user \G;
SELECT '------------------PLACE CONTRAINTS AND RELATIONSHIPS------------------' as ____________________;
DESCRIBE place \G;
SELECT '------------------REVIEW CONTRAINTS AND RELATIONSHIPS------------------' as ____________________;
DESCRIBE review \G;
SELECT '------------------AMENITY CONTRAINTS AND RELATIONSHIPS------------------' as ____________________;
DESCRIBE amenity \G;
SELECT '------------------PLACE_AMENITY CONTRAINTS AND RELATIONSHIPS------------------' as ____________________;
DESCRIBE place_amenity \G;

-- SELECT, INSERT and UPDATE Place
-- Insert Place
INSERT INTO place VALUES
  ("96890fd8-b2ee-470e-847e-e98dd44674b8", "Villa", "Un endroit chaleureux", 999.99, 0.787, 1.767, "36c9050e-ddd3-4c3b-9731-9f487208bbc1");
SELECT '-------------------------Create place-----------------------------------' as ____________________;
SELECT * FROM place \G;
-- Update Place
UPDATE place SET description = "Venez découvrir un endroit magnifique" WHERE id = "96890fd8-b2ee-470e-847e-e98dd44674b8"; 
SELECT '-------------------------Update place-----------------------------------' as ____________________;
SELECT description FROM place \G;

-- SELECT and UPDATE Amenity
-- Update Amenity
UPDATE amenity SET name = "Jaccuzi" WHERE id = "b23013b2-1155-415f-be02-16228ce73992"; 
SELECT '-------------------------Update amenity---------------------------------' as ____________________;
SELECT name FROM amenity WHERE id="b23013b2-1155-415f-be02-16228ce73992"\G;

-- SELECT, INSERT and UPDATE Review 
-- Insert Review
INSERT INTO review VALUES
  ("c47ade16-4f37-411f-9457-24c10add5921", "Je recommande vivement cette villa !!!", 5, "36c9050e-ddd3-4c3b-9731-9f487208bbc1", "96890fd8-b2ee-470e-847e-e98dd44674b8");
SELECT '-------------------------Insert review----------------------------------' as ____________________;
SELECT * FROM review \G;
-- Update Review
UPDATE review SET rating = 4 WHERE id = "c47ade16-4f37-411f-9457-24c10add5921"; 
SELECT '-------------------------Update Review----------------------------------' as ____________________;
SELECT rating FROM review WHERE id="c47ade16-4f37-411f-9457-24c10add5921" \G;

-- SELECT, INSERT and UPDATE PlaceAmenity
-- Insert new association
INSERT INTO place_amenity VALUES
  ("96890fd8-b2ee-470e-847e-e98dd44674b8", "8a6bcb29-9c09-4a7f-9150-a0614800674f");
SELECT '-------------------------Insert PlaceAmenity(Register an amenity in a place)----------------------------' as ____________________;
SELECT place_id, amenity_id FROM place_amenity \G;
SELECT '-------------------------The primary key has been created----------------------------' as ____________________;
SHOW KEYS FROM place_amenity WHERE Key_name = "PRIMARY";

-- CRUD User
-- Update User
UPDATE user SET last_name = "updated_last_name" WHERE id = "36c9050e-ddd3-4c3b-9731-9f487208bbc1";
SELECT '-------------------------Update User------------------------------------' as ____________________;
SELECT last_name FROM user WHERE id = "36c9050e-ddd3-4c3b-9731-9f487208bbc1" \G;

-- Delete all entries of tables
DELETE FROM user WHERE id = "36c9050e-ddd3-4c3b-9731-9f487208bbc1";
SELECT '---Delete the user deletes all reviews and locations relating to the user.---' as ____________________;
SELECT * FROM user \G;
SELECT * FROM review \G;
SELECT * FROM place \G;
SELECT '---No data was returned. The user, their location and their opinion have been deleted.---' as ____________________;

-- Check the amenities
SELECT '---Amenities have not been removed.---' as ____________________;
SELECT * FROM amenity \G;
-- Delete amenities
DELETE FROM amenity;

-- Last check of all datas
SELECT '---All data has been deleted.---' as ____________________;
SELECT * FROM user \G;
SELECT * FROM review \G;
SELECT * FROM place \G;
SELECT * FROM amenity \G;