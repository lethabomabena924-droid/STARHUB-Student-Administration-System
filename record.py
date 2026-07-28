# ==========================================
# STARHUB
# Student Records
# records.py
# ==========================================

import tkinter as tk
from tkinter import ttk
import sqlite3


class StudentRecords:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("STARHUB - Student Records")

        self.window.geometry("1000x550")

        self.window.configure(bg="white")

        # -------------------------
        # Heading
        # -------------------------

        title = tk.Label(
            self.window,
            text="📋 Student Records",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#D4AF37"
        )

        title.pack(pady=10)

        # -------------------------
        # Search
        # -------------------------

        search_frame = tk.Frame(self.window, bg="white")
        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Search:",
            bg="white",
            font=("Arial", 11)
        ).pack(side="left")

        self.search_entry = tk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.pack(side="left", padx=10)

        tk.Button(
            search_frame,
            text="Search",
            bg="#D4AF37",
            command=self.search_students
        ).pack(side="left")

        tk.Button(
            search_frame,
            text="Show All",
            command=self.load_students
        ).pack(side="left", padx=10)

        # -------------------------
        # Table
        # -------------------------

        columns = (
            "ID",
            "First Name",
            "Last Name",
            "Phone",
            "Email",
            "Course",
            "Status"
        )

        self.tree = ttk.Treeview(
            self.window,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.tree.heading(column, text=column)

            self.tree.column(column, width=130)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.load_students()

    # ======================================

    def load_students(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

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

        for student in students:

            self.tree.insert(
                "",
                tk.END,
                values=student
            )

    # ======================================

    def search_students(self):

        search = self.search_entry.get()

        for item in self.tree.get_children():
            self.tree.delete(item)

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
            "%" + search + "%",
            "%" + search + "%",
            "%" + search + "%"
        ))

        students = cursor.fetchall()

        connection.close()

        for student in students:

            self.tree.insert(
                "",
                tk.END,
                values=student)


# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    StudentRecords()

    root.mainloop()