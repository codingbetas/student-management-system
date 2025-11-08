# 🎓 Student Management System (Python + SQLite)

A simple **menu-driven Python application** to manage student records using an **SQLite database**.  
You can easily add, view, search, update, and delete student details — all through a command-line interface.

---

## 🧠 Features

- Add a new student (name, age, course, grade)
- View all students in a formatted table
- Search student by ID
- Update existing student information
- Delete a student record
- Automatically creates a local SQLite database (`students.db`)

---

## 🗂️ Project Structure

Student-Management-System/
│
├── app.py # Main menu program
├── database.py # Database connection and table creation
├── functions.py # All CRUD functions (insert, view, search, update, delete)
├── students.db # SQLite database (auto-created)
└── pycache/ # Auto-generated cache folder


---

## 🛠️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   
2 . Run the main program
python app.py

💾 Requirements

Python 3.x (SQLite comes built-in)
