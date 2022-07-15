from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import menu
import database
from tkcalendar import DateEntry
# import database


class create_appointment:
    def __init__(self):
        self.root=Tk()
        self.root.title("Create appointment")

        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-900)/2)
        self.height=int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
        # self.root.mainloop()
        
    def createAppointmentFrame(self):
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels '


        self.lab=Label(self.first,text="CREATE APPOINTMENTS",anchor=E,bg="white",fg="black")
        self.lab.place(x=330,y=80, width="460", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        
        self.lab=Label(self.first,text="Doctor",anchor=E,bg="white",fg="black")
        self.lab.place(x=400,y=150, width="140", height="30")
        self.lab.config(font=("calibri",18,"bold"))


    
        self.lab1=Label(self.first,text="Patient",anchor=E,bg="white",fg="black")
        self.lab1.place(x=380,y=200, width="160", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Date",anchor=E,bg="white",fg="black")
        self.lab1.place(x=390,y=250,width=150,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Time",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=300,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Reason",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=350,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        #entries

        
        # self.doctor=StringVar()
        # self.doctor=Entry(self.first,textvariable=self.doctor)
        # self.doctor.place(x=570,y=150,width=210,height=30)
        
        self.doctor = StringVar()
        self.doctor = (database.dynamicDoctor())
        self.Doctorselbox = ttk.Combobox(self.first,state="readonly",textvariable=self.doctor,value=self.doctor)
        self.Doctorselbox.place(x = 570,y=150,width="210",height="30")
        
        
        # self.patient=StringVar()
        # self.patient=Entry(self.first,textvariable=self.patient)
        # self.patient.place(x=570,y=200,width=210,height=30)

        self.patient = StringVar()
        self.patient = (database.dynamicPatient())
        self.Patientselbox = ttk.Combobox(self.first,state="readonly",textvariable=self.patient,value=self.patient)
        self.Patientselbox.place(x = 570,y=200,width="210",height="30")

        
        # self.date=StringVar()
        # self.date=Entry(self.first,textvariable=self.date)
        # self.date.place(x=570,y=250,width=210,height=30)

        self.date=StringVar()
        self.dt=DateEntry(self.first,textvariable=self.date)
        self.dt.place(x=570,y=250,width="210",height="30")

        
        self.time=StringVar()
        self.time=Entry(self.first,textvariable=self.time)
        self.time.place(x=570,y=300,width=210,height=30)

        self.reason=StringVar()
        self.reason=Entry(self.first,textvariable=self.reason)
        self.reason.place(x=570,y=350,width=210,height=30)
    

        #buttons

        self.loginButton1 = Button(self.first, text = "Submit",fg="black", command = self.create_appointment)
        self.loginButton1.place(x=470,y=400,width=100,height=40)

        self.loginButton2 = Button(self.first, text = "Back",fg="black", command =self.menuWindow)
        self.loginButton2.place(x=600,y=400,width=100,height=40)

        self.root.mainloop()

    def create_appointment(self):
        data = (
        self.Doctorselbox.get(),
        self.Patientselbox.get(),
        self.date.get(),
        self.time.get(),
        self.reason.get()
        )


        if self.Doctorselbox.get() == '':
                messagebox.showinfo('Alert', 'Please enter doctor name first')
        

        elif self.Patientselbox.get() == "":
            messagebox.showinfo('Alert','Please enter patient name')

        

        elif self.date.get() == "":
            messagebox.showinfo('Alert','Please enter date')
            
        
        elif self.time.get() == "":
            messagebox.showinfo('Alert','Please enter time') 

        elif self.reason.get() == "":
            messagebox.showinfo('Alert','Please enter reason for appointment.') 

        
        else:
            res = database.create_appointment(data)
            if res:
                messagebox.showinfo("Message", "create appointment successfully.")
                self.root.destroy()
                m = menu.AdminNav()
                m.navframe()
            else:
               messagebox.showinfo('Alert', 'Invalid data.')




       


    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

if __name__=='__main__':
    obj1 = create_appointment() 
    obj1.createAppointmentFrame()
    
         
    
