from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import manage_doctor
import database
import menu
from tkinter import ttk
# import database


class Edit_doctor:
    def __init__(self):
        self.root=Tk()
        self.root.title("Edit doctor")

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
    def editDoctorFrame(self, data):
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="EDIT DOCTORS",anchor=E,bg="white",fg="black")
        self.lab.place(x=310,y=30, width="370", height="45")
        self.lab.config(font=("calibri",30,"bold"))


        self.lab1=Label(self.first,text="Username",anchor=E,bg="white",fg="black")
        self.lab1.place(x=450,y=100,width=110,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        # self.lab1=Label(self.first,text="Password",anchor=E,bg="white",fg="black")
        # self.lab1.place(x=450,y=150,width=100,height=30)
        # self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Name",anchor=E,bg="white",fg="black")
        self.lab1.place(x=450,y=150, width="80", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Specialist",anchor=E,bg="white",fg="black")
        self.lab1.place(x=433,y=200, width="100", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Contact",anchor=E,bg="white",fg="black")
        self.lab1.place(x=348,y=250,width=190,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Qualification",anchor=E,bg="white",fg="black")
        self.lab1.place(x=370,y=300,width=170,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="charges",anchor=E,bg="white",fg="black")
        self.lab1.place(x=450,y=350,width=90,height=30)
        self.lab1.config(font=("calibri",18,"bold"))
        #entries


        self.username=StringVar()
        self.username=Entry(self.first,textvariable=self.username)
        self.username.place(x=570,y=100,width=210,height=30)

        # self.password=StringVar()
        # self.password=Entry(self.first,textvariable=self.password, show='*')
        # self.password.place(x=570,y=150,width=210,height=30)
        
        self.name=StringVar()
        self.name=Entry(self.first,textvariable=self.name)
        self.name.place(x=570,y=150,width=210,height=30)

        self.specialist = StringVar()
        self.specialist = ['Orthopedics', 'Dermatology', 'Pediatrics', 'Radiology', ' Anesthesia']
        self.special = ttk.Combobox(self.first,state="readonly",textvariable=self.specialist,value=self.specialist)
        self.special.place(x = 570,y=200,width="210",height="30")

        self.id=Entry(self.first)
        # self.id.place(x=570,y=200,width=210,height=30)
        
        self.contact=StringVar()
        self.contact=Entry(self.first,textvariable=self.contact)
        self.contact.place(x=570,y=250,width=210,height=30)

        self.qualification = StringVar()
        self.qualification = ['MBBS', 'MS', 'MD', 'BAMS', ' BHMS']
        self.qual = ttk.Combobox(self.first,state="readonly",textvariable=self.qualification,value=self.qualification)
        self.qual.place(x = 570,y=300,width="210",height="30")
        
        self.charges=StringVar()
        self.charges=Entry(self.first,textvariable=self.charges)
        self.charges.place(x=570,y=350,width=210,height=30)

        #buttons

        self.loginButton = Button(self.first, text = "Submit", command = self.doctor)
        self.loginButton.place(x=460,y=450,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=450,width=100,height=40)

        for i in database.get_doctor(data):
            print(i)
            self.id.insert(0,i[0])
            self.name.insert(0,i[1])
            self.special.set(i[2])
            self.contact.insert(0,i[3])
            self.qual.set(i[4])
            self.charges.insert(0,i[5])
            self.username.insert(0, i[6])

        self.root.mainloop()

    def doctor(self):
        data = (
            self.name.get(),
            self.special.get(),
            self.contact.get(),
            self.qual.get(),
            self.charges.get(),
            self.username.get(),
            self.id.get(),
        )
        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter doctor name first')
        elif(not(self.name.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in name")

        elif self.special.get() == "":
            messagebox.showinfo('Alert','Please enter doctor specialist')
        
        elif self.contact.get() == "":
            messagebox.showinfo('Alert','Please enter contact')  
        elif(not(self.contact.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digits in contact number") 
        elif (len(self.contact.get()) != 10):
            messagebox.showinfo('Alert', 'Please enter 10 digit contact')  

        elif self.qual.get() == "":
            messagebox.showinfo('Alert','Please enter doctor qualification')
        elif self.charges.get() == "":
            messagebox.showinfo('Alert','Please enter appointment charges') 
        elif(not(self.charges.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digit in appointment charges") 
        else:
            res = database.updateDoctor(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Doctor updated successfully.")
                self.root.destroy()
                obj = manage_doctor.ManageDoctor()
                obj.managedoc()
            else:
                messagebox.showinfo('Alert', 'Invalid data.')

    def menuWindow(self):
        self.root.destroy()
        obj = menu.AdminNav()
        obj.navframe()

if __name__=='__main__':
    obj1 = Edit_doctor()
    obj1.editDoctorFrame('data')
    
         
    
