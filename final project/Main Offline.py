#!/usr/bin/env python3

from tkinter import *
import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
import json
import hashlib
import ftplib
import os

class LoginRegister:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1020x680+160+10")
        self.window.title("Shared Power || Login")
        self.window.iconbitmap('img//fav.ico')
        self.window.resizable(0, 0)
        bg_img = PhotoImage(file="img//Login.png")
        bg_label = Label(self.window, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.Login_UI()
        self.window.mainloop()

    def clear_widget_login(event):
        if UID_Entry == UID_Entry.focus_get() and UID_Entry.get() == 'Enter Username':
            UID_Entry.delete(0, END)
        elif Pass_Entry == Pass_Entry.focus_get() and Pass_Entry.get() == '          ':
            Pass_Entry.delete(0, END)

    def clear_widget_register(event):
        if register_name == register_name.focus_get() and register_name.get() == "Full Name":
            register_name.delete(0, END)
        elif register_userid == register_userid.focus_get() and register_userid.get() == 'User ID':
            register_userid.delete(0, END)
        elif register_password == register_password.focus_get() and register_password.get() == '          ':
            register_password.delete(0, END)
        elif register_DOB == register_DOB.focus_get() and register_DOB.get() == 'Date of Birth':
            register_DOB.delete(0, END)
        elif register_citizenshipno == register_citizenshipno.focus_get() and register_citizenshipno.get() == 'Citizenship Number':
            register_citizenshipno.delete(0, END)

    def login_repopulate_defaults(event):
        if UID_Entry != UID_Entry.focus_get() and UID_Entry.get() == '':
            UID_Entry.insert(0, 'Enter Username')
        elif Pass_Entry != UID_Entry.focus_get() and Pass_Entry.get() == '':
            Pass_Entry.insert(0, '          ')

    def register_repopulate_defaults(event):
        if register_name != register_name.focus_get() and register_name.get() == '':
            register_name.insert(0, "Full Name")
        elif register_userid != register_userid.focus_get() and register_userid.get() == '':
            register_userid.insert(0, "User ID")
        elif register_password != register_password.focus_get() and register_password.get() == '':
            register_password.insert(0, "          ")
        elif register_DOB != register_DOB.focus_get() and register_DOB.get() == '':
            register_DOB.insert(0, "Date of Birth")
        elif register_citizenshipno != register_citizenshipno.focus_get() and register_citizenshipno.get() == '':
            register_citizenshipno.insert(0, "Citizenship Number")

    def Login_UI(self):
        global UID_Entry, Pass_Entry

        UID_Entry = Entry(self.window, font=(15))
        UID_Entry.insert(0, "Enter Username")
        UID_Entry.config(bd=0)
        UID_Entry.bind("<FocusIn>", LoginRegister.clear_widget_login)
        UID_Entry.bind("<FocusOut>", LoginRegister.login_repopulate_defaults)
        UID_Entry.place(x=370, y=347, relwidth=0.27, relheight=0.05)

        Pass_Entry = Entry(self.window, show="*", font=(15))
        Pass_Entry.insert(0, "          ")
        Pass_Entry.config(bd=0)
        Pass_Entry.bind("<FocusIn>", LoginRegister.clear_widget_login)
        Pass_Entry.bind("<FocusOut>", LoginRegister.login_repopulate_defaults)
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
            register_gender, gender_value

        self.Register_win = tk.Toplevel()
        self.Register_win.title("Shared Power || Register")
        self.Register_win.iconbitmap('img//fav.ico')
        self.Register_win.geometry("1020x680+160+10")
        self.Register_win.resizable(0, 0)
        bg_img = PhotoImage(file="img//register.png")
        bg_label = Label(self.Register_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        register_name = Entry(self.Register_win)
        register_name.insert(0, "Full Name")
        register_name.config(bd=0)
        register_name.bind("<FocusIn>", LoginRegister.clear_widget_register)
        register_name.bind("<FocusOut>", LoginRegister.register_repopulate_defaults)
        register_name.place(x=600, y=145, relwidth=0.34, relheight=0.05)

        register_userid = Entry(self.Register_win)
        register_userid.insert(0, "User ID")
        register_userid.config(bd=0)
        register_userid.bind("<FocusIn>", LoginRegister.clear_widget_register)
        register_userid.bind("<FocusOut>", LoginRegister.register_repopulate_defaults)
        register_userid.place(x=600, y=210, relwidth=0.34, relheight=0.05)

        register_password = Entry(self.Register_win, show = "*")
        register_password.insert(0, "          ")
        register_password.config(bd=0)
        register_password.bind("<FocusIn>", LoginRegister.clear_widget_register)
        register_password.bind("<FocusOut>", LoginRegister.register_repopulate_defaults)
        register_password.place(x=600, y=280, relwidth=0.34, relheight=0.05)

        register_DOB = Entry(self.Register_win)
        register_DOB.insert(0, "Date of Birth")
        register_DOB.config(bd=0)
        register_DOB.bind("<FocusIn>", LoginRegister.clear_widget_register)
        register_DOB.bind("<FocusOut>", LoginRegister.register_repopulate_defaults)
        register_DOB.place(x=600, y=350, relwidth=0.34, relheight=0.05)

        register_citizenshipno = Entry(self.Register_win)
        register_citizenshipno.insert(0, "Citizenship Number")
        register_citizenshipno.config(bd = 0)
        register_citizenshipno.bind("<FocusIn>", LoginRegister.clear_widget_register)
        register_citizenshipno.bind("<FocusOut>", LoginRegister.register_repopulate_defaults)
        register_citizenshipno.place(x=600, y=420, relwidth=0.34, relheight=0.05)

        Register_Button_Img = PhotoImage(file="img//register_button.png")

        Register_Button = Button(self.Register_win, image=Register_Button_Img)
        Register_Button.config(bd=0)
        Register_Button.place(x=615, y=590)
        Register_Button.bind('<Button-1>',LoginRegister.register)

        Register_Button.image = Register_Button_Img

        gender_value = StringVar()
        gender_value.set(' ')

        Radiobutton(self.Register_win, text="Male", variable=gender_value, value="Male", command = LoginRegister.selected_gender).place(x = 670, y = 495)
        Radiobutton(self.Register_win, text="Female", variable=gender_value, value="Female", command = LoginRegister.selected_gender).place(x = 750, y = 495)

        open_terms = Label(self.Register_win, text="terms and condition.", font=(15))
        open_terms.place(x=800, y=555)
        open_terms.bind('<Button-1>', LoginRegister.open_terms)

        self.Register_win.mainloop()

    def open_terms(self):
        os.startfile("Terms.txt")

    @staticmethod
    def selected_gender(event=None):
        global gender_selected
        gender_selected = gender_value.get()

    @staticmethod
    def register(event):
        open_db = json.load(open("database.txt"))  # Loads the json file as dictionary
        profile = [{"Name": register_name.get(),
                    "UserID": register_userid.get(),
                    "Pass": hashlib.sha1(register_password.get().encode()).hexdigest(),  # The password from the password entry box is encoded with SHA1 in "Pass" value
                    "DOB": register_DOB.get(),
                    "CNo": register_citizenshipno.get(),
                    "Gender": gender_selected,
                    "Own_Tools": {},
                    "Hired_Tools": {}
                    }]
        open_db[register_userid.get()] = profile  # Assigning the userid from entry box as a key
        try:
            json.dump(open_db, open("database.txt", 'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file

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
                Home()
            else:
                messagebox.showinfo("Login", "The Password you entered is incorrect!")
        except KeyError:
            messagebox.showinfo("Login", "The UserID you’ve entered doesn’t match any account. Please register first! ")

class Home:
    def __init__(self):
        self.home_win = Tk()
        self.home_win.geometry("1020x680+160+10")
        self.home_win.resizable(0, 0)
        self.home_win.title("Shared Power || Home")
        self.home_win.iconbitmap('img//fav.ico')
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
        # self.gr = Profile
        # Profile_Button.bind('<Button-1>', self.gr)
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

        view_all_button = Button(self.home_win, text = "View All Tools", command = self.view_all)
        view_all_button.place(x = 800, y = 100)

        Searched_Item_Name = Label(self.home_win, font=(15))
        Searched_Item_Name.place(x=200, y=350)

        Searched_Item_Price = Label(self.home_win, font=(15))
        Searched_Item_Price.place(x=500, y=350)

        Searched_Item_Condition = Label(self.home_win, font=(15))
        Searched_Item_Condition.place(x=800, y=350)

        Search_Hire_Button = Button(self.home_win, text="Hire", command= self.hire)
        Search_Hire_Button.place(x=850, y=350)


    def search(self):
        global count
        self.open_searchdb = json.load(open("searchdb.txt"))
        count = 0
        l = 0
        for k in self.open_searchdb.keys():
            if self.open_searchdb[k][0]["Name"] == search_Entry.get() or self.open_searchdb[k][0]["Name"].upper() == search_Entry.get() or self.open_searchdb[k][0]["Name"].capitalize() == search_Entry.get():
                Searched_Item_Name.config(text=self.open_searchdb[k][0]["Name"])
                Searched_Item_Price.config(text=self.open_searchdb[k][0]["Price"])
                Searched_Item_Condition.config(text=self.open_searchdb[k][0]["Condition"])
                search_hire_button = Button()
                l = 1
                count += 1
        if l!=1:
            messagebox.showinfo("Search", "Sorry Item not found!")

    def view_all(self):
        global clicked_hire, Hire_Button
        self.view_all_win = Tk()
        self.view_all_win.title("Shared Power || View All")
        self.view_all_win.iconbitmap('img//fav.ico')

        open_searchdb = json.load(open("searchdb.txt"))
        name = Label(self.view_all_win, text="Name", font=(15), bg="red", foreground="white")
        name.grid(row=0, column=0)
        price = Label(self.view_all_win, text="Price", font=(15), bg="blue", foreground="white")
        price.grid(row=0, column=1)
        Condition = Label(self.view_all_win, text="Condition", font=(15), bg="green", foreground="white")
        Condition.grid(row=0, column=2)
        Availability = Label(self.view_all_win, text="Availability", font=(15), bg="gray", foreground="white")
        Availability.grid(row=0, column=3)

        now = datetime.datetime.now()

        count = 1
        for k in open_searchdb.keys():
            diff = datetime.datetime.strptime(now.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.datetime.strptime(open_searchdb[k][0]["Time"], '%Y-%m-%d')

            if diff.days <= 42:
                Searched_Item_Name = Label(self.view_all_win, text=open_searchdb[k][0]["Name"])
                Searched_Item_Name.grid(row=count, column=0)
                Searched_Item_Price = Label(self.view_all_win, text=open_searchdb[k][0]["Price"])
                Searched_Item_Price.grid(row=count, column=1)
                Searched_Item_Condition = Label(self.view_all_win, text=open_searchdb[k][0]["Condition"])
                Searched_Item_Condition.grid(row=count, column=2)
                if open_searchdb[k][0]["Avail"]=="True" and open_searchdb[k][0]["UID"] != LoggedIn_user:
                    Searched_Item_Availability = Label(self.view_all_win, text = "Yes")
                    Searched_Item_Availability.grid(row=count, column=3)
                    Hire_Button = Button(self.view_all_win, text="Hire", command =lambda k=k: Home.hire(k))
                    Hire_Button.grid(row=count, column=4)
                elif open_searchdb[k][0]["UID"] == LoggedIn_user:
                    Searched_Item_Availability = Label(self.view_all_win, text="No")
                    Searched_Item_Availability.grid(row=count, column=3)
                    Hire_Button = Button(self.view_all_win, text="Own Tool", bg="Yellow")
                    Hire_Button.grid(row=count, column=4)
                elif open_searchdb[k][0]["Avail"]=="False":
                    Searched_Item_Availability = Label(self.view_all_win, text="No")
                    Searched_Item_Availability.grid(row=count, column=3)
                    Hire_Button = Button(self.view_all_win, text="Hired", bg = "red")
                    Hire_Button.grid(row=count, column=4)
            else:
                pass

            count += 1
        self.view_all_win.mainloop()

    def hire(k):
        now = datetime.datetime.now()
        open_db = json.load(open("database.txt"))
        open_searchdb = json.load(open("searchdb.txt"))
        hired_tools = [{"Name": open_searchdb[k][0]["Name"],
                        "Price": open_searchdb[k][0]["Price"],
                        "Condition": open_searchdb[k][0]["Condition"],
                        "Time": now.strftime("%Y-%m-%d")
                        }]
        add_to_logged_user = open_db[LoggedIn_user][0]['Hired_Tools']

        add_to_logged_user[k] = hired_tools
        try:
            json.dump(open_db, open("database.txt", 'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file
            open_searchdb[k][0]["Avail"] = not open_searchdb[k][0]["Avail"]
            update_tools = [{"Name": open_searchdb[k][0]["Name"],
                            "Price": open_searchdb[k][0]["Price"],
                            "UID": LoggedIn_user,
                            "Condition": open_searchdb[k][0]["Condition"],
                            "Avail" : str(open_searchdb[k][0]["Avail"])
                            }]
            open_searchdb[k] = update_tools
            json.dump(open_searchdb, open("searchdb.txt", 'w'))

            messagebox.showinfo("Hire Tools", "Tool Successfully Hired!")
        except:
            messagebox.showinfo("Add Tools", "Tools Hire Failed!")



class Profile():
    def __init__(self):
        self.profile_win = tk.Toplevel()
        self.profile_win.geometry("1020x680+160+10")
        self.profile_win.resizable(0, 0)
        self.profile_win.title("Shared Power || Profile")
        self.profile_win.iconbitmap('img//fav.ico')
        bg_img = PhotoImage(file="img//User-Profile.png")
        bg_label = Label(self.profile_win, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.ProfileScreen()
        self.profile_win.mainloop()

    def ProfileScreen(self):
        open_db = json.load(open("database.txt"))

        Profile_Name = Label(self.profile_win, text=open_db[LoggedIn_user][0]["Name"], font=(15), bg = "white")
        Profile_Name.place(x = 150, y = 261.5)

        Profile_UserID = Label(self.profile_win, text=open_db[LoggedIn_user][0]["UserID"], font=(15), bg = "white")
        Profile_UserID.place(x = 150, y = 321)

        Profile_DOB = Label(self.profile_win, text=open_db[LoggedIn_user][0]["DOB"], font=(15), bg = "white")
        Profile_DOB.place(x = 250, y = 375)

        Profile_Gender = Label(self.profile_win, text=open_db[LoggedIn_user][0]["Gender"], font=(15), bg = "white")
        Profile_Gender.place(x=150, y=430)

        Profile_CNo = Label(self.profile_win, text=open_db[LoggedIn_user][0]["CNo"], font=(15), bg = "white")
        Profile_CNo.place(x = 300, y = 485)

        Add_Tool_Img = PhotoImage(file="img//AddTool.png")

        Add_Tool_Button = Button(self.profile_win, image=Add_Tool_Img)
        Add_Tool_Button.config(bd=0)
        Add_Tool_Button.place(x=655, y=600)
        Add_Tool_Button.bind('<Button-1>', Profile.Add_Tools)

        Add_Tool_Button.image = Add_Tool_Img

        View_Added_Tool_Button = Button(self.profile_win, text = "View Your Added Tools", command = self.View_Added_Tool)
        View_Added_Tool_Button.place(x = 655, y = 180)

        View_Hired_Tool_Button = Button(self.profile_win, text = "View Your Hired Tools", command = self.View_Hired_Tool)
        View_Hired_Tool_Button.place(x = 655, y= 500)


    def View_Added_Tool(self):
        self.view_addedTool_win = Tk()
        self.view_addedTool_win.title("Shared Power || Added Tools")
        self.view_addedTool_win.iconbitmap('img//fav.ico')
        open_db = json.load(open("database.txt"))
        name = Label(self.view_addedTool_win, text="Name", font=(15), bg="red", foreground="white")
        name.grid(row=0, column=0)
        price = Label(self.view_addedTool_win, text="Price", font=(15), bg="blue", foreground="white")
        price.grid(row=0, column=1)
        Condition = Label(self.view_addedTool_win, text="Condition", font=(15), bg="green", foreground="white")
        Condition.grid(row=0, column=2)
        count = 1
        for k in open_db[LoggedIn_user][0]["Own_Tools"].keys():
            Searched_Item_Name = Label(self.view_addedTool_win, text=open_db[LoggedIn_user][0]["Own_Tools"][k][0]["Name"])
            Searched_Item_Name.grid(row=count, column=0)
            Searched_Item_Price = Label(self.view_addedTool_win, text=open_db[LoggedIn_user][0]["Own_Tools"][k][0]["Price"])
            Searched_Item_Price.grid(row=count, column=1)
            Searched_Item_Condition = Label(self.view_addedTool_win, text=open_db[LoggedIn_user][0]["Own_Tools"][k][0]["Condition"])
            Searched_Item_Condition.grid(row=count, column=2)
            count +=1

        self.view_addedTool_win.mainloop()

    def View_Hired_Tool(self):
        self.view_hiredTool_win = Tk()
        self.view_hiredTool_win.title("Shared Power || Hired Tools")
        self.view_hiredTool_win.iconbitmap('img//fav.ico')
        open_db = json.load(open("database.txt"))
        name = Label(self.view_hiredTool_win, text="Name", font=(15), bg="red", foreground="white")
        name.grid(row=0, column=0)
        price = Label(self.view_hiredTool_win, text="Price", font=(15), bg="blue", foreground="white")
        price.grid(row=0, column=1)
        Condition = Label(self.view_hiredTool_win, text="Condition", font=(15), bg="green", foreground="white")
        Condition.grid(row=0, column=2)
        Time = Label(self.view_hiredTool_win, text="Hired Time", font=(15), bg="Gray", foreground="white")
        Time.grid(row=0, column=3)
        count = 1
        for k in open_db[LoggedIn_user][0]["Hired_Tools"].keys():
            Searched_Item_Name = Label(self.view_hiredTool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Name"])
            Searched_Item_Name.grid(row=count, column=0)
            Searched_Item_Price = Label(self.view_hiredTool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Price"])
            Searched_Item_Price.grid(row=count, column=1)
            Searched_Item_Condition = Label(self.view_hiredTool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Condition"])
            Searched_Item_Condition.grid(row=count, column=2)
            Searched_Item_Condition = Label(self.view_hiredTool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Time"])
            Searched_Item_Condition.grid(row=count, column=3)
            Return_Button = Button(self.view_hiredTool_win, text = "Return", command =lambda k=k: Profile.return_tool(k))
            Return_Button.grid(row = count, column = 4)
            count +=1

        self.view_hiredTool_win.mainloop()

    def return_tool(k):
        return_tool_win = Tk()
        return_tool_win.title("Shared Power || Bill")
        return_tool_win.iconbitmap('img//fav.ico')
        open_db = json.load(open("database.txt"))
        now = datetime.datetime.now()


        Returned_Tool_name = Label(return_tool_win, text = open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Name"])
        Returned_Tool_name.grid(row = 0, column = 0)

        Returned_Tool_price = Label(return_tool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Price"])
        Returned_Tool_price.grid(row=1, column=0)

        Returned_Tool_time = Label(return_tool_win, text=open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Time"])
        Returned_Tool_time.grid(row=2, column=0)

        diffre = datetime.datetime.strptime(now.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.datetime.strptime(open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Time"], '%Y-%m-%d')

        if diffre.days <= 3:
            bill_without_fine = diffre.days * int(open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Price"][0])
            bill_without_fine_label = Label(return_tool_win, text=bill_without_fine)
            bill_without_fine_label.grid(row = 3, column = 0)
        else:
            more_than_three = diffre.days - 3
            bill_without_fine = 3 * int(open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Price"][0])
            bill_with_fine = more_than_three * (int(open_db[LoggedIn_user][0]["Hired_Tools"][k][0]["Price"][0])*2)
            total_bill_withfine = bill_with_fine+bill_without_fine
            bill_without_fine_label = Label(return_tool_win, text=total_bill_withfine)
            bill_without_fine_label.grid(row=3, column=0)

        return_tool_win.mainloop()

    def Add_Tools(self):
        global Tools_name_entry, Tools_price_entry, Tools_condition_entry, Tool_price_duration
        self.Add_Tools_win = tk.Toplevel()
        self.Add_Tools_win.title("Shared Power || Add Tools     ")
        self.Add_Tools_win.iconbitmap('img//fav.ico')
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

        Tool_price_duration = StringVar()
        Tool_price_duration.set(' ')

        Radiobutton(self.Add_Tools_win, text="Per day", variable=Tool_price_duration, value="Per day",
                    command=Profile.selected_tool_price_duration).place(x=280, y=325)
        Radiobutton(self.Add_Tools_win, text="Per half day", variable=Tool_price_duration, value="Per half day",
                    command=Profile.selected_tool_price_duration).place(x=380, y=325)

        self.Add_Tools_win.mainloop()



    @staticmethod
    def selected_tool_price_duration(event=None):
        global tool_price_duration_selected
        tool_price_duration_selected = Tool_price_duration.get()

    def Add_Tools_db(self):
        now = datetime.datetime.now()
        open_db = json.load(open("database.txt"))
        tool_price = Tools_price_entry.get(),tool_price_duration_selected
        # time_added = datetime.date(now.year, now.month, now.day)
        added_tools = [{"Name": Tools_name_entry.get(),
                        "Price": tool_price,
                        "UID": LoggedIn_user,
                        "Condition": Tools_condition_entry.get(),
                        "Time": now.strftime("%Y-%m-%d"),
                        "Avail": "True"
                      }]
        add_to_logged_user = open_db[LoggedIn_user][0]['Own_Tools']

        add_to_logged_user[Tools_name_entry.get()] = added_tools
        try:
            json.dump(open_db, open("database.txt",'w'))  # Saving the dictionary as json with "w" file method i.e, it overwrites the file

            messagebox.showinfo("Add Tools", "Tool Successfully Added!")
        except:
            messagebox.showinfo("Add Tools", "Tools Add Failed!")

        search_db = json.load(open("searchdb.txt"))
        count_db = json.load(open("count.txt"))
        count_db["T"][0]["Count"] += 1
        count_save = [{
                        "Count" : count_db["T"][0]["Count"]
                        }]
        count_db["T"] = count_save
        search_db[str(count_db["T"][0]["Count"])] = added_tools
        json.dump(count_db, open("count.txt", 'w'))
        json.dump(search_db, open("searchdb.txt", 'w'))



s = LoginRegister()
