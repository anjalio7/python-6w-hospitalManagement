from tkinter import *
from tkinter import messagebox
from wsgiref import validate
from PIL import ImageTk, Image
from tkinter import ttk
import menu,presciptions_history
import database
from tkcalendar import DateEntry

class create_presciptions:
    def __init__(self):
        self.root=Tk()
        self.root.title("Create presciptions")

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

    def createpresciptionsFrame(self):
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels '


        self.lab=Label(self.first,text="create presciption",anchor=E,bg="white",fg="black")
        self.lab.place(x=330,y=50, width="460", height="45")
        self.lab.config(font=("calibri",30,"bold"))

        
        self.lab=Label(self.first,text="Doctor",anchor=E,bg="white",fg="black")
        self.lab.place(x=400,y=150, width="140", height="30")
        self.lab.config(font=("calibri",18,"bold"))

        self.lab=Label(self.first,text="Patient",anchor=E,bg="white",fg="black")
        self.lab.place(x=400,y=200, width="140", height="30")
        self.lab.config(font=("calibri",18,"bold"))


    
        self.lab1=Label(self.first,text="Dose",anchor=E,bg="white",fg="black")
        self.lab1.place(x=380,y=250, width="160", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="No of Tablets",anchor=E,bg="white",fg="black")
        self.lab1.place(x=390,y=300,width=150,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Side Effects",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=350,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Tablet Name",anchor=E,bg="white",fg="black")
        self.lab1.place(x=400,y=400,width=140,height=30)
        self.lab1.config(font=("calibri",18,"bold"))
        
        self.doctor = (database.dynamicDoctor())
        self.Doctorselbox = ttk.Combobox(self.first,state="readonly",value=self.doctor)
        self.Doctorselbox.place(x = 570,y=150,width="210",height="30")

        # self.patient = StringVar()
        patient = database.dynamicPatient()
        self.Patientselbox = ttk.Combobox(self.first,state="readonly",value=patient)
        self.Patientselbox.place(x = 570,y=200,width="210",height="30")
        # self.Patientselbox.bind('<<ComboboxSelected>>')

        self.dose=Entry(self.first,bg="white",font=('bold'))
        self.dose.place(x=570,y=250,width="210",height="30")


        self.tablets=Entry(self.first,bg="white")
        self.tablets.place(x=570,y=300,width=210,height=30)

        self.sideeffect=Entry(self.first,bg="white")
        self.sideeffect.place(x=570,y=350,width=210,height=30)

        self.tabletName=Entry(self.first,bg="white")
        self.tabletName.place(x=570,y=400,width="210",height="30")
    
        self.loginButton1 = Button(self.first, text = "Submit",fg="black", command = self.create_presciptions)
        self.loginButton1.place(x=470,y=450,width=100,height=40)

        self.loginButton2 = Button(self.first, text = "Back",fg="black", command =self.menuWindow)
        self.loginButton2.place(x=600,y=450,width=100,height=40)

        self.root.mainloop()

    def create_presciptions(self):
        self.patient_data = self.Patientselbox.get().split()
        self.doctor_data = self.Doctorselbox.get()
        
        data = (
        self.doctor_data[0],
        self.patient_data[0],
        self.dose.get(),
        self.tablets.get(),
        self.sideeffect.get(),
        self.tabletName.get(),
        )

        if self.Patientselbox.get() == "":
            messagebox.showinfo('Alert','Please enter patient name')
        elif self.tablets == "":
            messagebox.showinfo('Alert','Please enter no of tablets')
        elif self.tablets.get() == "":
            messagebox.showinfo('Alert','Please enter no of tablets') 
        elif self.sideeffect.get() == "":
            messagebox.showinfo('Alert','Please enter side effects.')  
        elif self.tabletName == "":
            messagebox.showinfo('Alert','Please enter tablet name')      
        else:
            print(data)
            res = database.create_presciptions(data)
            if res:
                messagebox.showinfo("Message", "create presciptions successfully.")
                self.root.destroy()
                
                obj = presciptions_history.presciptionsHistory()
                obj.manageHistory()
            else:
               messagebox.showinfo('Alert', 'Invalid data.')

    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

if __name__=='__main__':
    obj1 = create_presciptions() 
    obj1.createpresciptionsFrame()
    
         
    
