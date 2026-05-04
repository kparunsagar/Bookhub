
CREATE DATABASE bookhub;
USE bookhub;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    category_id INT,
    price DECIMAL(10,2)
);

INSERT INTO categories (name) VALUES 
('Technology'), ('Fiction'), ('Self-Help');

INSERT INTO books (title, author, category_id, price) VALUES
('Python Basics', 'John Doe', 1, 299),
('Atomic Habits', 'James Clear', 3, 499);
