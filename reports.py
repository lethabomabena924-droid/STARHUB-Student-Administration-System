# ==========================================
# STARHUB
# Reports Dashboard
# reports.py
# ==========================================

import tkinter as tk
import sqlite3


class Reports:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title(
            "STARHUB - Reports"
        )

        self.window.geometry(
            "700x500"
        )

        self.window.configure(
            bg="white"
        )


        # Title

        tk.Label(
            self.window,
            text="📊 Student Reports",
            font=("Segoe UI",20,"bold"),
            fg="#D4AF37",
            bg="white"
        ).pack(pady=20)



        connection = sqlite3.connect(
            "sqca_database.db"
        )

        cursor = connection.cursor()



        # Total students

        cursor.execute(
            "SELECT COUNT(*) FROM students"
        )

        total = cursor.fetchone()[0]



        # Registered

        cursor.execute(
            "SELECT COUNT(*) FROM students WHERE status='Registered'"
        )

        registered = cursor.fetchone()[0]



        # New applications

        cursor.execute(
            "SELECT COUNT(*) FROM students WHERE status='New'"
        )

        new = cursor.fetchone()[0]



        connection.close()



        # Report Cards

        self.report_card(
            "👨‍🎓 Total Students",
            total
        )


        self.report_card(
            "🆕 New Applications",
            new
        )


        self.report_card(
            "✅ Registered Students",
            registered
        )



    def report_card(self,title,value):

        frame = tk.Frame(
            self.window,
            bg="#F4F4F4",
            width=400,
            height=80
        )

        frame.pack(
            pady=10
        )

        frame.pack_propagate(False)



        tk.Label(
            frame,
            text=title,
            font=("Segoe UI",12,"bold"),
            bg="#F4F4F4"
        ).pack(
            side="left",
            padx=20
        )


        tk.Label(
            frame,
            text=str(value),
            font=("Segoe UI",25,"bold"),
            fg="#D4AF37",
            bg="#F4F4F4"
        ).pack(
            side="right",
            padx=20
        )



if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    Reports()

    root.mainloop()