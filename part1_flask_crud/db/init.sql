-- Create database
CREATE DATABASE validata;
GO

-- Switch to database
USE validata;
GO

-- Create banks table
CREATE TABLE banks (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- (seed, increment)
    name NVARCHAR(255) NOT NULL,
    location NVARCHAR(255) NOT NULL
);
GO
