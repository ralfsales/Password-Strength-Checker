import tkinter as tk
import re

# Create the main function to handle the password testing
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one digit."
    if not re.search(r'[@#$%^&+=]', password):
        return "Weak: Password should contain at least one special character."
    
    common_patterns = ['password', '12345', 'qwerty']
    for pattern in common_patterns:
        if pattern in password.lower():
            return "Weak: Password contains common patterns."
    
    return "Strong: Password is secure."

# Create the main window for the application
root = tk.Tk()
# Give it a lable/title
root.title("🔏 Password Strength Checker")
# Set window size to 800px width and 300px height
root.geometry("800x300")

# A label to display instructions
label = tk.Label(root, text="Enter a password to check its strength:")
label.pack(pady=10)

# Frame to hold the password entry and the "view" button
frame = tk.Frame(root)
frame.pack(pady=5)

# An entry widget for password input
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.pack(side="left", padx=5)

# A button to toggle visibility of the password
eye_button = tk.Button(frame, text="🙂 Show", command=lambda: toggle_password_visibility(password_entry, eye_button))
eye_button.pack(side="left")

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Function to handle the button click event
def check_strength():
    password = password_entry.get()
    result = check_password_strength(password)
    result_label.config(text=result)

# Function to toggle password visibility
def toggle_password_visibility(entry, button):
    if entry.cget("show") == "*":
        entry.config(show="")
        button.config(text="🙈 Hide")  # Change button text to "Hide"
    else:
        entry.config(show="*")
        button.config(text="🙂 Show")  # Change button text to "Show"

# A button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=20)

# Run the application
root.mainloop()
