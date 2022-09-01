import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="doctorpatient"
)
cursor=con.cursor()

# create a function for admin login
def login(arg):
    try:
        cursor.execute("SELECT * FROM admin WHERE username = %s and password = %s",arg)
        return cursor.fetchone()
    except:
        return False

def add_doctor(arg):
    try:
        print(arg)

        cursor.execute("INSERT INTO doctor (name,specialist,contact_number,qualification,appointment_charges, username, password) VALUES(%s,%s,%s,%s,%s, %s, %s)",arg)
        con.commit()
        return True
    except:
        return False        

def add_patient(arg):
       
    try:
        print(arg)
        cursor.execute("INSERT INTO patient (name,gender,age,address,contact_number,medical_history) VALUES (%s,%s,%s,%s,%s,%s)",arg)
        con.commit()
        return True
    except:
        return False        

def viewmanage_patient():
    try:
        cursor.execute('SELECT * FROM patient')
        return cursor.fetchall()
    except:
        return False        

def deletemanage_patient(gup):
    try:
        print(gup)
        cursor.execute("DELETE FROM patient where id =%s",gup)
        con.commit()
        return True
    except:
        return False



def viewmanage_doctor():
    try:
        cursor.execute('SELECT * FROM doctor')
        return cursor.fetchall()
    except:
        return False     

def deletemanage_doctor(gup):
    try:
        print(gup)
        cursor.execute("DELETE FROM doctor where id = %s",gup)
        con.commit()
        return True
    except:
        return False


def create_appointment(arg):
    try:
        print("this",arg)

        cursor.execute("INSERT INTO appointment (doctor_id,patient_id,Charges,date,time, cause) VALUES(%s,%s,%s,%s, %s, %s)",arg)
        print(arg)
        con.commit()
        return True
    except:
        return False   

def viewcreate_appointment():
    try:
        cursor.execute('SELECT appointment.id,doctor.name,patient.name,appointment.Charges,appointment.date,appointment.time,appointment.cause,appointment.status,appointment.check_in FROM appointment left join doctor on appointment.doctor_id = doctor.id left join patient on appointment.patient_id = patient.id')
        return cursor.fetchall()
    except:
        return False     


def deleteappointment_history(gup):
    try:
        print(gup)
        cursor.execute("DELETE FROM appointment where id = %s",gup)
        con.commit()
        return True
    except:
        return False

def get_doctor(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM doctor WHERE id=%s',gup)
        return cursor.fetchall()
    except:
        return False 

def updateDoctor(gup):
    try:
        print(gup)
        cursor.execute("UPDATE doctor SET name=%s, specialist=%s,contact_number=%s,qualification=%s,appointment_charges=%s,username = %s WHERE id=%s",gup)
        con.commit()
        # con.close()
        return True
    
    except:
        return False

def get_patient(gup):
    try:
        print("get",gup)
        cursor.execute('SELECT * FROM patient WHERE id=%s',gup)
        return cursor.fetchall()
    except:
        return False 

def updatepatient(gup):
    try:
        print(gup)
        cursor.execute("UPDATE patient SET name=%s, gender=%s,age=%s,address=%s,contact_number=%s, medical_history=%s WHERE id=%s",gup)
        con.commit()
        # con.close()
        return True
    except:
        return False

def viewdoctor():
    try:
        cursor.execute('SELECT * FROM doctor')
        return cursor.fetchall()
    except:
        return False

def viewpatient():
    try:
        cursor.execute('SELECT * FROM patient')
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
        cursor.execute('select appointment.id,doctor.id,doctor.name,doctor.appointment_charges,patient.id,patient.name,appointment.Charges,appointment.date,appointment.time,appointment.cause FROM appointment left join doctor on appointment.doctor_id = doctor.id left join patient on appointment.patient_id = patient.id where appointment.id=%s',gup)
        print("get",gup)
        return cursor.fetchall()
    except:
        return False 

def updateappointment(gup):
    
    try:
        print(gup)
        cursor.execute("UPDATE appointment SET  doctor_id=%s, patient_id=%s,Charges=%s,date=%s,time=%s,cause = %s WHERE id=%s",gup)
        con.commit()
        # con.close()
        return True
    
    except:
        return False



def dynamicDoctor():
    try:
        cursor.execute('SELECT ID,name,appointment_charges FROM doctor')
        return cursor.fetchall()
    except:
        return False


def dynamicPatient():
    try:
        cursor.execute('SELECT Id,name FROM patient')
        return cursor.fetchall()
    except:
        return False


def doctorLogin(arg):
    try:
        cursor.execute("SELECT * FROM doctor WHERE username = %s and password = %s", arg)
        return cursor.fetchone()
    except:
        return False


def viewDoctorAppointment(gup):
    try:
        cursor.execute("SELECT * FROM appointment WHERE doctor = %s",gup)
        return cursor.fetchall()
    except:
        return False


def completeAppointment(val):
    try:
        cursor.execute("UPDATE appointment SET status = 'complete' WHERE  id = %s and doctor_id = %s", val)
        con.commit()
        return True
    except:
        return False


def viewDoctorAppointmnet(doctor):
    try:
        cursor.execute("SELECT * FROM appointment where doctor_id = %s and status = 'pending' ",doctor)
        return cursor.fetchall()
    except: 
        return False

def viewDoctorAppointmnetComplete(doctor):
    try:
        cursor.execute('SELECT * FROM appointment where doctor_id = %s and status = "complete" ', doctor)
        return cursor.fetchall()
    except: 
        return False


def create_presciptions(arg):
    try:
        print(arg)
        cursor.execute("INSERT INTO prescription (doctor_id,patient_id,dose,no_of_tablets,sideeffect, Tablet_name) VALUES(%s,%s,%s,%s,%s,%s)",arg)

        con.commit()
        return True
    except:
        return False 

def viewcreate_prescriptions():
    try:
        cursor.execute('SELECT prescription.id,doctor.name,patient.name,prescription.dose,prescription.no_of_tablets,prescription.sideeffect,prescription.Tablet_name FROM prescription left join doctor on prescription.doctor_id = doctor.id left join patient on prescription.patient_id = patient.id')
        return cursor.fetchall()
    except:
        return False 

def get_prescription(gup):
    try:
        cursor.execute('select prescription.id,doctor.id,doctor.name,doctor.appointment_charges,patient.id,patient.name,prescription.dose,prescription.no_of_tablets,prescription.sideeffect,prescription.Tablet_name FROM prescription left join doctor on prescription.doctor_id = doctor.id left join patient on prescription.patient_id = patient.id where prescription.id=%s',gup)
        print("get",gup)
        return cursor.fetchall()
    except:
        return False    


def deleteprescriptions_history(gup):
    try:
        print(gup)
        cursor.execute("DELETE FROM prescription where id = %s",gup)
        con.commit()
        return True
    except:
        return False

def updateprescription(gup):
    try:
        print(gup)
        cursor.execute("UPDATE prescription SET  doctor_id=%s, patient_id=%s,dose=%s,no_of_tablets=%s,sideeffect =%s,Tablet_name  = %s WHERE id=%s",gup)
        con.commit()
        # con.close()
        return True
    
    except:
        return False