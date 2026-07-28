# ==========================================
# STARHUB
# Settings Page
# settings.py
# ==========================================

import tkinter as tk


class Settings:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("STARHUB - Settings")

        self.window.geometry("500x400")

        self.window.configure(bg="white")


        # Title

        tk.Label(
            self.window,
            text="⚙ System Settings",
            font=("Segoe UI",20,"bold"),
            fg="#D4AF37",
            bg="white"
        ).pack(pady=20)


        # Information box

        info = """

STARHUB Student Administration System

College:
Star Quality Creative Arts College

Version:
1.0

Database:
SQLite Database Connected

System Status:
Running Successfully

        """


        tk.Label(
            self.window,
            text=info,
            font=("Segoe UI",12),
            bg="white",
            justify="left"
        ).pack(pady=20)


        tk.Button(
            self.window,
            text="Close",
            bg="#D4AF37",
            font=("Segoe UI",11,"bold"),
            command=self.window.destroy
        ).pack(pady=20)



# Test file

if __name__ == "__main__":

    root = tk.Tk()

    root.withdraw()

    Settings()

    root.mainloop()