# ==========================================
# STARHUB
# Student Administration Dashboard
# dashboard.py
# ==========================================

import tkinter as tk
from datetime import datetime
import random

from database import (
    get_dashboard_statistics,
    get_recent_applications
)

from students import StudentForm
from record import StudentRecords
from reports import Reports


class Dashboard:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title(
            "STARHUB - Student Administration Portal"
        )

        self.window.geometry(
            "1200x700"
        )

        self.window.configure(
            bg="#F4F4F4"
        )


        (
            self.total_students,
            self.new_applications,
            self.registered_students

        ) = get_dashboard_statistics()



        # =====================
        # SIDEBAR
        # =====================

        sidebar = tk.Frame(
            self.window,
            bg="#111111",
            width=250
        )

        sidebar.pack(
            side="left",
            fill="y"
        )


        tk.Label(
            sidebar,
            text="⭐ STARHUB",
            font=("Segoe UI",22,"bold"),
            fg="#D4AF37",
            bg="#111111"
        ).pack(
            pady=25
        )


        tk.Label(
            sidebar,
            text="Star Quality\nCreative Arts College",
            fg="white",
            bg="#111111",
            font=("Segoe UI",10)
        ).pack()



        tk.Frame(
            sidebar,
            bg="#D4AF37",
            height=2
        ).pack(
            fill="x",
            padx=20,
            pady=20
        )



        self.button(
            sidebar,
            "🏠 Dashboard"
        )


        self.button(
            sidebar,
            "➕ Register Student",
            self.open_students
        )


        self.button(
            sidebar,
            "📋 Student Records",
            self.open_records
        )


        self.button(
            sidebar,
            "📊 Reports",
            self.open_reports
        )



        # =====================
        # MAIN
        # =====================

        main = tk.Frame(
            self.window,
            bg="#F4F4F4"
        )

        main.pack(
            expand=True,
            fill="both"
        )


        tk.Label(
            main,
            text="👋 Welcome Administrator",
            font=("Segoe UI",20,"bold"),
            bg="#F4F4F4"
        ).pack(
            anchor="w",
            padx=30,
            pady=20
        )



        date = datetime.now().strftime(
            "%A, %d %B %Y"
        )


        tk.Label(
            main,
            text=date,
            bg="#F4F4F4"
        ).pack(
            anchor="w",
            padx=30
        )



        messages = [

            "⭐ Today's applicants could be tomorrow's stars.",
            "🎭 Creativity starts with opportunity.",
            "🎬 Building future creative professionals."

        ]


        tk.Label(
            main,
            text=random.choice(messages),
            bg="#F4F4F4",
            font=("Segoe UI",12,"italic")
        ).pack(
            padx=30,
            pady=20
        )



        cards=tk.Frame(
            main,
            bg="#F4F4F4"
        )

        cards.pack(
            padx=30
        )


        self.card(
            cards,
            "👨‍🎓 Total Students",
            self.total_students
        )


        self.card(
            cards,
            "🆕 Applications",
            self.new_applications
        )


        self.card(
            cards,
            "✅ Registered",
            self.registered_students
        )



    # =====================
    # BUTTON
    # =====================

    def button(
        self,
        parent,
        text,
        command=None
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            bg="#111111",
            fg="white",
            bd=0,
            anchor="w",
            padx=20,
            pady=12
        ).pack(
            fill="x"
        )



    # =====================
    # CARD
    # =====================

    def card(
        self,
        parent,
        title,
        number
    ):

        box=tk.Frame(
            parent,
            bg="white",
            width=220,
            height=120
        )

        box.pack(
            side="left",
            padx=10
        )

        box.pack_propagate(False)


        tk.Label(
            box,
            text=title,
            bg="white",
            font=("Segoe UI",11,"bold")
        ).pack(
            pady=15
        )


        tk.Label(
            box,
            text=str(number),
            fg="#D4AF37",
            bg="white",
            font=("Segoe UI",25,"bold")
        ).pack()



    # =====================
    # OPEN WINDOWS
    # =====================

    def open_students(self):

        StudentForm()



    def open_records(self):

        StudentRecords()



    def open_reports(self):

        Reports()



    def run(self):

        self.window.mainloop()



if __name__ == "__main__":

    app = Dashboard()

    app.run()
    