print('''\t\t=================================================
                \t   *COACHING MANAGEMENT SYSTEM*
    \t\t=================================================''')

import mysql.connector as sqltor
con=sqltor.connect(host='localhost',user='root',passwd='katy@05102005')
cur=con.cursor()
cur.execute("Create database if not exists coaching")
cur.execute("use coaching")
cur.execute("create table if not exists stud_rec(sno int primary key,stu_name varchar(20)not null,fee int,DOJ date)")
con.commit()

def add():
    sno=int(input("Enter Sno. to be added: "))
    stu_name=input("Enter Student's Name: ")
    fee=int(input("Enter the Amount of Fees: "))
    DOJ=input("Enter Date of Joinning: ")
    cur.execute("insert into stud_rec(sno,stu_name,fee,DOJ)values(%d,%s,%d,%s)"%(sno,stu_name,fee,DOJ))
    con.commit()
    print("\n          **********Student Record Saved Successfully !!!**********")

def search():
    print("             -----------Search for the Student Record----------")
    sno=input("Enter the Sno to be searched: ")
    cur.execute("select * from stud_rec where sno="+sno)
    for i in cur:
        sno,stu_name,fee,DOJ=i
        print("Sno\tStudent Name\t Fees\tDate of Joinning")
        print(sno,'\t',stu_name,'\t',fee,'\t',DOJ)
    con.commit()

def display():
    print("--------------------------------------------------------------------------------")
    print("              ~~~~~~~~~~ Data of All Students !!!~~~~~~~~~~")
    print("--------------------------------------------------------------------------------")
    cur.execute("select * from stud_rec")
    u=cur.fetchall()
    con.commit()
    w=(['sno','stu_name','fee','DOJ'])
    for sno,stu_name,fee,DOJ in u:
        print(sno,'\t',stu_name,'\t\t',fee,'\t\t',DOJ)
    con.commit()

def update():
    sno=input("Enter the Sno. whose fee is to be update: ")
    new_fees=input("Enter Updated fees: ")
    a="update stud_rec set fee={} where sno={}". format(new_fees,sno)
    cur.execute(a)
    cur.execute("select * from stud_rec where sno="+sno)
    print("--------------------------------------------------------------------------------")
    for i in cur:
        sno,stu_name,fee,DOJ=i
        print("Sno\tStudent Name\t Fees\tDate of Joinning")
        print(sno,'\t',stu_name,'\t\t',fee,'\t',DOJ)
    con.commit()
    print("\n              ********** Record Updated***********")

def delete():
    sno=input("Enter the Sno you want to delete: ")
    b="delete from stud_rec where sno={}". format(sno)
    cur.execute(b)
    print("              ********** Record Deleted !!!**********")
    con.commit()
    

while True:
    print("________________________________________________________________________________")
    print("\t\t1.Add Student Record")
    print("\t\t2.Search Student Record")
    print("\t\t3.Display All Student Record")
    print("\t\t4.Update Student Record")
    print("\t\t5.Delete Student Record")
    print("\t\t6.Exit")
    
    ch=int(input("\n\tEnter Your Choice: "))

    if(ch==1):
        add()

    elif(ch==2):
        search()

    elif(ch==3):
        display()

    elif(ch==4):
        update()

    elif(ch==5):
        delete()

    elif(ch==6):
        exit()

    else:
        print("\n                 __________Query Not Supported !!__________")
     
