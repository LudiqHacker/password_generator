import tkinter as tk
import random
import pyperclip
import string

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    global password
    password = "".join(random.choice(chars) for i in range(16))
    label1.config(text=f"Password: {password}", font=("Sans", 24), bg="lightblue")
    label2.config(text="", bg="#d9d9d9")
    btn_copy.config(text="Click to copy the password")

def press_to_copy():
    try:
        pyperclip.copy(password)
        label2.pack()
        label2.place(x=70, y=210)
        label2.config(text="Coppied!", bg="lightgreen")
    except NameError:
        label2.config(text="")
    
root = tk.Tk()
root.title("Password generator")
root.geometry("800x600")
btn = tk.Button(root, text="Generate a password", font=("Sans", 24), width=30, command=generate_password,)
btn.pack()
btn.place(x=120, y=10)
label1 = tk.Label(root, text="")
label1.pack(anchor="center", side="top", pady=80)
btn_copy = tk.Button(root, text="Click to copy the password", font=("Sans", 16), width=30, command=press_to_copy)
btn_copy.pack()
btn_copy.place(y=150, x= 200)
label2 = tk.Label(root, text="Coppied!", font=("Sans", 17), width=50, )
root.mainloop()
