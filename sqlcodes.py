import sqlite3
conn = sqlite3.connect("MDBA.db")
c1 = conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL\n(from sqlcodes.py)")


conn.execute("Drop table if EXISTS PATIENT")
conn.execute("Drop table if EXISTS CONTACT_NO")
conn.execute("Drop table if EXISTS ROOM")
conn.execute("Drop table if EXISTS TREATMENT")
conn.execute("Drop table if EXISTS MEDICINE")
conn.execute("Drop table if EXISTS employee")

conn.execute("""Create table PATIENT
            (PATIENT_ID int(10) primary key,
             NAME VARCHAR(20) not null,
             SEX varchar(10) not null,
             BLOOD_GROUP varchar(5) not null,
             DOB date not null,
             ADDRESS varcahr(100) not null,
             CONSULT_TEAM varchar(50) not null,
             EMAIL varchar(30) not null
             );""")
print("TABLE PATIENT CREATED")

conn.execute("""CREATE TABLE CONTACT_NO
            (PATIENT_ID int(10) PRIMARY KEY,
             CONTACTNO int(15) not null,
             ALT_CONTACT int(15),
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
             );""")
print("TABLE CONTACT_NO CREATED")

conn.execute("""Create table ROOM
            (PATIENT_ID int(10)not NULL ,
             ROOM_NO varchar(20) PRIMARY KEY ,
             ROOM_TYPE varchar(10) not null,
             RATE int(10) not null,
             DATE_ADMITTED date,
             DATE_DISCHARGED date NULL,
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
             );""")
print("TABLE ROOM CREATED")

conn.execute("""CREATE TABLE TREATMENT
            (PATIENT_ID int(10) primary key,
             TREATMENT varchar(100) not null,
             TREATMENT_CODE varchar(30) not null,
             T_COST int(20) not null,
            FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
            );""")
print("TABLE TREATMENT CREATED")

conn.execute("""CREATE TABLE MEDICINE
            (PATIENT_ID int(10) primary key,
             MEDICINE_NAME varchar(100) not null,
             M_COST int(20) not null,
             M_QTY int(10) not null,
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
             );""")
print("TABLE MEDICINE CREATED")

conn.execute("""create table employee
            (EMP_ID varchar(10) primary key,
             EMP_NAME varchar(20)not null,
             SEX varchar(10) not null,
             AGE int(5) not null,
             DESIG varchar(20) not null,
             SAL float(10) not null,
             EXP varchar(100) not null,
             EMAIL varcahr(20) not null,
             PHONE int(12))""")

print("TABLE EMPLOYEE CREATED")

conn.execute("DROP TABLE if EXISTS appointment")
conn.execute("""create table appointment
            (
             PATIENT_ID int(20) not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) not null,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
            foreign key(PATIENT_ID) references patient(PATIENT_ID),
            foreign key(EMP_ID) references doctor(EMP_ID));""")
# commit changes
conn.commit()

print("TABLE APPOINTMENT CREATED")

c1.execute("select * from patient")
results = c1.fetchone()
print(results)

# close connectio
conn.close()
