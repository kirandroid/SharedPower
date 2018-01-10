from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pickle


def Login_UI():
    global UID_Entry, Pass_Entry
    # UserId and password Entry box
    Label(window, text="UserID").grid(row=1, column=0)
    Label(window, text="Password").grid(row=2, column=0)

    UID_Entry = Entry(window)
    UID_Entry.grid(row=1, column=1)

    Pass_Entry = Entry(window, show='*')
    Pass_Entry.grid(row=2, column=1)

    Login_Button = Button(window, text="Login", command=get_Login_Details)
    Login_Button.grid()


def get_Login_Details():
    for k in Load_Profile().keys():
        if UID_Entry.get() == k:
            if Pass_Entry.get() == Load_Profile().get(k).get("Pass"):
                print("Welcome", Load_Profile().get(k).get("Name"))
                for t in Load_Profile().get(k).get("Hired_Equip").keys():
                    print("List of Hired Tools")
                    print(Load_Profile().get(k).get("Hired_Equip").get(t).get("Name"))
                    print(Load_Profile().get(k).get("Hired_Equip").get(t).get("Price"))
                    print(Load_Profile().get(k).get("Hired_Equip").get(t).get("Condition"))
        else:
            print("Invalid UserID or Password!")


def Save_Profile(val):
    with open("database.txt", "wb") as db:
        pickle.dump(val, db)
        db.close()


def Load_Profile():
    with open("database.txt", "rb") as db:
        k = pickle.load(db)
        db.close()
        return k


window = Tk()
window.title("Shared Power")
window.geometry("800x500")
window.iconbitmap('fav.ico')
window.configure(background="white")

banner = PhotoImage(file="banner.png")
div = Label(window, image=banner)
div.configure(background="white")
div.grid(row=0, column=0, columnspan=10)

Login_UI()

window.mainloop()






# Profile = {"kirandroid": {
#                             "Name" : "Kiran Pradhan",
#                             "UserID" : "kirandroid",
#                             "Pass" : "Password",
#                             "DOB" : "95/10/09",
#                             "CNo" : "0237856",
#                             "Gender": "Male",
#                             "Hired_Equip" : {
#                                                 "T1" : {
#                                                         "Name":"Pikaxe",
#                                                         "Price" : "$25/day",
#                                                         "Picture" : "c://downloads//x.jpg",
#                                                         "Condition" : "Good"
#                                                         },
#                                                 "T2" : {
#                                                         "Name":"hasya",
#                                                         "Price" : "$250/day",
#                                                         "Picture" : "c://downloads//x.jpg",
#                                                         "Condition" : "worst"
#                                                         }
#                                             },
#                             "Own_Equip" : {
#                                                 "T1" : {
#                                                         "Name":"Sword",
#                                                         "Price" : "$5/day",
#                                                         "Picture" : "c://downloads//x.jpg",
#                                                         "Condition" : "excel"
#                                                         },
#                                                 "T2" : {
#                                                         "Name": "knife",
#                                                         "Price": "$2500/day",
#                                                         "Picture": "c://downloads//x.jpg",
#                                                         "Condition": "good"
#                                                         }
#                                             }
#                          }
#           }
# with open("database.txt", "wb") as db:
#     pickle.dump(Profile, db)
