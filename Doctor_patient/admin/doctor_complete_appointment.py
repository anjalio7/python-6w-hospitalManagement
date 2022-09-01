from email import message
from tkinter import *

import database
# import tabledatabase
from tkintertable import TableCanvas
import manage_patient
from tkinter import messagebox
from tkinter.ttk import Treeview
import doctorDashboard
import edit_appointment

class AppointmentHistory:
    def __init__(self):
        self.root=Tk()
        self.root.title("APPOINTMENT HISTORY")
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth - 900) / 2)
        self.height = int((self.fullheight - 600) / 2)
        s = "1000x500+" + str(self.width) + "+" + str(self.height)
        self.root.resizable(height=False, width=False)

        self.root.geometry(s)

    def manageHistory(self, name):
        self.doctorUser = name
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="500")
     
        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F','G','H'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Doctor")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Patient")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Date")
        self.tr.column('#3', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#4', text="Time")
        self.tr.column('#4', minwidth=0, width=150, stretch=NO)

        self.tr.heading('#5', text="Reason")
        self.tr.column('#5', minwidth=0, width=150, stretch=NO)

        self.tr.heading('#6', text="Status")
        self.tr.column('#6', minwidth=0, width=50, stretch=NO)

        
        j = 0
        # print(database.viewmanage_patient())
        val = (self.doctorUser[0],)
        for i in database.viewDoctorAppointmnetComplete(val):
            self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],i[4], i[5], i[6]))
            j += 1
        # create double action button
        # self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,width=1000,height=600)
        self.loginButton = Button(self.fr, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=890,y=30,width=100,height=40)
        self.root.mainloop()

   

    def menuWindow(self):
        self.root.destroy()
        obj = doctorDashboard.AdminNav()
        obj.navframe(self.doctorUser)

    def select_data(tree):
        curItem=tree.focus()
        value=tree.item(curItem,"values")
        # print("selsect",value)



if __name__=='__main__':
    obj = AppointmentHistory()
    obj.manageHistory('name')