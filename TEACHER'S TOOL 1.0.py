import mysql.connector
import datetime
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE=True
tabulate.WIDE_CHARS_MODE=True

db=str(input("ENTER THE NAME OF YOUR DATABASE:"))



mydb=mysql.connector.connect(host='localhost',user='root',password='Sai123!@#')
mycursor= mydb.cursor()
print('_'*50)

print('_'*50)

sql="CREATE DATABASE if not exists %s"%db


mycursor.execute(sql)
print("DATABASE",db,"CREATED SUCCESSFULLY........")
print('_'*50)
if mydb.is_connected:
    print("YOU ARE SUCCESSFULL CONNECTED TO YOUR DATABASE",db,"!!!!!!!")
print('_'*50)
print('_'*50)

mycursor.execute("use %s"%db)
tablename=input("NAME OF TABLE TO BE CREATED:")
query="CREATE TABLE if not exists "+tablename+ \
    "(  rollno int primary key,\
    name varchar(15) not null,\
    school varchar(15),\
    maths float ,\
    english float ,\
    computerscience float ,\
    physics float,\
    chemistry float ,\
    totalmarks float, \
    percentage float )"
print("TABLE " ,tablename,"CREATED SUCCESSFULLY......")
mycursor.execute(query)
print('_'*50)
while True:
    print('\n\n\n')
    print("*"*95)
    print('\t\t\t\t\t\t MAIN MENU')
    print("*"*95)
    print('\t\t\t\t  1. ADDING STUDENT RECORD')
    print()
    print('\t\t\t\t  2. DISPLAYING RECORDS OF  ALL STUDENT')
    print('\t\t\t\t  3. DISPLAYING RECORDS OF PARTICULAR STUDENT')
    print()
    print('\t\t\t\t  4. DELETING RECORD OF ALL STUDENTS')
    print('\t\t\t\t  5. DELETING RECORD OF PARTICULAR STUDENTS')
    print()
    print('\t\t\t\t  6. MODIFICATIONS IN RESULTS')
    print()
    print('\t\t\t\t  7. DISPLAYING RESULTS OF ALL STUDENTS')
    print('\t\t\t\t  8. DISPLAYING RESULTS OF PARTICULAR STUDENTS')
    print()
    print('\t\t\t\t  9. TO EXIT / QUIT')
    print('*'*50)
    print('ENTER YOUR CHOICE......',end='')
    choice =int(input())
    print('_'*50)

    if choice==1:
        try:
            print(" Please Enter Student Information........")
            print('_'*50)
            mrollno=int(input('Enter Student Roll Number:'))
            mname=input('Enter Student Name __________please use single/double quotes:')
            mschool=input('Enter School Name !only initials please!  __________please use single/double quotes:')
            mmaths=float(input('Enter Maths Marks out of 100:'))
            meng=float(input('Enter English Marks  out of 100:')) 
            mcs=float(input('Enter  Computer Science marks  out of 100:'))
            mphy=float(input('Enter Physics Marks  out of 100:')) 
            mchem=float(input('Enter  Chemistry Marks  out of 100 :'))
            mtotal=mmaths+meng+mcs+mphy+mchem
            mnet=mtotal/5
            rec=(mrollno,mname,mschool,mmaths,meng,mcs,mphy,mchem,mtotal,mnet) 
            query="INSERT INTO "+tablename+"(rollno , name , school , maths , english , computerscience , physics , chemistry,totalmarks , percentage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(mrollno,mname,mschool,mmaths,meng,mcs,mphy,mchem,mtotal,mnet)
            mycursor.execute(query)
            mydb.commit()
            print('RECORD ADDED SUCCESSFULLY!!!!!')
            
        except Exception as e:
            print('SOMETHING GONE WRONG^%$E%&$&^7...........',e)


    elif choice==2:
         try:
             query = "select * from "  +tablename
             mycursor.execute(query)
             print(tabulate(mycursor, headers = ['ROLLNO' , 'NAME' , 'SCHOOL' , 'mMATHS' ,'mENG', 'mCS' , 'mPHY', 'mCHEM' ,'TOTAL ','AGGREGATE %'  ] , tablefmt="fancy_grid"   ))
             
         except Exception as e:
             print("SOMETHING GONE WRONG^%$E%&$&^7......",e)
    
    elif choice ==3:
        try:
            en=int(input("Enter Roll Number Of Student Whose Record Is To Be Displayed :"))
            query="SELECT * FROM" '\n\n'+tablename+'\n\n' "WHERE rollno = %s " % (en)
            mycursor.execute(query)
            data=mycursor.fetchone()
            print(list(data))
        except Exception as e:
            print('SOMETHING GONE WRONG^%$E%&$&^7',e)




    elif choice==4:
        try:
            print("CAUTION   :    DATA CAN'T BE RETRIEVED AFTER DELETION")
            ch=input("!!!!!Do You Want To Delete All Records (Y/N)")
            if ch == "Y":
                mycursor.execute('delete from ' + tablename)
                mydb.commit()
                print('ALL THE RECORDS ARE DELETED SUCCESSFULLY...')
        except Exception as e:
            print('SOMETHING GONE WRONG^%$E%&$&^7....',e)

    elif choice==5:
        try:
            print("CAUTION   :    DATA CAN'T BE RETRIEVED AFTER DELETION")
            en=int(input('Enter Roll No. Of Record To Be Deleted....'))
            query="DELETE FROM " '\n\n' + tablename +'\n\n' "WHERE rollno = %s  " % (en,)  
            mycursor.execute(query)
            mydb.commit()
            print('DELETION DONE!!!!!')
            print()
            print ('you can confirm it by pressing key 2 ')
                
        except Exception as e:
            print('SOMETHING GONE WRONG^%$E%&$&^7-----',e)

    elif choice==6:

        try:
            en=input('Enter Roll No.Of Record To Be Modified:')
            query="select * from "  '\n'+tablename+ '\n' " where rollno=%s"%(en,)
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if  c ==  -1 :
                print('roll no',en,'does not exist')
            else:
                mname=myrecord[1]
                mschool=myrecord[2]
                mmaths=myrecord[3]
                meng=myrecord[4]
                mcs=myrecord[5]
                mphy=myrecord[6]
                mchem=myrecord[7]
                print('              ROLLNO :' , myrecord[0])
                print('              NAME :' , myrecord[1])
                print('              SCHOOL:' , myrecord[2])
                print('              mMATHS:' , myrecord[3])
                print('              mENGLISH :' , myrecord[4])
                print('              mCOMPUTER SCIENCE:' , myrecord[5])
                print('              mPHYSICS :' , myrecord[6])
                print('              mCHEMISTRY:' , myrecord[7])
                print('              TOTAL MARKS:' , myrecord[8])
                print('              AGGREGATE %:' , myrecord[9])
                print('_'*95)
                print('type value to modify or else simply strike enter for no change!!!')
                print('_'*95)
                x=input('enter NAME:')
                if len(x)>0:
                    mname=x
                x=input('enter SCHOOL:')
                if len(x)>0:
                    mschool=x
                x=input('enter MATHS MARKS:')
                if len(x)>0:
                    mmaths=float(x)
                x=input('enter ENG MARKS:')
                if len(x)>0:
                    meng=float(x)
                x=input('enter CS MARKS:')
                if len(x)>0:
                    mcs=float(x)
                x=input('enter PHY MARKS:')
                if len(x)>0:
                    mphy=float(x)
                x=input('enter CHEMISTRY MARKS:')
                if len(x)>0:
                    mchem=float(x)
                mtotal=mmaths+meng+mcs+mphy+mchem
                mnet=mtotal/5
                query=("update result set name='%s' ,school='%s'   ,maths=%s   , english=%s , computerscience=%s ,physics=%s , chemistry=%s,totalmarks=%s, percentage=%s where rollno=%s" %(mname,mschool,mmaths,meng, mcs, mphy, mchem ,mtotal,mnet,en, ))
                
                mycursor.execute(query)
                mydb.commit()
                print('record modified')
        except Exception as e :
            print('something wrong',e)

 
    elif choice==7:
        try:
            query="SELECT * FROM "+tablename
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print('\n\n\n')
            print("-"*95)
            print('\t\t\t\t\t FINAL RESULTS')
            print("-"*95)
            now = datetime.datetime.now()
            print("Current Date and Time :",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            print()
            print(150*'*')
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s %-8s' \
                  %('Rollno' , 'Name' , 'School' , 'mMATHS' ,'mENG' ,'mCS' , 'mPHY' , 'mCHEM' , 'Total Marks' , 'Aggregate %'))
            print('*'*150)
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %9.2f %8.2f %9.2f %8.2f %9.2f '%rec)
            print('*'*150)
        except Exception as e:
            print('something went wrong.........',e)

    elif choice==8:
        try:

            en=input('ENTER ROLL NUMBER WHOSE RESULT IS TO BE GENERATED:')
            print('\n\n\n')
            print("-"*95)
            print('\t\t\t\t\t FINAL RESULTS')
            print("-"*95)
            now = datetime.datetime.now()
            print("Current Date and Time :",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            print()
            print(150*'*')
            query="select * from "  '\n'+tablename+ '\n' " where rollno=%s"%(en,)
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if  c ==  -1 :
                print('roll no',en,'does not exist')
            else:
                mname=myrecord[1]
                mschool=myrecord[2]
                mmaths=myrecord[3]
                meng=myrecord[4]
                mcs=myrecord[5]
                mphy=myrecord[6]
                mchem=myrecord[7]
                print('              ROLLNO :' , myrecord[0])
                print('              NAME :' , myrecord[1])
                print('              SCHOOL:' , myrecord[2])
                print('              mMATHS:' , myrecord[3])
                print('              mENGLISH :' , myrecord[4])
                print('              mCOMPUTER SCIENCE:' , myrecord[5])
                print('              mPHYSICS :' , myrecord[6])
                print('              mCHEMISTRY:' , myrecord[7])
                print('              TOTAL MARKS:' , myrecord[8])
                print('              AGGREGATE %:' , myrecord[9])            
            print('*'*150)
        except Exception as e:
            print('something went wrong.........',e)


    elif choice==9:
        break               
print('thank you for giving your precious time')
                
