import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "ANIKA"
VALID_PASSWORD = "Anika@123"

def logic():
    username = username_entry.get()
    password = password_entry.grt()

    if username == VALID_USERNAME and password == VALID_USERNAME:
        messagebox.showinfo("Login successful...", f"wellcome {username}")
    else:
        messagebox.showinfo("Invalid pass and id")

root = tk.Tk()
root.title("Login Application")
root.geometry("400x200")

tk.Label(root, text="username: ").grid(row=0, column=0, padx=10, pady=10, sticky='w')
username_entry = tk.Entry(root, width=25)
username_entry.grid(row=0,column=1)

tk.Label(root, text="password: ").grid(row=1, column=0, padx=10, pady=10, sticky='w')
password_entry = tk.Entry(root, width=25, show='*')
password_entry.grid(row=1,column=1)

login_button = tk.Button(root, text="login", )
login_button.grid(row=2, column=1, pady=20, wodth=25, command=login)

root.mainloop()




