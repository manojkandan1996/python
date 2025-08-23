import tkinter as tk
from tkinter import messagebox

# Functions
def submit_feedback():
    """Validate and submit the feedback."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_text.get("1.0", tk.END).strip()
    
    if not name or not email or not feedback:
        message_label.config(text="All fields are required!", fg="red")
    else:
        message_label.config(text=f"Thank you, {name}, for your feedback!", fg="green")
        # Here you can add code to save feedback to a file or database
        print(f"Name: {name}\nEmail: {email}\nFeedback: {feedback}\n{'-'*30}")

def reset_form():
    """Clear all input fields."""
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)
    message_label.config(text="")

# Main Window
root = tk.Tk()
root.title("Feedback Collector")
root.geometry("400x400")
root.resizable(False, False)


# Frame for form
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
name_entry.grid(row=0, column=1, pady=5)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
email_entry.grid(row=1, column=1, pady=5)

# Feedback (Text widget) with Scrollbar
tk.Label(form_frame, text="Feedback:", font=("Arial", 12)).grid(row=2, column=0, sticky="nw", pady=5)
feedback_text = tk.Text(form_frame, width=30, height=8, font=("Arial", 12))
feedback_text.grid(row=2, column=1, pady=5)

scrollbar = tk.Scrollbar(form_frame, command=feedback_text.yview)
scrollbar.grid(row=2, column=2, sticky='ns', pady=5)
feedback_text.config(yscrollcommand=scrollbar.set)

# Submit and Reset Buttons
submit_button = tk.Button(form_frame, text="Submit", width=12, command=submit_feedback)
submit_button.grid(row=3, column=0, pady=15)

reset_button = tk.Button(form_frame, text="Reset", width=12, command=reset_form)
reset_button.grid(row=3, column=1, pady=15)

# Message Label
message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.pack(pady=5)

root.mainloop()
