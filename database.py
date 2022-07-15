import sqlite3

con = sqlite3.connect('doctorPatient.db')

cursor = con.cursor()

# create a function for admin login
def login(arg):
    try:
        cursor.execute('''SELECT * FROM admin WHERE username = :user and password = :pass''', {
            'user': arg[0],
            'pass': arg[1]
        })
        return cursor.fetchone()
    except:
        return False

def add_doctor(arg):
    try:
        print(arg)

        cursor.execute('''INSERT INTO add_doctor (name,specialist,contact_number,qualification,appointment_charges, username, password) VALUES(:name,:specialist,:contact_number,:qualification,:appointment_charges, :user, :password)''',{

            'name': arg[0],
            'specialist': arg[1],
            'contact_number': arg[2],
            'qualification' : arg[3],
            'appointment_charges': arg[4],
            'user': arg[5],
            'password': arg[6]
             })
        con.commit()
        return True
    except:
        return False        

def add_patient(arg):
    try:
        print(arg)

        cursor.execute('''INSERT INTO add_patient (name,gender,age,address,contact_number,check_in) VALUES (:name,:gender,:age,:address,:contact_number,:check_in)''',{

            'name': arg[0],
            'gender': arg[1],
            'age': arg[2],
            'address' : arg[3],
            'contact_number': arg[4],
            'check_in': arg[5]
             })
        con.commit()
        return True
    except:
        return False        

def viewmanage_patient():
    try:
        cursor.execute('SELECT * FROM add_patient')
        return cursor.fetchall()
    except:
        return False        

def deletemanage_patient(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM add_patient where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False



def viewmanage_doctor():
    try:
        cursor.execute('SELECT * FROM add_doctor')
        return cursor.fetchall()
    except:
        return False     

def deletemanage_doctor(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM add_doctor where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False


def create_appointment(arg):
    try:
        print("this",arg)

        cursor.execute('''INSERT INTO appointment (doctor,patient,date,time, cause, status) VALUES(:doctor,:patient,:date,:time, :cause, :status)''',{
            'doctor': arg[0],
            'patient': arg[1],
            'date': arg[2],
            'time' : arg[3],
            'cause': arg[4],
            'status': 'pending'
             })
        print(arg)
        con.commit()
        return True
    except:
        return False   

def viewcreate_appointment():
    try:
        cursor.execute('SELECT * FROM appointment')
        return cursor.fetchall()
    except:
        return False     


def deleteappointment_history(gup):
    try:
        print(gup)
        cursor.execute('''DELETE FROM appointment where id = :id''',{'id':gup[0]})
        con.commit()
        return True
    except:
        return False

def get_doctor(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM add_doctor WHERE id=:id',{'id':gup[0]})
        return cursor.fetchall()
    except:
        return False 

def updateDoctor(gup):
    try:
        print(gup)
        cursor.execute('''UPDATE add_doctor 
                SET  
                name=:name, 
                specialist=:specialist,
                contact_number=:contact_number,
                qualification=:qualification,
                appointment_charges=:appointment_charges,
                username = :user
                
                WHERE id=:id''',
                {
                    'id':gup[0],
                    'name':gup[1],
                    'specialist':gup[2],
                    'contact_number':gup[3],
                    'qualification':gup[4],
                    'appointment_charges':gup[5],
                    'user': gup[6]
                }
        )
        con.commit()
        # con.close()
        return True
    
    except:
        return False

def get_patient(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM add_patient WHERE id=:id',{'id':gup[0]})
        return cursor.fetchall()
    except:
        return False 

def updatepatient(gup):
    try:
        print(gup)
        cursor.execute('''UPDATE add_patient 
                SET  
                name=:name, 
                gender=:gender,
                age=:age,
                address=:address,
                contact_number=:contact_number, 
                check_in=:check_in
                WHERE id=:id''',
                {
                    'id':gup[0],
                    'name':gup[1],
                    'gender':gup[2],
                    'age':gup[3],
                    'address':gup[4],
                    'contact_number':gup[5],
                    'check_in':gup[6],
                }
        )
        con.commit()
        # con.close()
        return True
    
    except:
        return False

def viewdoctor():
    try:
        cursor.execute('SELECT * FROM add_doctor')
        return cursor.fetchall()
    except:
        return False

def viewpatient():
    try:
        cursor.execute('SELECT * FROM add_patient')
        return cursor.fetchall()
    except:
        return False        

def viewappointment():
    try:
        cursor.execute('SELECT * FROM appointment')
        return cursor.fetchall()
    except:
        return False                

def get_appointment(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM appointment WHERE id=:id',{'id':gup[0]})
        return cursor.fetchall()
    except:
        return False 

def updateappointment(gup):
    
    try:
        print(gup)
        cursor.execute('''UPDATE appointment 
                SET  
                doctor=:doctor, 
                patient=:patient,
                date=:date,
                time=:time,
                cause = :reason
                WHERE id=:id''',
                {
                    'id':gup[0],
                    'doctor':gup[1],
                    'patient':gup[2],
                    'date':gup[3],
                    'time':gup[4],
                    'reason': gup[5]
                }
        )
        con.commit()
        # con.close()
        return True
    
    except:
        return False



def dynamicDoctor():
    try:
        cursor.execute('SELECT name FROM add_doctor')
        return cursor.fetchall()
    except:
        return False


def dynamicPatient():
    try:
        cursor.execute('SELECT name FROM add_patient')
        return cursor.fetchall()
    except:
        return False


def doctorLogin(arg):
    try:
        cursor.execute('''SELECT * FROM add_doctor WHERE username = :user and password = :pass''', {
            'user': arg[0],
            'pass': arg[1]
        })
        return cursor.fetchone()
    except:
        return False


def viewDoctorAppointment(doctor):
    try:
        cursor.execute('''SELECT * FROM appointment WHERE doctor = :name''', 
        {'name': doctor})
        return cursor.fetchall()
    except:
        return False


def completeAppointment(id, doctor):
    try:
        cursor.execute('''UPDATE appointment SET status = "complete" WHERE  id = :id and doctor = :name''', {
            'id': id,
            'name': doctor
        })

        con.commit()
        return True
    except:
        return False


def viewDoctorAppointmnet(doctor):
    try:
        cursor.execute('''SELECT * FROM appointment where doctor = :doctor and status = "pending" ''', {'doctor': doctor})
        return cursor.fetchall()
    except: 
        return False

def viewDoctorAppointmnetComplete(doctor):
    try:
        cursor.execute('''SELECT * FROM appointment where doctor = :doctor and status = "complete" ''', {'doctor': doctor})
        return cursor.fetchall()
    except: 
        return False