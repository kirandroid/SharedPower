#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import hashlib
import ftplib

class LoginRegister:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1020x680+160+10")
        self.window.resizable(0, 0)
        bg_img = PhotoImage(file="img//Login.png")
        bg_label = Label(self.window, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.Login_UI()
        self.window.mainloop()

    def Login_UI(self):
        global UID_Entry, Pass_Entry

        UID_Entry = Entry(self.window)
        UID_Entry.insert(0, "UserID")
        UID_Entry.config(bd=0)
        UID_Entry.place(x=370, y=347, relwidth=0.27, relheight=0.05)

        Pass_Entry = Entry(self.window, show="*")
        Pass_Entry.insert(0, "Password")
        Pass_Entry.config(bd=0)
        Pass_Entry.place(x=370, y=433, relwidth=0.27, relheight=0.05)

        Login_Button_Img = PhotoImage(file="img//login_button.png")

        Login_Button = Button(self.window, image = Login_Button_Img, command=self.login)
        Login_Button.config(bd=0)
        Login_Button.place(x=460, y=480)

        Login_Button.image = Login_Button_Img

        register_label = Label(self.window, text="Click Here!")
        register_label.place(x=575, y=600)
        register_label.bind('<Button-1>', LoginRegister.Register_UI)


    def Register_UI(self):
        global register_name, \
            register_userid, \
            register_password, \
            register_DOB, \
            register_citizenshipno, \
            register_gender

        self.Register_win = tk.Toplevel()
        self.Register_win.geometry("1020x680+160+10")
        self.Register_win.resizable(0, 0)
        bg_img = PhotoImage(file="img//register.png")
        bg_label = Label(self.Register_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        register_name = Entry(self.Register_win)
        register_name.insert(0, "Full Name")
        register_name.config(bd=0)
        register_name.place(x=600, y=145, relwidth=0.34, relheight=0.05)

        register_userid = Entry(self.Register_win)
        register_userid.insert(0, "UserID")
        register_userid.config(bd=0)
        register_userid.place(x=600, y=210, relwidth=0.34, relheight=0.05)

        register_password = Entry(self.Register_win, show = "*")
        register_password.insert(0, "Password")
        register_password.config(bd=0)
        register_password.place(x=600, y=280, relwidth=0.34, relheight=0.05)

        register_DOB = Entry(self.Register_win)
        register_DOB.insert(0, "Date of Birth")
        register_DOB.config(bd=0)
        register_DOB.place(x=600, y=350, relwidth=0.34, relheight=0.05)

        register_citizenshipno = Entry(self.Register_win)
        register_citizenshipno.insert(0, "CitizenShip Number")
        register_citizenshipno.config(bd = 0)
        register_citizenshipno.place(x=600, y=420, relwidth=0.34, relheight=0.05)

        Register_Button_Img = PhotoImage(file="img//register_button.png")

        Register_Button = Button(self.Register_win, image=Register_Button_Img)
        Register_Button.config(bd=0)
        Register_Button.place(x=615, y=590)
        Register_Button.bind('<Button-1>',LoginRegister.register)

        Register_Button.image = Register_Button_Img

        self.Register_win.mainloop()

        # Label(self.window, text="Gender").grid(row=5, column=2)
        # self.register_gender = Entry(self.window)
        # self.register_gender.grid(row=5, column=3)
        #
        # self.register_button = Button(self.window, text="Register", command=self.register)
        # self.register_button.grid(row=6, column=3)

    @staticmethod
    def register(event):
        open_db = json.load(open("database.txt"))  # Loads the json file as dictionary
        profile = [{"Name": register_name.get(),
                    "UserID": register_userid.get(),
                    "Pass": hashlib.sha1(register_password.get().encode()).hexdigest(),
                    # The password from the password entry box is encoded with SHA1 in "Pass" value
                    "DOB": register_DOB.get(),
                    "CNo": register_citizenshipno.get(),
                    # "Gender": register_gender.get(),
                    "Own_Tools": {},
                    "Hired_Tools": {}
                    }]
        open_db[register_userid.get()] = profile  # Assigning the userid from entry box as a key
        try:
            json.dump(open_db, open("database.txt",
                                    'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file

            connect = ftplib.FTP_TLS('files.000webhost.com', 'sharedpower', 'kiranpradhan')
            ftplib.FTP_TLS.cwd(connect, "public_html")  # changes the path to public_html
            file_db = open("database.txt", 'rb')
            connect.storbinary('STOR database.txt', file_db)
            file_db.close()
            connect.quit()

            messagebox.showinfo("Registration", "Registration Successful!")
        except:
            messagebox.showinfo("Registration", "Registration Failed!")


    def login(self):
        global LoggedIn_user
        open_db = json.load(open("database.txt"))  # Loads the json file as dictionary
        hashed_pass = hashlib.sha1(Pass_Entry.get().encode()).hexdigest()  # The password from the login section gets converted to SHA1

        try:
            if UID_Entry.get() == open_db[UID_Entry.get()][0]["UserID"] and hashed_pass == open_db[UID_Entry.get()][0]["Pass"]:  # if the userid entered is equal to the userid in the database and the SHA1 converted password is equal to the database password
                messagebox.showinfo("Login", "Login Successful!")
                LoggedIn_user = open_db[UID_Entry.get()][0]["UserID"]
                self.window.destroy()
                Home().HomeScreen()
            else:
                messagebox.showinfo("Login", "The Password you entered is incorrect!")
        except KeyError:
            messagebox.showinfo("Login", "The UserID you’ve entered doesn’t match any account. Please register first! ")


class Home:
    def __init__(self):
        self.home_win = Tk()
        self.home_win.geometry("1020x680+160+10")
        self.home_win.resizable(0, 0)
        bg_img = PhotoImage(file="img//Home.png")
        bg_label = Label(self.home_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.HomeScreen()

        self.home_win.mainloop()

    def HomeScreen(self):
        global search_Entry, Searched_Item_Name, Searched_Item_Price, Searched_Item_Condition

        # Profile_Button_Img = PhotoImage(file="img//profile_button.png")
        # Profile_Button = Button(self.home_win, image=Profile_Button_Img)
        # Profile_Button.config(bd=0)
        # Profile_Button.place(x=40, y=188)
        # Profile_Button.bind('<Button-1>', Profile)
        #
        # Profile_Button.image = Profile_Button_Img

        self.profile_button = Button(self.home_win, text="Profile", command=Profile)
        self.profile_button.place(x=40, y=188)

        search_Entry = Entry(self.home_win)
        search_Entry.config(bd=0)
        search_Entry.place(x=200, y=188, relwidth=0.44, relheight=0.06)

        Search_Button_Img = PhotoImage(file="img//search_button.png")

        Search_Button = Button(self.home_win, image=Search_Button_Img)
        Search_Button.config(bd=0)
        Search_Button.place(x=900, y=188)
        Search_Button.bind('<Button-1>', Home.search)

        Search_Button.image = Search_Button_Img

        Searched_Item_Name = Label(self.home_win)
        Searched_Item_Name.place(x = 180, y = 350)

        Searched_Item_Price = Label(self.home_win)
        Searched_Item_Price.place(x = 500, y = 350)

        Searched_Item_Condition = Label(self.home_win)
        Searched_Item_Condition.place(x = 800, y = 350)


    def search(self):
        global count
        self.open_searchdb = json.load(open("searchdb.txt"))
        count = 0
        for k in self.open_searchdb.keys():
            if self.open_searchdb[k][0]["Name"] == search_Entry.get():
                Searched_Item_Name.config(text=self.open_searchdb[k][0]["Name"])
                Searched_Item_Price.config(text=self.open_searchdb[k][0]["Price"])
                Searched_Item_Condition.config(text=self.open_searchdb[k][0]["Condition"])
                count += 1
                break
        else:
            messagebox.showinfo("Search", "Sorry Item not found!")

class Profile:
    def __init__(self):
        self.profile_win = tk.Toplevel()
        self.profile_win.geometry("1020x680+160+10")
        self.profile_win.resizable(0, 0)
        bg_img = PhotoImage(file="img//User-Profile.png")
        bg_label = Label(self.profile_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ProfileScreen()
        self.profile_win.mainloop()

    def ProfileScreen(self):
        open_db = json.load(open("database.txt"))

        Profile_Name = Label(self.profile_win, text=open_db[LoggedIn_user][0]["Name"])
        Profile_Name.place(x = 150, y = 265)

        Profile_UserID = Label(self.profile_win, text=open_db[LoggedIn_user][0]["UserID"])
        Profile_UserID.place(x = 150, y = 320)

        Profile_DOB = Label(self.profile_win, text=open_db[LoggedIn_user][0]["DOB"])
        Profile_DOB.place(x = 250, y = 375)

        Profile_Gender = Label(self.profile_win, text=open_db[LoggedIn_user][0]["Gender"])
        Profile_Gender.place(x=150, y=430)

        Profile_CNo = Label(self.profile_win, text=open_db[LoggedIn_user][0]["CNo"])
        Profile_CNo.place(x = 300, y = 485)

        Add_Tool_Img = PhotoImage(file="img//AddTool.png")

        Add_Tool_Button = Button(self.profile_win, image=Add_Tool_Img)
        Add_Tool_Button.config(bd=0)
        Add_Tool_Button.place(x=655, y=600)
        Add_Tool_Button.bind('<Button-1>', Profile.Add_Tools)

        Add_Tool_Button.image = Add_Tool_Img

        Added_Tool_Name = Label(self.profile_win, text=open_db[LoggedIn_user][0]['Own_Tools']["Name"])
        Added_Tool_Name.place(x=200, y = 100)

    def Add_Tools(self):
        global Tools_name_entry, Tools_price_entry, Tools_condition_entry
        self.Add_Tools_win = tk.Toplevel()
        self.Add_Tools_win.geometry("1020x680+160+10")
        self.Add_Tools_win.resizable(0, 0)
        bg_img = PhotoImage(file="img//Add_Tool_Screen.png")
        bg_label = Label(self.Add_Tools_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        Tools_name_entry = Entry(self.Add_Tools_win)
        Tools_name_entry.config(bd=0)
        Tools_name_entry.place(x=470, y=240, relwidth=0.44, relheight=0.06)

        Tools_price_entry = Entry(self.Add_Tools_win)
        Tools_price_entry.config(bd=0)
        Tools_price_entry.place(x=470, y=325, relwidth=0.44, relheight=0.06)

        Tools_condition_entry = Entry(self.Add_Tools_win)
        Tools_condition_entry.config(bd=0)
        Tools_condition_entry.place(x=470, y=410, relwidth=0.44, relheight=0.06)

        Add_Tool_Img = PhotoImage(file="img//AddTool.png")

        Add_Tool_Button = Button(self.Add_Tools_win, image=Add_Tool_Img)
        Add_Tool_Button.config(bd=0)
        Add_Tool_Button.place(x=580, y=550)
        Add_Tool_Button.bind('<Button-1>', Profile.Add_Tools_db)

        Add_Tool_Button.image = Add_Tool_Img

        self.Add_Tools_win.mainloop()


    def Add_Tools_db(self):
        open_db = json.load(open("database.txt"))
        added_tools = [{"Name": Tools_name_entry.get(),
                        "Price": Tools_price_entry.get(),
                        "Condition": Tools_condition_entry.get()
                      }]
        add_to_logged_user = open_db[LoggedIn_user][0]['Own_Tools']

        add_to_logged_user[Tools_name_entry.get()] = added_tools

        try:
            json.dump(open_db, open("database.txt",'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file

            connect = ftplib.FTP_TLS('files.000webhost.com','sharedpower','kiranpradhan')
            ftplib.FTP_TLS.cwd(connect, "public_html") #changes the path to public_html
            file_db = open("database.txt", 'rb')
            connect.storbinary('STOR database.txt', file_db)
            file_db.close()
            connect.quit()

            messagebox.showinfo("Add Tools", "Tool Successfully Added!")
        except:
            messagebox.showinfo("Add Tools", "Tools Add Failed!")






s = LoginRegister()
