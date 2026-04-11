import mysql.connector
dbconnector=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dinesh@9963",
    database="hospital_db"
)
print(dbconnector)
print("db connect sucessfully")

curobj=dbconnector.cursor()

#=============patients table======================
curobj.execute("""
CREATE TABLE if not exists patients(
patient_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
age INT,
gender VARCHAR(10),
disease VARCHAR(100),
phone VARCHAR(15) unique,
);
"""
)
#===========doctors table=========
curobj.execute("""
CREATE TABLE if not exists doctors(
doctor_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
specialization VARCHAR(50),
phone VARCHAR(15) unique,
);
"""
)
#==============appointments table=================
curobj.execute("""
CREATE TABLE if not exists appointments(
appointment_id INT PRIMARY KEY AUTO_INCREMENT,
patient_id INT,
doctor_id INT,
appointment_date DATE,
FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
);                         
"""
)
print("all tables connect sucessfully")


#=================patients_login===============
curobj.execute("select * from patients ")
allpatientsdata=curobj.fetchall()
def patients_login():
    curobj.execute("select * from patients ")
    allpatients=curobj.fetchall()
    print(allpatientsdata,'allpatientdata')
    nlogin=input('enter ur name login:-')
    plogin=input('enter ur phone login:-')
    for i in allpatientsdata:
        if i[1]==nlogin and i[5]==plogin:
            print('login sucess')
            break
        else:
            print("wrng login")
patients_login()

#==============show_patientsappointments============
def show_patients_appointments():
    curobj.execute('''
        SELECT 
            a.appointment_id,
            p.name,
            d.name,
            a.appointment_date
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
    ''')

    data = curobj.fetchall()

    if data:
        print("\npatients Appointment Details:")
        for row in data:
            print("Appointment ID:", row[0])
            print("Patient Name:", row[1])
            print("Doctor Name:", row[2])
            print("Date:", row[3])
            print("----------------------")
    else:
        print("No appointments found")
show_patients_appointments()    

#============doctors_login============
curobj.execute("select * from doctors ")
alldoctorsdata=curobj.fetchall()
def doctors_login():
    curobj.execute("select * from doctors ")
    allpatients=curobj.fetchall()
    print(alldoctorsdata,'alldoctorsdata')
    nlogin=input('enter ur name login:-')
    plogin=input('enter ur phone login:-')
    for i in alldoctorsdata:
        if i[1]==nlogin and i[3]==plogin:
            print('login sucess')
            break
        else:
            print("wrg login or wrg cerdencles")
doctors_login()

#===============show_all_appointments==================
def show_all_appointments():
    curobj.execute('''
        SELECT 
            a.appointment_id,
            p.name,
            d.name,
            a.appointment_date
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
    ''')

    data = curobj.fetchall()

    if data:
        print("\nAll Appointment Details:")
        for row in data:
            print("Appointment ID:", row[0])
            print("Patient Name:", row[1])
            print("Doctor Name:", row[2])
            print("Date:", row[3])
            print("----------------------")
    else:
        print("No appointments found")
show_all_appointments()

        
#================register patient=====================
def register_patient():
    n=input("enter ur p_name")
    a=int(input("enter ur P_age"))
    g=input("enter ur  P-gender")
    d=input("enter ur P_disease")
    p=input("enter ur P_phone")
    quarey="insert into patients (name,age,gender,disease,phone) values(%s,%s,%s,%s,%s)"
    data=(n,a,g,d,p)
    curobj.execute(quarey,data)
    dbconnector.commit()
    print("patient register sucessfull")
register_patient()

#================register doctor============
def register_doctors():
    n=input("enter ur D_name")
    sp=input("enter ur specialization")
    p=input("enter ur D_phone")
    quarey="insert into doctors(name,specialization,phone) values(%s,%s,%s)"
    data=(n,sp,p)
    curobj.execute(quarey,data)
    dbconnector.commit()
    print("doctor register sucessfull")
register_doctors()

#================register appointments=============
def register_appointments():
    p=int(input("enter ur patient_id"))
    d=int(input("enter ur doctor_id"))
    da=input("enter ur appointment_date")
    quarey="insert into appointments(patient_id,doctor_id,appointment_date) values(%s,%s,%s)"
    data=(p,d,da)
    curobj.execute(quarey,data)
    dbconnector.commit()
    print("appointments register sucessfull")
register_appointments()






