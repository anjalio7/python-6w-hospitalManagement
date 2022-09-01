from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import login
import doctor_appointment
import doctor_complete_appointment
import database
import welcome


class AdminNav:
    def __init__ (self):
        self.root=Tk()
        self.root.title("Admin Navigation | Doctor Patient Management")
        self.fullwidth=self.root.winfo_screenwidth()
        self.fullheight=self.root.winfo_screenheight()
        self.width=int((self.fullwidth-900)/2)
        self.height=int((self.fullheight-600)/2)
        s="900x550+" +str(self.width)+ "+" +str(self.height)
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
        self.menu=Menu()

        self.appointment = Menu(self.menu)
        self.menu.add_cascade(label=  "Appointment", menu=self.appointment)
        self.appointment.add_command(label = "Appointment List",command=self.openapphistoryer)
        self.appointment.add_command(label = "Completed Appointment List",command=self.openAppCom)
     #button
        self.menu.add_command(label="Logout",command=self.logout)
        

        self.root.config(menu= self.menu)

    def navframe(self, name):
        self.doctorUser = name
        print("doc",self.doctorUser)
        self.navfra = Frame(self.root)
        self.navfra.place(x=0, y=0, width="900", height="600")
        self.navfra.config(bg="white")
        self.root.resizable(height=False, width=False)
        
        self.image = Image.open("images/doctorsidepic.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.navfra,image=self.bgimg)
        self.bglab.place(x=600, y=0,width="300",height="550")
 
        self.image0 = Image.open("images/appointment logo.jpg")
        self.bgimg0 = ImageTk.PhotoImage(self.image0)
        self.bglab0 = Label(self.navfra,image=self.bgimg0)
        self.bglab0.config(bg='white')
        self.bglab0.place(x=20, y=50,width="170",height="200")
    
    
        self.navfra1=Label(self.root,text="Appointments",fg="black",bg="white")
        self.navfra1.place(x=35,y=250, width="210", height="30")
        self.navfra1.config(font=("calibri",25,"bold"))

        self.countdoctor1 = Label(self.navfra,text=len(database.viewDoctorAppointment(self.doctorUser)),anchor=E,fg="black",bg="white")
        self.countdoctor1.place(x=35,y=280,width="60",height="26")
        self.countdoctor1.config(font=("calibri",21,"bold"))
 


        self.root.mainloop()

    
    def openapphistoryer(self):
        self.root.destroy()
        obj = doctor_appointment.AppointmentHistory()
        obj.manageHistory(self.doctorUser)    
        

    def openAppCom(self):
        self.root.destroy()
        obj = doctor_complete_appointment.AppointmentHistory()
        obj.manageHistory(self.doctorUser)   


    def logout(self):
        t=messagebox.askyesno("ALERT","Do You Realy Want To Exit?")
        if t:
            self.root.destroy()
            obj = welcome.Welcome()
            obj.frame()

if __name__=='__main__':
    obj1 = AdminNav()
    obj1.navframe('name')
        
