CREATE DATABASE Library_Management;

-- creating tables

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(75) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    phone VARCHAR(14) NOT NULL
);

CREATE TABLE books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(150) NOT NULL,
	author VARCHAR(150) NOT NULL,
	availability VARCHAR(40) DEFAULT "available for loan"
);

CREATE TABLE borrowed_books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (user_name, email, phone)
VALUES ('Rick Sanchez', 'Wubba@lubba.com', '555-456-1234'),
('Morty Smith', 'ahjeez@gmail.com', '555-123-4567'),
('Summer Smith', 'sofawine@yahoo.com', '555-132-9876'),
('Bird Person', 'squawk@acorns.com', '555-234-6543');

INSERT INTO books (title, author)
VALUES ('The Hobbit', 'J. R. R. Tolkien'),
('The Shining', 'Steven King'),
('The Catcher in the Rye', 'J.D. Salinger'),
('Shantaram', 'Gregory David Roberts'),
('The Alchemist', 'Paulo Coelho'),
('The Great Gatsby', 'F. Scott Fitzgerald'),
('The Da Vinci Code', 'Dan Brown'),
('Into The Wild', 'Jon Krakauer');

SELECT * FROM users;
SELECT * FROM books;