Project Requirements
In this project, you will integrate a MySQL database with Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in database integration, SQL, and Python.

Integration with the "Library Management System" Project from Module 4 (OOP):

For this project, you will build upon the foundation laid in "Module 4: Python Object-Oriented Programming (OOP)." The object-oriented structure and classes you developed in that module will serve as the core framework for the Library Management System. 

Enhanced User Interface (UI) and Menu:

Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
Welcome to the Library Management System with Database Integration!
****
Main Menu:
1. Book Operations
2. User Operations
3. Quit
 Book Operations:
Book Operations:
1. Add a new book 
2. Borrow a book 
3. Return a book
4. Search for a book
5. Display all books
 User Operations:
User Operations:
1. Add a new user
2. View user details
3. Display all users


Database Integration with MySQL:

Integrate a MySQL database into the Library Management System to store and retrieve data related to books, and users
Design and create the necessary database tables to represent these entities. 
Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and scalability of your Library Management System.
Data Definition Language Scripts:

Create the necessary database tables for the Library Management System. For instance:
Books Table:

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    availability BOOLEAN DEFAULT 1
);
(For the BOOLEAN data type, the values can be  0 for False or 1 for True)

Users Table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
);
Borrowed Books Table:
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
(Borrow date and return date are optional.)

Database Connection:

Establish a connection to the MySQL database using the mysql-connector-python library.
Create a database cursor to execute SQL queries.
Functions for Data Manipulation:

Create functions for adding new books, and users to the database.
 Implement functions for borrowing books
Implement functions for returning books

Develop functions for searching books by title.
Define functions for displaying all books, all users.
Implement functions for user registration and viewing user details.
User Interface Functions:

Create a user-friendly command-line interface (CLI) with clear menu options.
Implement functions to handle user interactions using the input() function.
Validate user input using regular expressions (regex) to ensure proper formatting.
Error Handling:

Use try, except, else, and finally blocks to manage errors gracefully.
Handle exceptions related to database operations, input validation, and other potential issues.
Provide informative error messages to guide users.
Clean Code Principles:

Use meaningful variable and function names that convey their purpose.
Write clear comments and docstrings to explain the functionality of functions and classes.
Follow PEP 8 style guidelines for code formatting and structure.
Ensure proper indentation and spacing for readability.
Modular Design:

Organize code into separate modules to promote modularity and maintainability.
Create distinct modules for database operations, user interactions, error handling, and core functionalities.
GitHub Repository:

Create a GitHub repository for your project and commit code regularly.
Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
Include a link to your GitHub repository in your project documentation.


💡 Note: You can reuse the clean code and functions developed in the "Module 4: Python Object-Oriented Programming (OOP)" project to maintain consistency and reduce redundancy. Emphasize the importance of code reusability and modular design to make it easier to integrate the database functionality into their existing project.
