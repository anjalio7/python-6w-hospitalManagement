from tkinter import *
import login
import doctor_login

class Welcome:
    def __init__(self):
        self.root = Tk()
        #If tkinter doent load image than use Toplevel() instead of Tk()
        self.root.title("Doctor Navigation | Doctor Patient Management")
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth - 1200) / 2)
        self.height = int((self.fullheight - 600) / 2)-50
        s = "1200x600+" + str(self.width) + "+" + str(self.height)
        self.root.resizable(height=False, width=False)

        self.root.geometry(s)
    def frame(self):
        self.fra = Frame(self.root, bg='#202A44')
        self.fra.place(x=0, y=0, width="1200", height="600")

        # self.img=PhotoImage(file='images/travelhealth.png')
        # self.imglab=Label(self.fra,image=self.img)
        # self.imglab.place(x=0,y=0,width="1200",height="600")

        self.btn=Button(self.fra,text="Doctor",bg="Brown",fg="White",font="30",command=self.doctor)
        self.btn.place(x=250,y=250,width="200",height="50")

        self.btn = Button(self.fra, text="Admin", bg="Brown",fg="White",font="30",command=self.recept)
        self.btn.place(x=650, y=250, width="200",height="50")
        self.root.mainloop()

    def doctor(self):
        self.root.destroy()
        obj1 = doctor_login.AdminLogin()
        obj1.loginFrame()
    def recept(self):
        self.root.destroy()
        obj1 = login.AdminLogin()
        obj1.loginFrame()
        
if __name__=="__main__":
    obj=Welcome()
    obj.frame()
