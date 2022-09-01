from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import login
import add_doctor
import add_patient
import create_appointment
import appointment_history
import manage_doctor
import manage_patient
import database
import welcome
import prescription
import presciptions_history
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
        self.receptionist = Menu(self.menu)
        self.menu.add_cascade(label= "Doctor" , menu=self.receptionist)
        self.receptionist.add_command(label="Add",command=self.openAddDoctor)
        self.receptionist.add_command(label="Manage",command=self.openmanagerec)

        self.account = Menu(self.menu)
        self.menu.add_cascade(label = "patient", menu = self.account)
        self.account.add_command(label="add",command=self.openAddPatient)
        self.account.add_command(label="Manage",command=self.openmanagePatient)

        self.appointment = Menu(self.menu)
        self.menu.add_cascade(label=  "Appointment", menu=self.appointment)
        self.appointment.add_command(label="Create's Appointment",command=self.opentoday)
        self.appointment.add_command(label = "Appointment's History",command=self.openapphistoryer)
     #button
        self.Prescriptions = Menu(self.menu)
        self.menu.add_cascade(label=  "Prescriptions", menu=self.Prescriptions)
        self.Prescriptions.add_command(label="Create's Prescriptions",command=self.openprescriptions)
        self.Prescriptions.add_command(label = "Prescriptions's History",command=self.openManagePrescriptions)
     
        self.menu.add_command(label="Logout",command=self.logout)
        

        self.root.config(menu= self.menu)

    def navframe(self):
        self.navfra = Frame(self.root)
        self.navfra.place(x=0, y=0, width="900", height="600")
        self.navfra.config(bg="white")
        self.root.resizable(height=False, width=False)
        
        self.image = Image.open("images/doctorsidepic.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.navfra,image=self.bgimg)
        self.bglab.place(x=600, y=0,width="300",height="550")
 
        self.image0 = Image.open("images/doctor logo.jpg")
        self.bgimg0 = ImageTk.PhotoImage(self.image0)
        self.bglab0 = Label(self.navfra,image=self.bgimg0)
        self.bglab0.config(bg='white')
        self.bglab0.place(x=20, y=50,width="170",height="200")
    
        self.image1 = Image.open("images/patient logo.jpg")
        self.bgimg1 = ImageTk.PhotoImage(self.image1)
        self.bglab1 = Label(self.navfra,image=self.bgimg1)
        self.bglab1.config(bg='white')
        self.bglab1.place(x=18, y=300,width="180",height="200")


        self.image2 = Image.open("images/appointment logo.jpg")
        self.bgimg2 = ImageTk.PhotoImage(self.image2)
        self.bglab2 = Label(self.navfra,image=self.bgimg2)
        self.bglab2.config(bg='white')
        self.bglab2.place(x=300, y=50,width="180",height="200")
    
        self.navfra1=Label(self.root,text="Doctor-",fg="black",bg="white")
        self.navfra1.place(x=35,y=250, width="110", height="30")
        self.navfra1.config(font=("calibri",25,"bold"))

        self.navfra2=Label(self.root,text="Patient-",bg="white",fg="black")
        self.navfra2.place(x=23,y=500, width="125", height="30")
        self.navfra2.config(font=("calibri",25,"bold"))

        self.navfra3=Label(self.root,text="Appointment-",bg="white",fg="black")
        self.navfra3.place(x=335,y=230, width="193", height="40")
        self.navfra3.config(font=("calibri",25,"bold"))

        self.countdoctor1 = Label(self.navfra,text=len(database.viewdoctor()),anchor=E,fg="black",bg="white")
        self.countdoctor1.place(x=150,y=255,width="30",height="26")
        self.countdoctor1.config(font=("calibri",18,"bold"))
    
        # count=0
        # for i in database.viewpatient():
        #     count+=1

        # print(count)
        self.countpatient1=Label(self.navfra,text=len(database.viewpatient()),anchor=E,fg="black",bg="white")
        self.countpatient1.place(x=150,y=505,width="30",height="26")
        self.countpatient1.config(font=("calibri",18,"bold"))


        # count=0
        # for i in database.viewappointment():
        #     count+=1

        # print(count)
        self.countappointment1=Label(self.navfra,text=len(database.viewappointment()),anchor=E,fg="black",bg="white")
        self.countappointment1.place(x=530,y=238,width="30",height="26")
        self.countappointment1.config(font=("calibri",18,"bold"))


        self.root.mainloop()

    def openprescriptions(self):
        self.root.destroy()
        obj1 = prescription.create_presciptions() 
        obj1.createpresciptionsFrame()

    def openManagePrescriptions(self):
        self.root.destroy()
        obj = presciptions_history.presciptionsHistory()
        obj.manageHistory()

    def openmanagerec(self):
        self.root.destroy()
        obj = manage_doctor.ManageDoctor()
        obj.managedoc()

    def openmanagePatient(self):
        self.root.destroy()
        obj = manage_patient.Managepatient()
        obj.managepat()

    def opentoday(self):
        self.root.destroy()
        obj = create_appointment.create_appointment()
        obj.createAppointmentFrame()

    def openapphistoryer(self):
        self.root.destroy()
        obj = appointment_history.AppointmentHistory()
        obj.manageHistory()    

    def openAddDoctor(self):
        self.root.destroy()
        addDocObj = add_doctor.Add_doctor()
        addDocObj.addDoctorFrame()

    def openAddPatient(self):
        self.root.destroy()
        addPatObj = add_patient.Add_patient()
        addPatObj.AddPatientFrame()

    def opencreateappointment(self):

        self.root.destroy()
        obj = appointment_history.AppointmentHistory()
        obj.manageHistory()

    def logout(self):
        t=messagebox.askyesno("ALERT","Do You Realy Want To Exit?")
        if t:
            self.root.destroy()
            obj = welcome.Welcome()
            obj.frame()

if __name__=='__main__':
    obj1 = AdminNav()
    obj1.navframe()
        

        
        
        

         
        
    










