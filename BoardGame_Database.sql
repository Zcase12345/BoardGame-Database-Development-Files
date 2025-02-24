-- Create The Database If It Does Not Exist
CREATE DATABASE IF NOT EXISTS BoardGameProject;
USE BoardGameProject;

-- Create The User Table If It Does Not Exist
CREATE TABLE IF NOT EXISTS User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL
);

-- Create The BoardGame Table If It Does Not Exist
CREATE TABLE IF NOT EXISTS BoardGame (
    GameID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description TEXT,
    Image VARCHAR(255)
);

-- Create The BoardGameLog Table If It Does Not Exist
CREATE TABLE IF NOT EXISTS BoardGameLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (UserID)
        REFERENCES User (UserID),
    UserID INT,
    GameID INT,
    Rating DECIMAL(2 , 1 ),
    Players INT,
    Description TEXT,
    Image VARCHAR(255),
    FOREIGN KEY (GameID)
        REFERENCES BoardGame (GameID)
);