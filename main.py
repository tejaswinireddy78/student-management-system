import tkinter as tk
from tkinter import messagebox
import sqlite3
root = tk.Tk()





#faculty database work start
def faculty_database():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS faculty(
            f_name text,
            l_name text,
            gender text,
            emp_id text,
            email text,
            mobile_no text,
            department text,
            designation text,
            complaint_type text,
            complain text,
            complaint_status text)""")
    c.execute("INSERT INTO faculty VALUES(:f_name,:l_name,:gender,:emp_id,:email,:mobile_no,:department,:designation,:complaint_type,:complain,:complaint_status)",
            {
                'f_name': entry1.get(),
                'l_name': entry2.get(),
                'gender': entry7.get(),
                'emp_id': entry3.get(),
                'email': entry4.get(),
                'mobile_no': entry5.get(),
                'department': entry6.get(),
                'designation': entry8.get(),
                'complaint_type': entry9.get(),
                'complain': entry10.get(),
                'complaint_status':"send"
            })

    conn.commit()
    conn.close()

#faculty database work ends




#faculty file complain window start

def faculty_complain():

    root = tk.Tk()
    canvas=tk.Canvas(root,height=700,width=800)
    canvas.pack()

    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    global entry7
    global entry8
    global entry9
    global entry10


    frame1=tk.Frame(root)
    frame1.place(relheight=0.05,relwidth=0.8)
    label1=tk.Label(frame1,text="FILL THE FOLLOWING DETAILS : ",font=("Arial",12))
    label1.pack()

    frame2=tk.Frame(root)
    frame2.place(rely=0.08,relheight=0.08,relwidth=0.8)
    label2=tk.Label(frame2,text="First Name:",font=("Arial",12))
    label2.pack()
    entry1=tk.Entry(frame2)
    entry1.pack()

    frame3=tk.Frame(root)
    frame3.place(rely=0.16,relheight=0.08,relwidth=0.8)
    label3=tk.Label(frame3,text="Last Name:",font=("Arial",12))
    label3.pack()
    entry2=tk.Entry(frame3)
    entry2.pack()

    frame8=tk.Frame(root)
    frame8.place(rely=0.24,relheight=0.08,relwidth=0.8)
    label8=tk.Label(frame8,text="Gender:",font=("Arial",12))
    label8.pack()
    entry7=tk.Entry(frame8)
    entry7.pack()

    frame4=tk.Frame(root)
    frame4.place(rely=0.32,relheight=0.08,relwidth=0.8)
    label4=tk.Label(frame4,text="Employee Id:",font=("Arial",12))
    label4.pack()
    entry3=tk.Entry(frame4)
    entry3.pack()

    frame5=tk.Frame(root)
    frame5.place(rely=0.4,relheight=0.08,relwidth=0.8)
    label5=tk.Label(frame5,text="Email Id:",font=("Arial",12))
    label5.pack()
    entry4=tk.Entry(frame5)
    entry4.pack()

    frame6=tk.Frame(root)
    frame6.place(rely=0.48,relheight=0.08,relwidth=0.8)
    label6=tk.Label(frame6,text="Mobile Number:",font=("Arial",12))
    label6.pack()
    entry5=tk.Entry(frame6)
    entry5.pack()

    frame7=tk.Frame(root)
    frame7.place(rely=0.56,relheight=0.08,relwidth=0.8)
    label7=tk.Label(frame7,text="Department:",font=("Arial",12))
    label7.pack()
    entry6=tk.Entry(frame7)
    entry6.pack()

    frame9=tk.Frame(root)
    frame9.place(rely=0.64,relheight=0.08,relwidth=0.8)
    label9=tk.Label(frame9,text="Designation:",font=("Arial",12))
    label9.pack()
    entry8=tk.Entry(frame9)
    entry8.pack()

    frame10=tk.Frame(root)
    frame10.place(rely=0.72,relheight=0.08,relwidth=0.8)
    label10=tk.Label(frame10,text="Type of Complaint:",font=("Arial",12))
    label10.pack()
    entry9=tk.Entry(frame10)
    entry9.pack()

    frame11=tk.Frame(root)
    frame11.place(rely=0.8,relheight=0.13,relwidth=0.8)
    label11=tk.Label(frame11,text="Your Complain:",font=("Arial",12))
    label11.pack()
    entry10=tk.Entry(frame11,width=60)
    entry10.pack()

    frame12=tk.Frame(root)
    frame12.place(rely=0.93,relheight=0.07,relwidth=0.8)
    button =tk.Button(frame12,text ="File Complaint",font=("Arial",12),command = faculty_database)
    button.pack()

    root.mainloop()
        
#faculty file complain window end


# faculty complain status starts
def tell_faculty_status():
    root=tk.Tk()

    conn=sqlite3.connect('complain.db')
    c= conn.cursor()

    c.execute("SELECT * FROM faculty WHERE emp_id = ?",(entry22.get(),))
    records = c.fetchall()
    
    if not records:
        messagebox.showinfo('InValid Info',"no record found")
        root.destroy()

    else:
        s1 ="Name :" + records[0][0] +" "+records[0][1]
        label1 = tk.Label(root,text=s1,font=("Arial",20))
        label1.pack()

        s2 = "Employee id :" + records[0][3]
        label2 = tk.Label(root,text=s2,font=("Arial",20))
        label2.pack()

        s3 = "Email id :" + records[0][4] + "\n"
        label3 = tk.Label(root,text=s3,font=("Arial",20))
        label3.pack()

        selected_list1 = [item[8] for item in records]
        selected_list2 = [item[9] for item in records]
        selected_list3 = [item[10] for item in records]

        for i in range(0,len(selected_list1)) :
            s4 = "Type of complaint :" + selected_list1[i]
            label4 = tk.Label(root,text=s4,font=("Arial",20))
            label4.pack()
            s5 = "Complaint :" + selected_list2[i]
            label5 = tk.Label(root,text=s5,font=("Arial",20))
            label5.pack()
            s6 = "Complaint Status :" + selected_list3[i]+"\n"
            label6 = tk.Label(root,text=s6,font=("Arial",20))
            label6.pack()

    conn.commit()
    conn.close()
    tk.mainloop()




def faculty_complain_status():
    global entry22
    root =tk.Tk()

    canvas=tk.Canvas(root,height=700,width=800)
    canvas.pack()

    frame11=tk.Frame(root)
    frame11.place(rely=0.02,relheight=0.1,relwidth=0.8)
    label11=tk.Label(frame11,text="ENTER YOUR EMPLOYEE ID:",font=("Arial",15))
    label11.pack()
    entry22=tk.Entry(frame11)
    entry22.pack()

    frame2=tk.Frame(root)
    frame2.place(rely=0.2,relheight=0.1,relwidth=0.8)
    button=tk.Button(frame2,text="SEE STATUS",font=("Arial",15),command = tell_faculty_status)
    button.pack()


    root.mainloop()

#faculty complain status ends


#faculty window start
def faculty():
    root2=tk.Tk()

    canvas=tk.Canvas(root2,height=700,width=800)
    canvas.pack()

    frame1=tk.Frame(root2)
    frame1.place(relx=0.3,rely=0.15,relheight=0.1,relwidth=0.5)
    label1=tk.Label(frame1,text="YOU WANT TO : ",font=("Arial",15))
    label1.pack()

    frame2=tk.Frame(root2)
    frame2.place(relx=0.3,rely=0.4,relheight=0.2,relwidth=0.5)
    button_ad=tk.Button(frame2,text="FILE A COMPLAINT",font=("Arial",15),command = faculty_complain)
    button_ad.pack()

    frame2=tk.Frame(root2)
    frame2.place(relx=0.3,rely=0.7,relheight=0.2,relwidth=0.5)
    button_ad=tk.Button(frame2,text="SEE COMPLAINT STATUS",font=("Arial",15),command = faculty_complain_status)
    button_ad.pack()

    root2.mainloop()
#faculty window ends

# student database starts
def student_database():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS student(
            f_name text,
            l_name text,
            gender text,
            enrollment_no text,
            email text,
            mobile_no text,
            department text,
            complaint_type text,
            complain text,
            complaint_status text)""")
    c.execute("INSERT INTO student VALUES(:f_name,:l_name,:gender,:enrollment_no,:email,:mobile_no,:department,:complaint_type,:complain,:complaint_status)",
            {
                'f_name': entry11.get(),
                'l_name': entry12.get(),
                'gender': entry17.get(),
                'enrollment_no': entry13.get(),
                'email': entry14.get(),
                'mobile_no': entry15.get(),
                'department': entry16.get(),
                'complaint_type': entry18.get(),
                'complain': entry19.get(),
                'complaint_status' : "send"
            })
    messagebox.showinfo("Complaint Filed","Your complaint has been filed successfully!")

    conn.commit()
    conn.close()


# student database ends


#student file complain window start

def student_complain():

    global entry11
    global entry12
    global entry13
    global entry14
    global entry15
    global entry16
    global entry17
    global entry18
    global entry19

    root = tk.Tk()
    canvas=tk.Canvas(root,height=700,width=800)
    canvas.pack()

    frame1=tk.Frame(root)
    frame1.place(relheight=0.05,relwidth=0.8)
    label1=tk.Label(frame1,text="FILL THE FOLLOWING DETAILS : ",font=("Arial",12))
    label1.pack()

    frame2=tk.Frame(root)
    frame2.place(rely=0.08,relheight=0.08,relwidth=0.8)
    label2=tk.Label(frame2,text="First Name:",font=("Arial",12))
    label2.pack()
    entry11=tk.Entry(frame2)
    entry11.pack()

    frame3=tk.Frame(root)
    frame3.place(rely=0.16,relheight=0.08,relwidth=0.8)
    label3=tk.Label(frame3,text="Last Name:",font=("Arial",12))
    label3.pack()
    entry12=tk.Entry(frame3)
    entry12.pack()

    frame8=tk.Frame(root)
    frame8.place(rely=0.24,relheight=0.08,relwidth=0.8)
    label8=tk.Label(frame8,text="Gender:",font=("Arial",12))
    label8.pack()
    entry17=tk.Entry(frame8)
    entry17.pack()

    frame4=tk.Frame(root)
    frame4.place(rely=0.32,relheight=0.08,relwidth=0.8)
    label4=tk.Label(frame4,text="Enrollment Number:",font=("Arial",12))
    label4.pack()
    entry13=tk.Entry(frame4)
    entry13.pack()

    frame5=tk.Frame(root)
    frame5.place(rely=0.4,relheight=0.08,relwidth=0.8)
    label5=tk.Label(frame5,text="Email Id:",font=("Arial",12))
    label5.pack()
    entry14=tk.Entry(frame5)
    entry14.pack()

    frame6=tk.Frame(root)
    frame6.place(rely=0.48,relheight=0.08,relwidth=0.8)
    label6=tk.Label(frame6,text="Mobile Number:",font=("Arial",12))
    label6.pack()
    entry15=tk.Entry(frame6)
    entry15.pack()

    frame7=tk.Frame(root)
    frame7.place(rely=0.56,relheight=0.08,relwidth=0.8)
    label7=tk.Label(frame7,text="Department:",font=("Arial",12))
    label7.pack()
    entry16=tk.Entry(frame7)
    entry16.pack()

    frame10=tk.Frame(root)
    frame10.place(rely=0.64,relheight=0.08,relwidth=0.8)
    label10=tk.Label(frame10,text="Type of Complaint:",font=("Arial",12))
    label10.pack()
    entry18=tk.Entry(frame10)
    entry18.pack()

    frame11=tk.Frame(root)
    frame11.place(rely=0.72,relheight=0.13,relwidth=0.8)
    label11=tk.Label(frame11,text="Your Complain:",font=("Arial",12))
    label11.pack()
    entry19=tk.Entry(frame11,width=60)
    entry19.pack()

    frame12=tk.Frame(root)
    frame12.place(rely=0.85,relheight=0.07,relwidth=0.8)
    button =tk.Button(frame12,text ="File Complaint",font=("Arial",12),command = student_database)
    button.pack()

    root.mainloop()


#student file complain window end

#student complain status starts

def tell_student_status():
    root=tk.Tk()

    conn=sqlite3.connect('complain.db')
    c= conn.cursor()

    c.execute("SELECT * FROM student WHERE enrollment_no = ?",(entry23.get(),))
    records = c.fetchall()
    
    if not records:
        messagebox.showinfo('InValid Info',"no record found")
        root.destroy()
    else:
        s1 ="Name :" + records[0][0] +" "+records[0][1]
        label1 = tk.Label(root,text=s1,font=("Arial",20))
        label1.pack()

        s2 = "Employee id :" + records[0][3]
        label2 = tk.Label(root,text=s2,font=("Arial",20))
        label2.pack()

        s3 = "Email id :" + records[0][4] + "\n"
        label3 = tk.Label(root,text=s3,font=("Arial",20))
        label3.pack()

        selected_list1 = [item[7] for item in records]
        selected_list2 = [item[8] for item in records]
        selected_list3 = [item[9] for item in records]

        for i in range(0,len(selected_list1)) :
            s4 = "Type of complaint :" + selected_list1[i]
            label4 = tk.Label(root,text=s4,font=("Arial",20))
            label4.pack()
            s5 = "Complaint :" + selected_list2[i]
            label5 = tk.Label(root,text=s5,font=("Arial",20))
            label5.pack()
            s6 = "Complaint Status :" + selected_list3[i]+"\n"
            label6 = tk.Label(root,text=s6,font=("Arial",20))
            label6.pack()

    conn.commit()
    conn.close()
    tk.mainloop()




def student_complaint_status():
    global entry23
    root =tk.Tk()

    canvas=tk.Canvas(root,height=700,width=800)
    canvas.pack()

    frame11=tk.Frame(root)
    frame11.place(rely=0.02,relheight=0.1,relwidth=0.8)
    label11=tk.Label(frame11,text="ENTER YOUR ENROLLMENT NO:",font=("Arial",15))
    label11.pack()
    entry23=tk.Entry(frame11)
    entry23.pack()

    frame2=tk.Frame(root)
    frame2.place(rely=0.2,relheight=0.1,relwidth=0.8)
    button=tk.Button(frame2,text="SEE STATUS",font=("Arial",15),command = tell_student_status)
    button.pack()


    root.mainloop()



#student complain status ends

#student window starts

def student():
    root2=tk.Tk()

    canvas=tk.Canvas(root2,height=700,width=800)
    canvas.pack()

    frame1=tk.Frame(root2)
    frame1.place(relx=0.3,rely=0.15,relheight=0.1,relwidth=0.5)
    label1=tk.Label(frame1,text="YOU WANT TO : ",font=("Arial",15))
    label1.pack()

    frame2=tk.Frame(root2)
    frame2.place(relx=0.3,rely=0.4,relheight=0.2,relwidth=0.5)
    button_ad=tk.Button(frame2,text="FILE A COMPLAINT",font=("Arial",15), command= student_complain)
    button_ad.pack()

    frame2=tk.Frame(root2)
    frame2.place(relx=0.3,rely=0.7,relheight=0.2,relwidth=0.5)
    button_ad=tk.Button(frame2,text="SEE COMPLAINT STATUS",font=("Arial",15),command = student_complaint_status)
    button_ad.pack()

    root2.mainloop()


#student window ends

#after login starts

def delete():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()

    c.execute("DELETE FROM faculty where complaint_status = 'resolved' ")

    conn.commit()
    conn.close()
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()

    c.execute("DELETE FROM student where complaint_status = 'resolved' ")

    conn.commit()
    conn.close()


def update_faculty_status():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    record_id=entry24.get()
    c.execute("UPDATE faculty SET complaint_status= :cs WHERE oid= "+entry24.get(), {'cs':entry26.get()}  )
    c.execute("SELECT * FROM faculty")

    conn.commit()
    conn.close()


def update_student_status():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    record_id=entry24.get()
    c.execute("UPDATE student SET complaint_status= :cs WHERE oid= "+entry25.get(), {'cs':entry27.get()}  )
    c.execute("SELECT * FROM faculty")

    conn.commit()
    conn.close()


def login():
    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS login(
            username text,
            password text)""")
    c.execute("INSERT INTO login VALUES(:username,:password)",
            { 'username':"admin",'password':"admin"})

    conn.commit()
    conn.close()

    conn=sqlite3.connect('complain.db')
    c= conn.cursor()
    c.execute("SELECT * FROM login where username = ? AND password = ?",(entry20.get(),entry21.get()))
    row = c.fetchone()
    conn.commit()
    conn.close()

    
    if row:
        root=tk.Tk()

        global entry24
        global entry25
        global entry26
        global entry27

        conn=sqlite3.connect('complain.db')
        c= conn.cursor()
        c.execute("SELECT *,oid FROM faculty")
        records=c.fetchall()
        conn.commit()
        conn.close()
        #print(records)
        
        label1 = tk.Label(root,text="All faculty complaints:",font=("Arial",15))
        label1.pack()
        for i in records:
            s1=" "
            s1+=str(i[11])+". Name:"+i[0]+" "+i[1]+", Emp_id:"+i[3]+", Email_id:"+i[4]+", Mob_no:"+i[5]+", Dept:"+i[6]+", complaint_type:"+i[8]+", complaint:"+i[9]+", complaint_status:"+i[10]
            #print(s1)
            label2 = tk.Label(root,text=s1,font=("Arial",10))
            label2.pack()

        label4 = tk.Label(root,text="Enter the complaint number:",font=("Arial",12))
        label4.pack()
        entry24=tk.Entry(root)
        entry24.pack()
        label6 = tk.Label(root,text="Enter new status:",font=("Arial",12))
        label6.pack()
        entry26=tk.Entry(root)
        entry26.pack()
        button1= tk.Button(root,text="update status",command = update_faculty_status)
        button1.pack()


        conn=sqlite3.connect('complain.db')
        c= conn.cursor()
        c.execute("SELECT *,oid FROM student")
        records1=c.fetchall()
        conn.commit()
        conn.close()

        #print(records1)
        label2 = tk.Label(root,text="All student complaints:",font=("Arial",15))
        label2.pack()
        for i in records1:
            s1="\n "
            s1+=str(i[10])+". Name:"+i[0]+" "+i[1]+", Emp_id:"+i[3]+", Email_id:"+i[4]+", Mob_no:"+i[5]+", Dept:"+i[6]+", complaint_type:"+i[7]+", complaint:"+i[8]+", complaint_status:"+i[9]
            label3 = tk.Label(root,text=s1,font=("Arial",10))
            label3.pack()
        
        label5 = tk.Label(root,text="Enter the complaint number:",font=("Arial",12))
        label5.pack()
        entry25=tk.Entry(root)
        entry25.pack()
        label7 = tk.Label(root,text="Enter new status:",font=("Arial",12))
        label7.pack()
        entry27=tk.Entry(root)
        entry27.pack()
        button2= tk.Button(root,text="update status",command = update_student_status)
        button2.pack()

        button3= tk.Button(root,text="Delete all resolved complaints",width=80,command = delete)
        button3.pack()

        tk.mainloop()
    else:
        messagebox.showinfo('InValid',"login was not successful")


#after login ends



#admin login page starts
def admin():

    global entry20
    global entry21
    root = tk.Tk()
    canvas=tk.Canvas(root,height=700,width=800)
    canvas.pack()

    frame1=tk.Frame(root)
    frame1.place(relheight=0.2,relwidth=0.8)
    label1=tk.Label(frame1,text="FILL YOUR CREDENTIALS : ",font=("Arial",15))
    label1.pack()

    frame2=tk.Frame(root)
    frame2.place(rely=0.3,relheight=0.2,relwidth=0.8)
    label2=tk.Label(frame2,text="USER NAME:",font=("Arial",15))
    label2.pack()
    entry20=tk.Entry(frame2)
    entry20.pack()

    frame3=tk.Frame(root)
    frame3.place(rely=0.6,relheight=0.2,relwidth=0.8)
    label3=tk.Label(frame3,text="PASSWORD:",font=("Arial",15))
    label3.pack()
    entry21=tk.Entry(frame3)
    entry21.pack()

    frame4=tk.Frame(root)
    frame4.place(rely=0.9,relheight=0.1,relwidth=0.8)
    button=tk.Button(frame4,text="LOGIN",font=("Arial",20), command = login)
    button.pack()

    root.mainloop()


#admin login page ends

#main window starts
canvas=tk.Canvas(root,height=700,width=800)
canvas.pack()

frame1=tk.Frame(root)
frame1.place(relx=0.3,rely=0.15,relheight=0.1,relwidth=0.4)
label1=tk.Label(frame1,text="YOU ARE : ",font=("Arial",20))
label1.pack()

frame2=tk.Frame(root)
frame2.place(relx=0.3,rely=0.3,relheight=0.2,relwidth=0.4)
button_ad=tk.Button(frame2,text="ADMIN",font=("Arial",20),command = admin)
button_ad.pack()

frame3=tk.Frame(root)
frame3.place(relx=0.3,rely=0.5,relheight=0.2,relwidth=0.4)
button_fac=tk.Button(frame3,text="FACULTY",font=("Arial",20),command = faculty)
button_fac.pack()

frame4=tk.Frame(root)
frame4.place(relx=0.3,rely=0.7,relheight=0.2,relwidth=0.4)
button_stu=tk.Button(frame4,text="STUDENT",font=("Arial",20),command = student)
button_stu.pack()
#main window ends

root.mainloop()