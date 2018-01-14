from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import hashlib


def Login_UI():
    global UID_Entry, Pass_Entry
    Label(window, text="UserID").grid(row=0, column=0)
    Label(window, text="Password").grid(row=1, column=0)

    UID_Entry = Entry(window)
    UID_Entry.insert(0, "UserID")
    UID_Entry.grid(row=0, column=1)
    UID_Entry.bind("<Button-1>", clear_entry)  # When left mouse button is clicked "clear_entry" function is called

    Pass_Entry = Entry(window, show='*')
    Pass_Entry.grid(row=1, column=1)

    Login_Button = Button(window, text="Login", command=login)
    Login_Button.grid(row=2, column=1)


def Register_UI():
    global register_name, \
        register_userid, \
        register_password, \
        register_dob, \
        register_citizenshipno, \
        register_gender, \
        insertPic_button, \
        Profile_pic_label, \
        inserted_pic

    Label(window, text="Name").grid(row=0, column=2)
    register_name = Entry(window)
    register_name.grid(row=0, column=3)

    Label(window, text="UserID").grid(row=1, column=2)
    register_userid = Entry(window)
    register_userid.grid(row=1, column=3)

    Label(window, text="Password").grid(row=2, column=2)
    register_password = Entry(window, show='*')
    register_password.grid(row=2, column=3)

    Label(window, text="Date of Birth").grid(row=3, column=2)
    register_dob = Entry(window)
    register_dob.grid(row=3, column=3)

    Label(window, text="Citizenship No.").grid(row=4, column=2)
    register_citizenshipno = Entry(window)
    register_citizenshipno.grid(row=4, column=3)

    Label(window, text="Gender").grid(row=5, column=2)
    register_gender = Entry(window)
    register_gender.grid(row=5, column=3)

    register_button = Button(window, text="Register", command=register)
    register_button.grid(row=6, column=3)


def register():
    open_db = json.load(open("database.txt"))  # Loads the json file as dictionary
    profile = [{"Name": register_name.get(),
                "UserID": register_userid.get(),
                "Pass": hashlib.sha1(register_password.get().encode()).hexdigest(),
                # The password from the password entry box is encoded with SHA1 in "Pass" value
                "DOB": register_dob.get(),
                "CNo": register_citizenshipno.get(),
                "Gender": register_gender.get()}]
    open_db[register_userid.get()] = profile  # Assigning the userid from entry box as a key
    try:
        json.dump(open_db, open("database.txt",'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file
        messagebox.showinfo("Registration", "Registration Successful!")
    except:
        messagebox.showinfo("Registration", "Registration Failed!")


def login():
    open_db = json.load(open("database.txt"))  # Loads the json file as dictionary
    hashed_pass = hashlib.sha1(
        Pass_Entry.get().encode()).hexdigest()  # The password from the login section gets converted to SHA1

    if UID_Entry.get() == open_db[UID_Entry.get()][0]["UserID"] and hashed_pass == open_db[UID_Entry.get()][0]["Pass"]:  # if the userid entered is equal to the userid in the database and the SHA1 converted password is equal to the database password
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showinfo("Login", "Login Failed!")


def clear_entry(event):  # This function is used to erase the content in the userID entry box in login section
    UID_Entry.delete(0, tk.END)


window = Tk()

Login_UI()
Register_UI()

window.mainloop()
