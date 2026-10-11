import tkinter as tk
from tkinter import messagebox
import secrets
import string


# -----------------------------
# FUNCTIONS
# -----------------------------

def generate_password():
    """Create a random password."""

    try:
        length = int(length_entry.get())

    except ValueError:
        messagebox.showerror(
            "Invalid Length",
            "Please enter a whole number."
        )
        return

    if length < 8:
        messagebox.showwarning(
            "Password Too Short",
            "Please choose at least 8 characters."
        )
        return

    if length > 50:
        messagebox.showwarning(
            "Password Too Long",
            "Please choose 50 characters or fewer."
        )
        return

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_characters = letters + numbers + symbols

    password = ""

    for count in range(length):
        password += secrets.choice(all_characters)

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    status_label.config(
        text="Your new password is ready!",
        fg="#16A34A"
    )


def copy_password():
    """Copy the generated password."""

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Please generate a password first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    status_label.config(
        text="Password copied!",
        fg="#2563EB"
    )


def clear_password():
    """Clear the password and length."""

    length_entry.delete(0, tk.END)

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    status_label.config(
        text="Choose a length and generate a password.",
        fg="#6B7280"
    )

    length_entry.focus()


# -----------------------------
# MAIN WINDOW
# -----------------------------

window = tk.Tk()

window.title("Rain's Password Generator")
window.geometry("570x570")
window.resizable(False, False)
window.configure(bg="#FFF7ED")


# -----------------------------
# HEADER
# -----------------------------

header = tk.Frame(window, bg="#EA580C", height=115)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="Password Generator",
    font=("Arial", 25, "bold"),
    bg="#EA580C",
    fg="white"
)

title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    header,
    text="Create a random password with one click",
    font=("Arial", 11),
    bg="#EA580C",
    fg="#FFEDD5"
)

subtitle_label.pack()


# -----------------------------
# MAIN CARD
# -----------------------------

card = tk.Frame(
    window,
    bg="white",
    padx=40,
    pady=35,
    highlightbackground="#FED7AA",
    highlightthickness=1
)

card.pack(padx=40, pady=35, fill="both", expand=True)

length_label = tk.Label(
    card,
    text="Password Length",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#374151"
)

length_label.pack(anchor="w")

length_entry = tk.Entry(
    card,
    font=("Arial", 17),
    justify="center",
    bd=1,
    relief="solid"
)

length_entry.pack(fill="x", ipady=8, pady=(7, 8))

help_label = tk.Label(
    card,
    text="Choose a number from 8 to 50.",
    font=("Arial", 10),
    bg="white",
    fg="#6B7280"
)

help_label.pack(anchor="w", pady=(0, 18))

generate_button = tk.Button(
    card,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#EA580C",
    fg="white",
    activebackground="#C2410C",
    cursor="hand2",
    command=generate_password
)

generate_button.pack(fill="x", ipady=10)


# -----------------------------
# PASSWORD OUTPUT
# -----------------------------

password_label = tk.Label(
    card,
    text="Generated Password",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#374151"
)

password_label.pack(anchor="w", pady=(22, 7))

password_entry = tk.Entry(
    card,
    font=("Courier New", 14, "bold"),
    justify="center",
    readonlybackground="#FFF7ED",
    fg="#9A3412",
    bd=1,
    relief="solid",
    state="readonly"
)

password_entry.pack(fill="x", ipady=12)

copy_button = tk.Button(
    card,
    text="Copy Password",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    cursor="hand2",
    command=copy_password
)

copy_button.pack(fill="x", ipady=8, pady=(12, 7))

clear_button = tk.Button(
    card,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#6B7280",
    fg="white",
    activebackground="#4B5563",
    cursor="hand2",
    command=clear_password
)

clear_button.pack(fill="x", ipady=8)

status_label = tk.Label(
    card,
    text="Choose a length and generate a password.",
    font=("Arial", 10),
    bg="white",
    fg="#6B7280"
)

status_label.pack(pady=(15, 0))

length_entry.focus()

window.mainloop()