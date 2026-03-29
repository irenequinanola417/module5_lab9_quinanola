import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        course TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_student():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ")
    course = input("Enter course: ")

    if name == "":
        print("❌ Name cannot be empty!")
        return
    if "@" not in email:
        print("❌ Invalid email!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, phone, course) VALUES (?, ?, ?, ?)",
                   (name, email, phone, course))
    conn.commit()
    conn.close()
    print("✅ Added successfully!")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No records found.")
    else:
        for r in rows:
            print(r)

    conn.close()

def update_student():
    id = input("Enter ID to update: ")
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    if not cursor.fetchone():
        print("❌ Not found")
        conn.close()
        return

    name = input("New name: ")
    email = input("New email: ")

    cursor.execute("UPDATE students SET name=?, email=? WHERE id=?", (name, email, id))
    conn.commit()
    conn.close()
    print("✅ Updated!")

def delete_student():
    id = input("Enter ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    if not cursor.fetchone():
        print("❌ Not found")
        conn.close()
        return

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print("✅ Deleted!")

def menu():
    create_table()
    while True:
        print("\n1 Add\n2 View\n3 Update\n4 Delete\n5 Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

menu()