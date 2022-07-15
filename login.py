from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database
import menu

class AdminLogin:
    def __init__(self):
        self.root=Tk()
        self.root.title("Admin Login")

        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-900)/2)
        self.height=int((self.fullheight-550)/2)

        s = "900x550+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
        # self.root.mainloop()
        
    def loginFrame(self):
        self.first= Frame(self.root, bg='#202A44')

        self.first.place(x=0,y=0,width="800",height="500")
        
        self.first.place(x=0,y=0,width="900",height="550")
        
        #self.bgimg = PhotoImage(file="images/img4.jpg")
        #self.bglab = Label(self.first,image=self.bgimg)
        #self.bglab.place(x=0, y=0,width="50",height="50")
        
        
        img = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
        self.img = Label(image=img)
        self.img.place(x=350,y=50,width="180",height="200")

      #creating and placing labels
        self.lab=Label(self.first,text="USERNAME",anchor=E,bg='#202A44',fg='#D4AF37')
        self.lab.place(x=280,y=300,width="134",height="25")
        self.lab.config(font=("Calibri",20,"bold"))
        
        self.lab1=Label(self.first,text="PASSWORD",anchor=E,bg='#202A44',fg='#D4AF37')
        self.lab1.place(x=280,y=340,width="134",height="25")
        self.lab1.config(font=("Calibri",20,"bold"))

        #entries

        self.user=StringVar()
        self.ent=Entry(self.first,textvariable=self.user)
        self.ent.place(x=440,y=300,width="180",height="30")

        self.passw=StringVar()
        self.ent1=Entry(self.first,textvariable=self.passw,show = "*")
        self.ent1.place(x=440,y=340,width="180",height="30")

        #buttons

        self.loginButton = Button(self.first, text = "SUBMIT", command = self.login,bg='#202A44',fg='#D4AF37')
        self.loginButton.place(x = 420, y = 400, width = "110", height="40")
        self.loginButton.config(font=("Calibri",20,"bold"))


        self.root.mainloop()

    
    def login(self):
        data = (
            self.user.get(),
            self.passw.get()

        )
        if self.user.get() == "":
            messagebox.showinfo("Alert", "Enter the username first")
        elif self.passw.get() == "":
            messagebox.showinfo("Alert", "Enter the password")

            
            
        else:
            print(data)
            res = database.login(data)
            print(res)
            if res:

                messagebox.showinfo("Message", "Login Successfull")
                self.root.destroy()
                m = menu.AdminNav()
                m.navframe()
            else:
                messagebox.showinfo('Alert', 'Invalid username and/or password.')




      

if __name__=='__main__':
    obj1 = AdminLogin()
    obj1.loginFrame()
    