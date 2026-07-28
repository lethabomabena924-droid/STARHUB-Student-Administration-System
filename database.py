# ==========================================
# SQCA Student Administration System
# database.py
# ==========================================

import sqlite3


def create_database():
    """
    Creates the database and students table
    if it does not already exist.
    """

    connection = sqlite3.connect("sqca_database.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            course TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

def get_dashboard_statistics():

    connection = sqlite3.connect("sqca_database.db")

    cursor = connection.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # New Applications
    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE status='New'"
    )
    new_applications = cursor.fetchone()[0]

    # Registered Students
    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE status='Registered'"
    )
    registered_students = cursor.fetchone()[0]

    connection.close()

    return (
        total_students,
        new_applications,
        registered_students
    )


# ==========================================
# RECENT APPLICATIONS
# ==========================================

def get_recent_applications(limit=5):

    connection = sqlite3.connect("sqca_database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            first_name,
            last_name,
            course,
            status
        FROM students
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    students = cursor.fetchall()

    connection.close()

    return students


# ==========================================
# GET ALL STUDENTS
# ==========================================


def get_all_students():

    connection = sqlite3.connect("sqca_database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            first_name,
            last_name,
            phone,
            email,
            course,
            status
        FROM students
        ORDER BY id DESC
    """)
    students = cursor.fetchall()

    connection.close()

    return students
# ==========================================
# SEARCH STUDENTS
# ==========================================

def search_students(search_text):

    connection = sqlite3.connect("sqca_database.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            first_name,
            last_name,
            phone,
            email,
            course,
            status
        FROM students
        WHERE
            first_name LIKE ?
            OR last_name LIKE ?
            OR course LIKE ?
        ORDER BY id DESC
    """, (
        f"%{search_text}%",
        f"%{search_text}%",
        f"%{search_text}%"
    ))

    students = cursor.fetchall()

    connection.close()

    return students

# ==========================================
# RUN FILE
# ==========================================

if __name__ == "__main__":

    create_database()

    print("✅ Database created successfully!")