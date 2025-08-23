import tkinter as tk
from tkinter import messagebox

# Function to handle registration
def register(event=None):
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    if not name or not email:
        result_label.config(text="Please fill in all fields!", fg="red")
    else:
        result_label.config(text=f"Thank you {name} for registering!", fg="green")
        # Optionally, print to console
        print(f"Registered: Name={name}, Email={email}")

# Function to clear the form
def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    result_label.config(text="")

# Main Window
root = tk.Tk()
root.title("Event Registration")
root.geometry("400x300")
root.resizable(False, False)


# Frame for grouping fields
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(pady=20)

# Name Label and Entry
tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
name_entry.grid(row=0, column=1, pady=5)

# Email Label and Entry
tk.Label(form_frame, text="Email:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
email_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
email_entry.grid(row=1, column=1, pady=5)

# Register Button
register_button = tk.Button(form_frame, text="Register", width=15, command=register)
register_button.grid(row=2, column=0, columnspan=2, pady=15)

# Bind <Return> key to register
root.bind("<Return>", register)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", width=12, command=clear_fields)
clear_button.pack()

root.mainloop()
