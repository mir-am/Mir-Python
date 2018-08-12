-- Creates a table for storing user information

CREATE TABLE user_info (

    id INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    city VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    registerDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);
