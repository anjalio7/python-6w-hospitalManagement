from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu
import database
from tkcalendar import DateEntry
from tkinter import ttk
# import database


class Edit_appointment:
    def __init__(self):
        self.root=Tk()
        self.root.title("edit_appointment")

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
        
    def editAppointmentFrame(self,data):
        print("id",data)
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="EDIT APPOINTMENT",anchor=E,bg="white",fg="black")
        self.lab.place(x=460,y=30, width="340", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        self.lab1=Label(self.first,text="Doctor",anchor=E,bg="white",fg="black")
        self.lab1.place(x=460,y=100, width="80", height="30")
        self.lab1.config(font=("calibri",18,"bold"))


    
        self.lab2=Label(self.first,text="patient",anchor=E,bg="white",fg="black")
        self.lab2.place(x=440,y=150, width="100", height="30")
        self.lab2.config(font=("calibri",18,"bold"))

        self.lab3=Label(self.first,text="Date",anchor=E,bg="white",fg="black")
        self.lab3.place(x=350,y=200,width=190,height=30)
        self.lab3.config(font=("calibri",18,"bold"))

        self.lab4=Label(self.first,text="Time",anchor=E,bg="white",fg="black")
        self.lab4.place(x=370,y=250,width=170,height=30)
        self.lab4.config(font=("calibri",18,"bold"))

        self.lab4=Label(self.first,text="Reason",anchor=E,bg="white",fg="black")
        self.lab4.place(x=370,y=300,width=170,height=30)
        self.lab4.config(font=("calibri",18,"bold"))

        
        #entries

        # for i in database.get_doctor(data): 
        #     print(i)

        # self.name=StringVar()
        # self.doctor=Entry(self.first)
        # self.doctor.place(x=570,y=100,width=210,height=30)
        self.doctor = StringVar()
        self.doctor = (database.dynamicDoctor())
        self.Doctorselbox = ttk.Combobox(self.first,state="readonly",textvariable=self.doctor,value=self.doctor)
        self.Doctorselbox.place(x = 570,y=100,width="210",height="30")
        self.Doctorselbox['state'] = 'disabled'
        
        # self.specialist=StringVar()
        # self.patient=Entry(self.first)
        # self.patient.place(x=570,y=150,width=210,height=30)

        self.patient = StringVar()
        self.patient = (database.dynamicPatient())
        self.Patientselbox = ttk.Combobox(self.first,state="readonly",textvariable=self.patient,value=self.patient)
        self.Patientselbox.place(x = 570,y=150,width="210",height="30")
        self.Patientselbox['state'] = 'disabled'

        self.id=Entry(self.first)
        self.id.place(x=570,y=200,width=210,height=30)

        # self.contact_number=StringVar()
        # self.date=Entry(self.first)
        # self.date.place(x=570,y=200,width=210,height=30)

        self.date=StringVar()
        self.dt=DateEntry(self.first,textvariable=self.date)
        self.dt.place(x=570,y=200,width="210",height="30")

        
        # self.qualification=StringVar()
        self.time=Entry(self.first)
        self.time.place(x=570,y=250,width=210,height=30)

        self.reason=Entry(self.first)
        self.reason.place(x=570,y=300,width=210,height=30)
        
       
    #buttons
        self.loginButton = Button(self.first, text = "Update", command = self.appointment)
        self.loginButton.place(x=460,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=410,width=100,height=40)

        # fetchdata
        for i in database.get_appointment(data):
            print(i)
            self.id.insert(0,i[0])
            self.Doctorselbox.set(i[1])
            self.Patientselbox.set(i[2])
            # self.date = i[3]
            self.time.insert(0,i[4])
            self.reason.insert(0, i[5])
           


        self.root.mainloop()

    
    def appointment(self):
        data = (
            self.id.get(),
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
            res = database.updateappointment(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Appointment updated successfully.")
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
    obj1 = Edit_appointment()
    obj1.editAppointmentFrame('data')
    
         
    
