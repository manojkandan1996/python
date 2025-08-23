import tkinter as tk
from tkinter import messagebox

# Functions
def login():
    """Validate username and password."""
    user = username_entry.get().strip()
    pwd = password_entry.get().strip()
    
    if not user or not pwd:
        error_label.config(text="Please enter both username and password", fg="red")
    else:
        error_label.config(text="")
        # Simulate login success
        show_welcome(user)

def clear():
    """Clear all entry fields and error messages."""
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    error_label.config(text="")

def show_welcome(user):
    """Display welcome message in a new frame."""
    login_frame.pack_forget()  # Hide login frame
    
    welcome_frame.pack(pady=20)
    welcome_label.config(text=f"Welcome, {user}!")

# Main Window
root = tk.Tk()
root.title("User Login")
root.geometry("350x250")
root.resizable(False, False)


root.iconbitmap("icon.ico") 


# Login Frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Username
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 12))
username_label.pack(anchor="w", padx=20)
username_entry = tk.Entry(login_frame, font=("Arial", 12))
username_entry.pack(padx=20, pady=5, fill="x")

# Password
password_label = tk.Label(login_frame, text="Password:", font=("Arial", 12))
password_label.pack(anchor="w", padx=20)
password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")
password_entry.pack(padx=20, pady=5, fill="x")

# Error message label
error_label = tk.Label(login_frame, text="", font=("Arial", 10))
error_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(login_frame)
button_frame.pack(pady=10)

login_button = tk.Button(button_frame, text="Login", width=10, command=login)
login_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Clear", width=10, command=clear)
clear_button.pack(side="left", padx=5)

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_label = tk.Label(welcome_frame, text="", font=("Arial", 16), fg="green")
welcome_label.pack()

root.mainloop()
