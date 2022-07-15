from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu 
import database

# import database

class Add_patient:
    def __init__(self):
        self.root=Tk()
        self.root.title("Add Patient")

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
        
    def AddPatientFrame(self):
        self.first= Frame(self.root, bg="white")
        self.first.place(x=0,y=0,width="900",height="600")
        
        self.image = Image.open("images/sidepic1.jpg")
        self.bgimg = ImageTk.PhotoImage(self.image)
        self.bglab = Label(self.first,image=self.bgimg)
        self.bglab.place(x=0, y=0,width="300",height="600")
        
        
        #create and place labels 
        self.lab=Label(self.first,text="ADD PATIENTS",anchor=E,bg="white",fg="black")
        self.lab.place(x=370,y=30, width="370", height="45")
        self.lab.config(font=("calibri",30,"bold"))
     
        self.lab=Label(self.first,text="Name",anchor=E,bg="white",fg='black')
        self.lab.place(x=450,y=100, width="70", height="30")
        self.lab.config(font=("calibri",18,"bold"))


    
        self.lab1=Label(self.first,text="Gender",anchor=E,bg="white",fg='black')
        self.lab1.place(x=435,y=150, width="90", height="30")
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Age",anchor=E,bg="white",fg='black')
        self.lab1.place(x=480,y=200,width=40,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Address",anchor=E,bg="white",fg='black')
        self.lab1.place(x=430,y=250,width=100,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Contact",anchor=E,bg="white",fg='black')
        self.lab1.place(x=342,y=300,width=190,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        self.lab1=Label(self.first,text="Check_In",anchor=E,bg="white",fg='black')
        self.lab1.place(x=435,y=350,width=100,height=30)
        self.lab1.config(font=("calibri",18,"bold"))

        #entries

        
        self.name=StringVar()
        self.ent=Entry(self.first,textvariable=self.name)
        self.ent.place(x=570,y=100,width=210,height=30)
        
        
        self.gender=StringVar()
        self.ent=Entry(self.first,textvariable=self.gender)
        self.ent.place(x=570,y=150,width=210,height=30)

        
        self.age=StringVar()
        self.ent=Entry(self.first,textvariable=self.age)
        self.ent.place(x=570,y=200,width=210,height=30)

        
        self.address=StringVar()
        self.ent=Entry(self.first,textvariable=self.address)
        self.ent.place(x=570,y=250,width=210,height=30)
        
        self.contact=StringVar()
        self.ent=Entry(self.first,textvariable=self.contact)
        self.ent.place(x=570,y=300,width=210,height=30)

        self.check_In=StringVar()
        self.ent=Entry(self.first,textvariable=self.check_In)
        self.ent.place(x=570,y=350,width=210,height=30)

        #buttons

        self.loginButton = Button(self.first, text = "Submit", command = self.addPatient)
        self.loginButton.place(x=460,y=430,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=430,width=100,height=40)
        
        # self.gender = (male,female);
        # self.selbox = ttk.combobox(self.first,text=male,value=self.gender)
        # self.selbox.place(x=570,y=150,width=10,height=10)

    

        
        self.root.mainloop()

    
    def addPatient(self):
        data = (
            self.name.get(),
            self.gender.get(),
            self.age.get(),
            self.address.get(),
            self.contact.get(),
            self.check_In.get()
            )

        if self.name.get() == '':
            messagebox.showinfo('Alert', 'Please enter patient name first')
        elif(not(self.name.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in name") 

        elif self.gender.get() == "":
            messagebox.showinfo('Alert','Please enter patient gender')
        elif(not(self.gender.get()=='male') and not(self.gender.get()=='female')):
            messagebox.showinfo("Message", "Enter only male or female in gender")
        elif(not(self.gender.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in gender")

        elif self.age.get() == "":
            messagebox.showinfo('Alert','Please enter patient age')
        elif(not(self.age.get().isdigit())):
            messagebox.showinfo("Message", "Enter only characters in age") 

        elif self.address.get() == "":
            messagebox.showinfo('Alert','Please enter patient address') 
        elif(not(self.address.get().isalpha())):
            messagebox.showinfo("Message", "Enter only characters in address")    

        elif self.contact.get() == "":
            messagebox.showinfo('Alert','Please enter contact')  
        elif(not(self.contact.get().isdigit())):
            messagebox.showinfo("Message", "Enter only digits in contact number") 
        elif (len(self.contact.get()) != 10):
            messagebox.showinfo('Alert', 'Please enter 10 digit contact') 
        elif self.check_In.get() == "":
            messagebox.showinfo('Alert','Please enter patient check_In') 
        elif(self.check_In.get().isalpha()):
            messagebox.showinfo("Message", "Enter only digit in check_In")               
        else:
            res = database.add_patient(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "Patient added successfully.")
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
    obj1 = Add_patient()
    obj1.AddPatientFrame()
    
         
    
