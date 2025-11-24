# Student Marks Management System

## Overview
This project is a Python console application made to manage student marks for three subjects. It allows the user to add, update, delete, search, and view student details. The program also calculates total marks, percentage, and grade automatically.


## Features
- Add a new student (roll number, name, and marks for three subjects)
- Automatically calculate total marks, percentage, and grade
- Update marks for an existing student
- Delete a student record
- View all students in a clean list
- Search a student using roll number
- Class statistics:
  - Number of students
  - Average percentage
  - Topper’s name and percentage

## Project Structure
Student Marks Management Project/
├── main.py – Main menu and program control
├── operations.py – Add, update, delete functions
├── reports.py – Viewing, searching, statistics
└── data.py – In-memory list storing student records

## How to Run the Project
1. Install Python 3 on your system.
2. Download or clone this repository.
3. Open the folder in VS Code or any editor.
4. Run the program using:
   python main.py

## Technologies Used
- Python 3
- Lists and dictionaries
- Basic modular programming

## Testing Instructions
- Add multiple students with different marks
- Update marks for a student
- Search using valid and invalid roll numbers
- Delete a student and check the updated output
- Try wrong inputs such as letters instead of numbers
- View class statistics after entering a few students

## Future Enhancements
- Add file or database storage for permanent data
- Allow more than three subjects
- Add a GUI using Tkinter or a web app
- Add login or admin authentication
