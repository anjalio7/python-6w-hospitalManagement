from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import menu 
import database
from tkcalendar import DateEntry
from tkinter import ttk
# import database


class Edit_prescriptions:
    def __init__(self):
        self.root=Tk()
        self.root.title("Edit_prescriptions")

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
    def dose_price(self,e):
        self.dose.config(state="normal")
        self.DATA = self.Doctorselbox.get().split()
        self.data_doc = self.DATA[2]
        self.dose.delete(0, 'end')
        if ((self.Doctorselbox != '')):
            self.dose.insert(0,self.data_doc)
            self.dose.config(state="disabled")
        else:
            return 0
        
    def editprescriptionsFrame(self,data):
        print("id",data)
        self.data = data
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
        self.Doctorselbox = ttk.Combobox(self.first,value=self.doctor)
        self.Doctorselbox.place(x = 570,y=150,width="210",height="30")

        # self.patient = StringVar()
        patient = database.dynamicPatient()
        self.Patientselbox = ttk.Combobox(self.first,value=patient)
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
    
       
    #buttons
        self.loginButton = Button(self.first, text = "Update", command = self.prescription)
        self.loginButton.place(x=460,y=450,width=100,height=40)

        self.loginButton = Button(self.first, text = "Back", command = self.menuWindow)
        self.loginButton.place(x=590,y=450,width=100,height=40)

        # fetchdata
        for i in database.get_prescription(data):
            print("get ",i)
            self.Doctorselbox.insert(0,(i[1],i[2],i[3]))
            self.Patientselbox.insert(0,(i[4],i[5]))
            self.dose.insert(0,i[6])
            self.tablets.insert(0,i[7])
            self.sideeffect.insert(0,i[8])
            self.tabletName.insert(0, i[9])
           


        self.root.mainloop()

    
    def prescription(self):
        
        self.doc = self.Doctorselbox.get()
        self.patient = self.Patientselbox.get()
        data = (
            self.doc[0],
            self.patient[0],
            self.dose.get(),
            self.tablets.get(),
            self.sideeffect.get(),
            self.tabletName.get(),
            self.data[0]
        )
        if self.doc == '':
                messagebox.showinfo('Alert', 'Please enter doctor name first')
        elif self.patient == "":
            messagebox.showinfo('Alert','Please enter patient name')
        elif self.tablets.get() == "":
            messagebox.showinfo('Alert','Please enter date')    
        elif self.sideeffect.get() == "":
            messagebox.showinfo('Alert','Please enter time')      
        elif self.tabletName.get() == "":
            messagebox.showinfo('Alert','Please enter reason for prescription.')         
        else:
            print(data)
            res = database.updateprescription(data)
            # print('res')
            if res:
                messagebox.showinfo("Message", "prescription updated successfully.")
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
    obj1 = Edit_prescriptions()
    obj1.editprescriptionsFrame('data')
    
         
    
