# student-management-system-python
student management system with basic CRUD functionalities.

# Student Management System

A simple Python-based Student Management System that allows users to manage student records through a menu-driven interface.

## Features

* Add new students
* View all students
* Search for a student by name
* Update student marks
* Delete student records
* Persistent data storage using JSON
* Input validation using exception handling
* Menu-driven user interface

## Technologies Used

* Python
* JSON File Handling

## Project Structure

```text
student-management-system/
│
├── main.py
├── students.json
└── README.md
```

## How It Works

The program loads existing student data from a JSON file when it starts.

Users can perform the following operations:

1. Add Student
2. View Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit

Any changes made to student records are automatically saved to the JSON file.

## Sample Student Record

```json
{
    "name": "Aryan",
    "age": 22,
    "marks": 90
}
```

## Concepts Implemented

* Variables and Data Types
* Conditional Statements
* Loops
* Functions
* Lists and Dictionaries
* File Handling
* JSON Operations
* Exception Handling
* CRUD Operations

## Learning Outcome

This project was built while learning Python fundamentals and demonstrates the implementation of a complete CRUD (Create, Read, Update, Delete) application with persistent storage.

## Future Improvements

* Object-Oriented Programming (OOP) implementation
* Grade calculation system
* Student ID generation
* Sorting and filtering records
* Graphical User Interface (GUI)
* Database integration

## Author

Aryan
