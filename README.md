# Student Contact Manager

## Description
This is a simple Python application that uses SQLite to manage student records.  
It allows users to **add, view, update, and delete** student information using a command-line interface (CLI).

## Table Fields
The `students` table contains the following fields:
- `id` (Primary Key, auto-increment)  
- `name` (TEXT, required)  
- `email` (TEXT, required)  
- `phone` (TEXT, optional)  
- `course` (TEXT, optional)

## How to Run
1. Open the `main.py` file in Pydroid 3 (or any Python 3 IDE).  
2. Run the program.  
3. Use the menu to perform actions:
   - `1` → Add Student  
   - `2` → View Students  
   - `3` → Update Student  
   - `4` → Delete Student  
   - `5` → Exit  

> Tip: On some phone keyboards, the number keys may appear as symbols (`@`, `#`, `$`). The program automatically handles this.

## CRUD Features Implemented
- **Create:** Add new student with validated name and email.  
- **Read:** View all student records in a clear format.  
- **Update:** Modify student name and email by ID.  
- **Delete:** Remove a student record by ID.  

## Sample Output
