import tkinter as tk
from tkinter import messagebox # GUI Library
import hashlib # hash library 

# User Data Placeholder
DATA_FILE = "user_data.txt"

# Hash Password Function using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save username and hashed password into the .txt file
def save_user(username, password):
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{hash_password(password)}\n")

# Function to read the .txt file and place it into dictionary
def load_users():
    users = {} # users dict
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                username, hashed = line.split(",")
                users[username] = hashed
    return users

# Register function
def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("The input is Empty!", "Please fill the username and password!")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Register Failed", "This username is existed.")
        return
    
    save_user(username, password)
    messagebox.showinfo("Register Success.", "Successfully Registered.")

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("The input is Empty!", "Please fill the username and password!")
        return
    
    users = load_users()
    hashed_password_input = hash_password(password)

    if username in users and users[username] == hashed_password_input:
        messagebox.showinfo("Login Succeed!", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed.", "Username or Password is Wrong!")

# GUI
root = tk.Tk()
root.title("Safe Login App with Hashing")
root.geometry("300x250") # size of desktop app
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_title = tk.Label(frame, text="Safe Login App", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

tk.Label(frame, text="Username").pack()
entry_username = tk.Entry(frame)
entry_username.pack()

tk.Label(frame, text="Password").pack()
entry_password = tk.Entry(frame, show="*") # Password will shown as *
entry_password.pack()

tk.Button(frame, text="Login", command=login, width=20).pack(pady=5)
tk.Button(frame, text="Register", command=register, width=20).pack(pady=5)

root.mainloop()