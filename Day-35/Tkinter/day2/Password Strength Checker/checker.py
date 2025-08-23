import tkinter as tk
import re

# Function to check password strength
def check_strength(event=None):
    password = password_entry.get()
    strength = "Weak"
    color = "red"
    
    if len(password) >= 8:
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) \
           and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            strength = "Strong"
            color = "green"
        elif re.search(r'[A-Z]', password) or re.search(r'[0-9]', password):
            strength = "Moderate"
            color = "orange"
    strength_label.config(text=f"Strength: {strength}", fg=color)
    root.title(f"Password Strength Checker - {strength}")

# Function to clear the form
def clear_password():
    password_entry.delete(0, tk.END)
    strength_label.config(text="")
    root.title("Password Strength Checker")

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# Top Frame for grouping
top_frame = tk.Frame(root, padx=20, pady=20)
top_frame.pack(pady=10)

# Password Entry
tk.Label(top_frame, text="Enter Password:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
password_entry = tk.Entry(top_frame, show="*", font=("Arial", 12), width=25)
password_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry.bind("<KeyRelease>", check_strength)

# Strength Label
strength_label = tk.Label(top_frame, text="", font=("Arial", 12))
strength_label.grid(row=1, column=0, columnspan=2, pady=5)

# Buttons
submit_button = tk.Button(top_frame, text="Submit", width=12, command=lambda: print("Password Submitted"))
submit_button.grid(row=2, column=0, pady=15)

clear_button = tk.Button(top_frame, text="Clear", width=12, command=clear_password)
clear_button.grid(row=2, column=1, pady=15)

root.mainloop()
