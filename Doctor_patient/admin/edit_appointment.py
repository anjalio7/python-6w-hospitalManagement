from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu ,doctor_appointment
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
    def charges_price(self,e):
        self.charges.config(state="normal")
        self.DATA = self.Doctorselbox.get().split()
        self.data_doc = self.DATA[2]
        self.charges.delete(0, 'end')
        if ((self.Doctorselbox != '')):
            self.charges.insert(0,self.data_doc)
            self.charges.config(state="disabled")
        else:
            return 0
        
    def editAppointmentFrame(self,data):
        print("id",data)
        self.data = data
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

        self.lab1=Label(self.first,text="charges",anchor=E,bg="white",fg="black")
        self.lab1.place(x=390,y=200,width=150,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Date",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=250,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Time",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=300,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Reason",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=350,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))
        #entries
        self.doctor = (database.dynamicDoctor())
        self.Doctorselbox = ttk.Combobox(self.first,value=self.doctor)
        self.Doctorselbox.place(x = 570,y=100,width="210",height="30")
        self.Doctorselbox.bind('<<ComboboxSelected>>', self.charges_price)

        # self.patient = StringVar()
        patient = database.dynamicPatient()
        self.Patientselbox = ttk.Combobox(self.first,value=patient)
        self.Patientselbox.place(x = 570,y=150,width="210",height="30")

        self.charges=Entry(self.first,bg="white",font=('bold'))
        self.charges.place(x=570,y=200,width="210",height="30")
    

        self.dtEntry=DateEntry(self.first,bg="white",date_pattern='yyyy/mm/dd')
        self.dtEntry.place(x=570,y=250,width="210",height="30")

        self.timeEntry=Entry(self.first,bg="white")
        self.timeEntry.place(x=570,y=300,width=210,height=30)

        self.reasonEntry=Entry(self.first,bg="white")
        self.reasonEntry.place(x=570,y=350,width=210,height=30)
    
       
    #buttons
        self.loginButton = Button(self.first, text = "Update", command = self.appointment)
        self.loginButton.place(x=460,y=410,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=410,width=100,height=40)

        # fetchdata
        for i in database.get_appointment(data):
            print("get ",i)
            self.Doctorselbox.insert(0,(i[1],i[2],i[3]))
            self.Patientselbox.insert(0,(i[4],i[5]))
            self.charges.insert(0,i[6])
            self.charges.config(state='disabled')
            # self.dtEntry.set(i[7])
            self.timeEntry.insert(0,i[8])
            self.reasonEntry.insert(0, i[9])
           


        self.root.mainloop()

    
    def appointment(self):
        
        self.doc = self.Doctorselbox.get()
        self.patient = self.Patientselbox.get()
        data = (
            self.doc[0],
            self.patient[0],
            self.charges.get(),
            self.dtEntry.get(),
            self.timeEntry.get(),
            self.reasonEntry.get(),
            self.data[0]
        )
        if self.doc == '':
                messagebox.showinfo('Alert', 'Please enter doctor name first')
        elif self.patient == "":
            messagebox.showinfo('Alert','Please enter patient name')
        elif self.dtEntry.get() == "":
            messagebox.showinfo('Alert','Please enter date')    
        elif self.timeEntry.get() == "":
            messagebox.showinfo('Alert','Please enter time')      
        elif self.reasonEntry.get() == "":
            messagebox.showinfo('Alert','Please enter reason for appointment.')         
        else:
            print(data)
            res = database.updateappointment(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Appointment updated successfully.")
                self.root.destroy()
                obj = menu.AdminNav()
                obj.navframe()
            else:
                messagebox.showinfo('Alert', 'Invalid data.')

    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()


if __name__=='__main__':
    obj1 = Edit_appointment()
    obj1.editAppointmentFrame('data')
    
         
    
