-- Prépare MySQL pour le projet

-- Création de la base de données de développement
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Création de l'utilisateur de développement
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Attribution des privilèges à l'utilisateur de développement
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;

-- Utiliser la base de données de développement
USE hbnb_dev_db;

-- Création des tables de la base de données de développement
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS amenities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    user_id VARCHAR(60) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    number_rooms INT NOT NULL,
    number_bathrooms INT NOT NULL,
    max_guest INT NOT NULL,
    price_by_night FLOAT NOT NULL,
    latitude FLOAT(10, 6) NOT NULL,
    longitude FLOAT(10, 6) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    text TEXT NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

-- Création de la base de données de test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Création de l'utilisateur de test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Attribution des privilèges à l'utilisateur de test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;

-- Utiliser la base de données de test
USE hbnb_test_db;

-- Création des tables de la base de données de test
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS amenities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    user_id VARCHAR(60) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    number_rooms INT NOT NULL,
    number_bathrooms INT NOT NULL,
    max_guest INT NOT NULL,
    price_by_night FLOAT NOT NULL,
    latitude FLOAT(10, 6) NOT NULL,
    longitude FLOAT(10, 6) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    text TEXT NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);