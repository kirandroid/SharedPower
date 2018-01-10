from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pickle

def get_Login_Details():
    print(UID_Entry.get())
    print(Pass_Entry.get())

def Save_Profile(val):
    with open("database.txt", "wb") as db:
        pickle.dump(val, db)
        db.close()

def Load_Profile():
    with open("database.txt", "rb") as db:
        k = pickle.load(db)
        db.close()
        return k


# Profile = {"0":{"Name": "Kiran Pradhan", "UID": "kirandroid", "Pass": "banana", "DOB": "95/10/09", "CNo":"02624789"},
#            "1":{"Name": "Ram Sita", "UID": "SitaRam", "Pass": "Rasi", "DOB": "00/00/00", "CNo":"999999"}}
#
# with open("database.txt", "wb") as db:
#     pickle.dump(Profile, db)

# k = {"0":[{"Equip_name":"Pikaxe",
#            "Price" : "$25/day",
#            "Picture" : "c://downloads//x.jpg",
#            "Condition" : "Good"
#            },
#           {"Equip_name":"hasya",
#            "Price" : "$250/day",
#            "Picture" : "c://downloads//x.jpg",
#            "Condition" : "worst"}],
#      "1":[{"Equip_name":"Sword",
#            "Price" : "$5/day",
#            "Picture" : "c://downloads//x.jpg",
#            "Condition" : "excel"
#            },
#           {"Equip_name":"knife",
#            "Price" : "$2500/day",
#            "Picture" : "c://downloads//x.jpg",
#            "Condition" : "good"}]}
# k["0"][1]["price"]


window = Tk()
window.title("Shared Power")
window.geometry("500x300")
window.iconbitmap('fav.ico')
window.configure(background="white")

banner = PhotoImage(file = "banner.png")
div = Label(window, image = banner)
div.configure(background = "white")
div.grid(row = 0, column = 0, columnspan= 10)

#UserId and password Entry box
Label(window, text="UserID").grid(row = 1, column=0)
Label(window, text="Password").grid(row =2,column=0)

UID_Entry = Entry(window)
UID_Entry.grid(row = 1, column = 1)

Pass_Entry = Entry(window, show='*')
Pass_Entry.grid(row = 2, column = 1)

Login_Button = Button(window, text = "Login", command = get_Login_Details)
Login_Button.grid()
window.mainloop()

