from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable
import sqlite3
import webbrowser as www

import mysql.connector as mysql

demo=mysql.connect(host='localhost',password='LL44sris$',user='root')

mycursor=demo.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT")


#LINKING PYTHON WITH SQL USING CONNECTOR
#CREATING DATABASE WITH TABLE AND INSERTING VALUES  

def database():
    global entry_1,entry_2,radio,c,gender,droplist1,droplist2,droplist
    name1=entry_1.get()
    email=entry_2.get()
    gender=droplist1.get()
    stream=droplist.get()
    Class=droplist2.get()
    demo=mysql.connect(host='localhost',password='LL44sris$',user='pranav',database='student')
    mycursor=demo.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS REGISTRATION(STUDENTNAME VARCHAR(25),EMAILID VARCHAR(100),
                        GENDER VARCHAR(10),STREAM VARCHAR(30),CLASS VARCHAR(10))''')
    if gender=="male":
        mycursor.execute('INSERT INTO REGISTRATION VALUES("{}","{}","{}","{}","{}")'.format(name1,email,'MALE',stream,Class))
        demo.commit()
    elif gender=="female":
        mycursor.execute('INSERT INTO REGISTRATION VALUES("{}","{}","{}","{}","{}")'.format(name1,email,'FEMALE',stream,Class))
        demo.commit()


#FUNCTION BLOC FOR REGISTRATION PAGE
#USING TKINTER AND FILLING THE DETAILS MENTIONED 

def wel():
    global entry_1,entry_2,radio,c,d,droplist1,droplist2,e,droplist
    root=Tk()
    root.geometry('800x800')
    root.title("registration form")
    label_0 = Label(root, text="REGISTRATION FORM",width=20,font=("bold",22))
    label_0.place(x=90,y=53)



    label_1= Label(root, text="Fullname",width=20,font=("bold",10))
    label_1.place(x=80,y=130)


    entry_1= Entry(root)
    entry_1.place(x=240,y=130)




    label_2= Label(root, text="Email",width=20,font=("bold",10))
    label_2.place(x=70,y=180)


    entry_2= Entry(root)
    entry_2.place(x=240,y=180)


    label_3= Label(root, text="Gender",width=20,font=("bold",10))
    label_3.place(x=70,y=230)


    c1=StringVar()
    d=['male','female']
    droplist1=ttk.Combobox(root,textvariable=c1,value=d,state='readonly')
    droplist1.config(width=15) 
    droplist1.place(x=200,y=50)


    label_4 = Label(root, text="Stream",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)


    list1 = ['Engineering','Medical','Law','Arts','Commerce','Fashion Design']
    c=StringVar()
    droplist=ttk.Combobox(root,textvariable=c,value=list1,state='readonly')
    droplist.config(width=15) 
    droplist.place(x=240,y=280)



    label_4 = Label(root, text="Class",width=20,font=("bold", 10))
    label_4.place(x=85,y=330)

    c2=StringVar()
    e=['XI','XII']
    droplist2=ttk.Combobox(root,textvariable=c2,value=e,state='readonly')
    droplist2.config(width=15) 
    droplist2.place(x=150,y=200)
    



    abc=Button(root, text='Submit',width=20,bg='brown',fg='white',command=database)
    abc.place(x=180,y=380)
    root.mainloop()#nfn



#FUNCTION BLOC FOR PRETTY TABLE IN PYTHON 

def reg():
    name=Entry
    admin = mysql.connect( user = 'root',
                         password = 'LL44sris$',
                         host = 'localhost',
                         database = 'student')
    
    cur = admin.cursor()
    
    cur.execute('SHOW TABLES')
    
    tables = [ i[0] for i in cur.fetchall()]
    
    for table in tables:
        print("Table " + table)
        cur.execute('DESC ' + table)
        cols = [i[0] for i in cur.fetchall()]
        cur.execute('SELECT * FROM ' + table)
        rows = cur.fetchall()
        ptable = PrettyTable(cols)
        for i in range(len(rows)):
            ptable.add_row(rows[i])
        print(ptable)
        print()
    cur.execute('SELECT * FROM REGISTRATION')
    print(cur.fetchall())


#CODE SNIPPET FOR OPENING MAIN PAGE LINKED WITH VARIOUS FEATURES     

def firstpage():
    root2=Tk()
    title=Label(root2,text='Welcome to exam registration',font=('Algerian',30),width=30)
    title.grid(row=1,column=2,pady=100,padx=60)
    new=Button(root2, text='New candidate',width=20,bg='brown',fg='white',command=wel)
    new.grid(row=2,column=1,padx=50)
    old=Button(root2, text='registered candidate',width=20,bg='brown',fg='white',command=reg)
    old.grid(row=2,column=3)

#ADDING VARIOUS BUTTONS TO THE MAIN PAGE 

def main():
    root3=Tk()
    root3.state('zoomed')
    #root3['bg']="#1f2e67 0%, #3a4d95 100%"
    x=Label(root3,text='AIITS Application Form 2020',font=('Algerian',35))
    x.grid(row=1,column=2)#,pady=80,padx=280
    apply=Button(root3,text='APPLY',font=('Times New Roman',15),bg='yellow',command=firstpage)
    apply.grid(row=10,column=2)
    #vk=PhotoImage(file="Exam.jpg")
    #abd=Label(root3,image=vk)
    #abd.grid(row=3,column=2,pady=29)
    #abd.image=vk
    fb=Button(root3,text='ELIGIBILITY',font=('Times New Roman',15))
    fb.grid(row=2,column=1)
    fb.bind('<Button-1>',eligibility)
    fb=Button(root3,text='COURSES OFFERED',font=('Times New Roman',15))
    fb.grid(row=2,column=3)
    fb.bind('<Button-1>',coursesoffered)
    fb=Button(root3,text='EXAM PATTERN',font=('Times New Roman',15))
    fb.grid(row=3,column=1,padx=80)
    fb.bind('<Button-1>',exampattern)
    fb=Button(root3,text='COUNCELLING',font=('Times New Roman',15))
    fb.grid(row=3,column=3)
    fb.bind('<Button-1>',councelling)



#ELEGIBILITY INFORMATION USING HTML PAGE 

def eligibility(x):
    f=open('eligibility.html','w+')
    m='''<html><body><br>
    <br>Nationality:
    <br>•The applicant for admission should be a Resident / Non Resident Indian National / PIO.
    <br>•Foreign Candidates studied/studying abroad can apply directly through foreign category only. A separate application form is made available.
    <br>Kindly check our website for details.
    <br>
    <br>Age Limit :
    <br>•Candidates whose date of birth falls on or after 1st July 1998 are eligible to apply for AIITS-2020. The date of birth as recorded in the High School / SSC / X Certificate will be considered authentic. Candidates should produce this certificate in original as a proof of their age at the time of counselling, failing for which they will be disqualified.
    <br>
    <br>Qualifying Examination:
    <br>
    <br>Candidates appearing for the AIITS-2020 should have either completed or shall be appearing in 2020, in any one of the following qualifying examinations :
    <br>•The final examination of the 10+2 system of Higher Secondary Examination conducted by the State Board; Central Board of Secondary Education (CBSE, New Delhi), The Council for
    <br>•Indian School Certificate Examination (ISCE), New Delhi.
    <br>•Intermediate or Two-year Pre-University Examination conducted by a recognized Board/ University.
    <br>•High School Certificate Examination of the Cambridge University or International Baccalaureate Diploma of the International Baccalaureate Office, Geneva.
    <br>•General Certificate Education (GCE) examination (London/Cambridge/Srilanka) at the Advanced (A) level.
    <br>•As per VIT Norms, Regular 'NIOS' board candidates are also eligible for AIITS. They should produce the Migration Cum Transfer Certificate at the time of joining.
    <br>
    <br>Eligibility Criteria For The Qualifying Examination:
    <br>•Candidates appearing for the AIITS in 2020 should have secured minimum aggregate of 60% in Physics, Chemistry, and Mathematics/Biology in the qualifying examination (+2/Intermediate).
    <br>•The average marks obtained in the subjects Physics, Chemistry and Mathematics or Biology (PCM / PCB) in +2 (or its equivalent) put together should be minimum aggregate of 50% for the following categories:
    <br>Candidates belonging to SC/ST
    <br>Candidates hailing from Jammu and Kashmir/ Ladakh and the North Eastern states of Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim and Tripura. CERTIFICATE TO PROVE COMMUNITY / NATIVITY should be produced at the time of counselling,
    <br>failing which they will not be considered for admission.
    </body>
    </html>'''
    f.writelines(m)
    f.close()
    f='eligibility.html'
    www.open_new_tab(f)


# PAGE FOR COURSES OFFERED USING HTML PAGE 

def coursesoffered(y):
    f1=open('coursesoffered.html','w')
    n='''<html><body>
    <br>B.Tech Course offered
    <br>Aerospace Engineering(4)
    <br>Biotechnology(1)
    <br>Bioengineering (4)
    <br>Chemical Engineering(1)
    <br>Civil Engineering(1,2)
    <br>Computer Science and Engineering(1,2,3,4)
    <br>Computer Science and Engineering with specialisation in Bioinformatics(1)
    <br>Computer Science and Engineering with specialisation in Information Security(1)
    <br>Computer Science and Engineering and Business systems(in collaboration with TCS)(1,3)
    <br>Computer Science and Engineering with specialisation in Data Science(1)
    <br>Computer Science and Engineering with specialisation in Internet of Things(1)
    <br>Computer Science and Engineering with specialisation in Data Analytics(3)
    <br>Computer Science and Engineering with specialisation in Networking & Security(3)
    <br>Computer Science and Engineering with specialisation in AI and Machine Learning(2,4)
    <br>Computer Science and Engineering with specialisation in Cyber Physical Systems(2)
    <br>Computer Science and Engineering with specialisation in Artificial Intelligence(3)
    <br>Computer Science and Engineering with specialisation in Gaming Technology(4)
    <br>Computer Science and Engineering with specialisation in Cyber security & Digital Forensics(4)
    <br>Computer Science and Engineering with specialisation in Block Chain Technology(1)
    <br>Computer Science and Engineering with specialisation in Artificial Intelligence and Robotics(2)
    <br>Computer Science and Engineering with specialisation in Robotics(3)
    <br>Electronics and Communication Engineering with specialisation in Artificial Intelligence and Cybernetics(4)
    <br>Electrical and Electronics Engineering(1,2,4)
    <br>Electronics and Communication Engineering(1,2,3,4)
    <br>Electronics and Communication with specialisation in Biomedical Engineering(1)
    <br>Electronics and Communication Engineering with specialisation in Embedded Systems(3)
    <br>Electronics and Communication Engineering with specialisation in VLSI(3)
    <br>Electronics and Instrumentation Engineering(1)
    <br>Electronics and Computer Engineering(2)
    <br>Fashion Technology(2)
    <br>Information Technology(1)
    <br>Mechanical with specialisation in Automotive Engineering(1)
    <br>Mechanical Engineering with specialisation in Gamification(4)
    <br>Mechanical Engineering(1,2,3,4)
    <br>Mechatronics and Automation(2)
    <br>Production and Industrial Engineering(1)
    <br>
    <br>B.Des. Course offered:
    <br>B.Des. Industrial Design(1)
    </body>
    </html>'''
    

    f1.write(n)
    f1.close()
    f1='coursesoffered.html'
    www.open_new_tab(f1)


# EXAM PATTERN PAGE 

def exampattern(z):
    f2=open('exampattern.html','w')
    GJ='''<html><body>Particulars: Details
    <br>
    <br>Mode of Examination: Computer Based Test (Online)
    <br>
    <br>Duration: 2 Hours 30 Minutes (150 Minutes)
    <br>
    <br>Sessions: There will be three sessions per day of the exam
    <br>
    <br>Session 1 - 9 AM to 11:30 AM
    <br>
    <br>Session 2 - 12:30 PM to 3 PM
    <br>
    <br>Session 3 - 4 PM to 6:30 PM
    <br>
    <br>Type of Questions:
    <br>Objective (Multiple Choice Questions)
    <br>
    <br>Sections
    <br>There will be four sections:
    <br>
    <br>Physics - 35 Questions
    <br>Chemistry - 35 Questions
    <br>Mathematics/Biology - 40 Questions
    <br>Aptitude - 10 questions
    <br>English - 5 Questions
    <br>
    <br>Total Number of Questions: 125 Questions
    <br>
    <br>Total Marks: 125 Marks
    <br>
    <br>Marking Scheme
    <br>For each correct answer, one mark will be awarded.
    <br>Negative Marking
    <br>There will be no negative marking.
    </body>
    </html>'''


    f2.write(GJ)
    f2.close()
    f2='exampattern.html'
    www.open_new_tab(f2)


#INFORMATION REGARDING COUNCELLING 

def councelling(g):
    f3=open('councelling.html','w')
    p='''<html><body>
    <br>The counselling of AIITS 2020 will be held for all eligible candidates in offline mode.<br>
    <br>All of the selected candidates will have to download their provisional letters and attend the counselling session as per their ranks and schedule.
    <br>Document verification will be conducted by the authorities. Allotment of the candidates will be done as per their merit and preferences selected for admission.
    <br>Availability of seats will also be a factor for allotment, Selected candidates will have to confirm their allotted seat and pay the required amount.
    <br>
    <br>Documents Required for Verification:
    <br>
    <br>1.AIITS-2020 e-Admit Card, Counselling Admit card and AIITS Result copy
    <br>
    2.Class X Board Certificate as a proof of date of birth or any other age proof Certificate
    <br>
    <br>3.Mark sheet of Qualifying Examination (If available)
    <br>
    <br>4.Class XII Hall ticket (For candidates awaiting results)
    <br>
    <br>5.Community Certificate (For SC/ST candidates only)
    <br>
    <br>6.Nativity Certificate (For candidates hailing from Jammu and Kashmir and the North Eastern states )
    <br>
    <br>7.Demand draft for Rs 50,000/- drawn in favour of 'Bangalore Institute of Technology', payable at Bangalore.
    <br>
    <br>8.Demand draft for Rs 21,000/- drawn in favour of 'Bangalore Institute of Technology', payable at Bangalore, for Hostel.
    </body>
    </html>'''


    f3.write(p)
    f3.close()
    f3='councelling.html'
    www.open_new_tab(f3)




main()
