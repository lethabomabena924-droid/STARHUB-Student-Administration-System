# ==========================================
# STARHUB
# Student Registration
# students.py
# ==========================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class StudentForm:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("⭐ STARHUB - Register Student")

        self.window.geometry("500x620")

        self.window.configure(bg="white")

        # -------------------------------
        # TITLE
        # -------------------------------

        tk.Label(
            self.window,
            text="Register New Student",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#D4AF37"
        ).pack(pady=20)

        # -------------------------------
        # FIRST NAME
        # -------------------------------

        tk.Label(
            self.window,
            text="First Name",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.first_name = tk.Entry(
            self.window,
            width=40
        )

        self.first_name.pack(pady=5)

        # -------------------------------
        # LAST NAME
        # -------------------------------

        tk.Label(
            self.window,
            text="Last Name",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.last_name = tk.Entry(
            self.window,
            width=40
        )

        self.last_name.pack(pady=5)

        # -------------------------------
        # PHONE
        # -------------------------------

        tk.Label(
            self.window,
            text="Phone Number",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.phone = tk.Entry(
            self.window,
            width=40
        )

        self.phone.pack(pady=5)

        # -------------------------------
        # EMAIL
        # -------------------------------

        tk.Label(
            self.window,
            text="Email Address",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.email = tk.Entry(
            self.window,
            width=40
        )

        self.email.pack(pady=5)

        # -------------------------------
        # COURSE
        # -------------------------------

        tk.Label(
            self.window,
            text="Course",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.course = ttk.Combobox(

            self.window,

            width=37,

            state="readonly",

            values=[

                "Acting",
                "Dance",
                "Music",
                "Photography",
                "Graphic Design",
                "Film Production",
                "Fashion Design",
                "Vocal Performance"

            ]
        )

        self.course.current(0)

        self.course.pack(pady=5)

        # -------------------------------
        # STATUS
        # -------------------------------

        tk.Label(
            self.window,
            text="Application Status",
            bg="white"
        ).pack(anchor="w", padx=40)

        self.status = ttk.Combobox(

            self.window,

            width=37,

            state="readonly",

            values=[

                "New",
                "Contacted",
                "Registered",
                "Rejected"

            ]
        )

        self.status.current(0)

        self.status.pack(pady=5)

        # -------------------------------
        # SAVE BUTTON
        # -------------------------------

        tk.Button(

            self.window,

            text="💾 Save Student",

            bg="#D4AF37",

            fg="black",

            font=("Segoe UI",11,"bold"),

            command=self.save_student

        ).pack(pady=25)

    # ==========================================

    def save_student(self):

        if self.first_name.get() == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter the first name."
            )

            return

        if self.last_name.get() == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter the last name."
            )

            return

        connection = sqlite3.connect(
            "sqca_database.db"
        )

        cursor = connection.cursor()

        cursor.execute("""

        INSERT INTO students(

        first_name,

        last_name,

        phone,

        email,

        course,

        status

        )

        VALUES(?,?,?,?,?,?)

        """,(

        self.first_name.get(),

        self.last_name.get(),

        self.phone.get(),

        self.email.get(),

        self.course.get(),

        self.status.get()

        ))

        connection.commit()

        connection.close()

        messagebox.showinfo(

            "Success",

            "Student registered successfully."

        )

        self.window.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    StudentForm()

    root.mainloop()