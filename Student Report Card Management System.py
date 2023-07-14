import mysql.connector 
from prettytable import PrettyTable

# global variable for report
school_name ='Amrita School of Engineering'
school_address ='337/1 A, Valla RCK Nagar, SH 50A, Vengal Village, Tamil nadu'
school_email = 'info@ch.amrita.edu'
school_phone ='044-27602165'

def clear():
  for _ in range(65):
     print()

def add_student():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    clear()
    print('Add New Student Screen')
    print('-'*120)
    name = input('Enter student Name : ')
    fname = input('Enter student Father Name  : ')
    clas = input('Enter student Class : ')
    section = input('Enter student section : ')
    sql ='insert into student(name,fname,class,section,status) values (" '+name+' "," '+fname+' "," '+clas+' "," '+section+' ","active");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Student added successfully.....')
    wait=input('\n\n\nPress Enter to continue...')

def add_marks():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    clear()
    print('Add New marks Screen')
    print('-'*120)
    admno = input('Enter admission NO :')
    term = input('Enter TERM Name : ')
    session = input('Enter session  : ')
    dbms = input('Enter marks in Data Base Management System : ')
    python = input('Enter marks in Python : ')
    java = input('Enter marks in Java : ')
    eng = input('Enter marks in English : ')
    comp = input('Enter marks in Computer Systems and Essentials : ')
    sql = 'insert into marks(admno,term,session,dbms,python,java,eng,comp) values (' + \
        admno+',"'+term+'","'+session+'",'+dbms+','+python+','+java+','+eng+','+comp+');'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Marks added successfully.....')
    wait = input('\n\n\nPress Enter to continue...')

def modify_student():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    clear()
    print('Modify Student Information - Screen')
    print('-'*120)
    admno = input('Enter admission No :')
    print('\n1.   Name  ')
    print('\n2.   Father Name  ')
    print('\n3.   Class  ')
    print('\n4.   Section  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice ==1:
       field ='name' 
    if choice == 2:
       field = 'fname'
    if choice == 3:
       field = 'class'
    if choice == 4:
       field = 'section'
    value =input('Enter new value :')   
    sql ='update student set '+field+' ="'+value +'" where admno ='+admno+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Student Record Updated.....')
    wait = input('\n\n\nPress Enter to continue......')

def modify_marks():
    conn = mysql.connector.connect(
        host='localhost', database='report_card',port='3306',  user='root', password='mysql@1111')
    cursor = conn.cursor()
    clear()
    print('Modify Marks - Screen')
    print('-'*120)
    admno = input('Enter admission No :')
    term = input('Enter Term  :')
    session = input('Enter Session  :')
    print('\n1.   Data Base Management System  ')
    print('\n2.   Python  ')
    print('\n3.   Java  ')
    print('\n4.   English  ')
    print('\n5.   Computer System and Essentials  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
       field = 'dbms'
    if choice == 2:
       field = 'python'
    if choice == 3:
       field = 'java'
    if choice == 4:
       field = 'eng'
    if choice == 5:
       field = 'comp'

    value = input('Enter new value :')
    sql = 'update marks set '+field+' ='+value + ' where admno ='+admno+' AND term="'+term+'" AND session="'+session+'";'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Marks Updated.....')
    wait = input('\n\n\nPress Enter to continue......')

def search_student(field):
  conn = mysql.connector.connect(
      host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
  cursor = conn.cursor()
  sql ='select * from student where '
  msg ='Enter '+field +' :'
  value = input(msg)
  if field=='admno':
     sql = sql + field +'=' +value+';'
  else:
     sql = sql + field +' like "%'+value+'%" or fname like "%'+value +'%";'
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Search Result for '+field+' : '+value)
  print('-'*120)
  for record in records:
     print(record)
  conn.close()
  wait = input('\n\n\n Press Enter to continue.....')

def search_marks():
    conn = mysql.connector.connect(
      host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    admno = input('Enter admission No :')
    session = input('Enter Session  :')
    sql ='select * from marks where admno = '+admno + ' and session ="'+session+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for Admission No :'+admno +' Session : '+session)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press Enter to continue.....')

def search_menu():
    while True:
      clear()
      print(' S E A R C H    M E N U')
      print('-'*120)
      print("\n1.  Admission No")
      print('\n2.  Name / Father Name')
      print('\n3.  Student Term Marks')
      print('\n4.  back to main')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field=''
      if choice == 1:
        field='admno'
        search_student(field)
      if choice == 2:
        field='name'
        search_student(field)
      if choice == 3:
        search_marks()
      if choice == 4:
        break

def report_single_term(): 
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    admno = input('Enter admission No :')
    session = input('Enter Session  :')
    term = input('Enter term  :')
    sql ='select s.admno,name,fname,dbms,java,python,eng,comp from  \
          student s,marks m  where s.admno = m.admno and s.admno = '+admno +' and m.session = "'+session+'" and m.term ="'+term+'";'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :',school_phone ,' Email :', school_email)
    print('-'*120)
    print('Admno :',record[0],' Name :',record[1], '   Father Name :',record[2])
    print('Session :', session, ' Term :', term)
    print('-'*120)
    print('Subject',' Max_marks','min-marks','marks obtained')
    print('Data Base Management System','100','33',record[3])
    print('Python','100','33',record[4])
    print('Java','100','33',record[5])
    print('English','100','33',record[6])
    print('Computer System and Essentials','100','33',record[7])
    print('-'*120)
    total = record[3]+record[4]+record[5]+record[6]+record[7]
    percentage = total*100/500
    print('Total Marks : ',total,'Percentage Marks :',percentage)
    conn.close()
    wait = input('\n\n\n Press Enter to continue.....')

def report_whole_class(): 
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    clas = input('Enter Class :')
    section =input ('Enter section :')
    session = input('Enter Session  :')
    term = input('Enter term  :')
    sql ='select s.admno,name,fname,dbms,java,python,eng,comp from  \
          student s, marks m  where s.admno = m.admno  AND s.class="'+clas+'" AND s.section ="'+section +'" and m.session = "'+session+'" and m.term ="'+term+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :',school_phone ,' Email :', school_email)
    print('-'*120)
    print('Class Wise Report Card:',clas,'-',section, 'Session : ',session, ' Term :',term)
    print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name', 'dbms', 'python', 'java','Eng','Comp','Total'])
    for idr, name, fname, dbms,python,java,eng,comp in records:
      total = dbms+python+java+eng+comp
      t.add_row([idr, name, fname, dbms, python, java, eng, comp,total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press Enter to continue.....')


def report_whole_session():
    conn = mysql.connector.connect(
        host='localhost', database='report_card',port='3306',  user='root', password='mysql@1111')
    cursor = conn.cursor()
    session = input('Enter Session  :')
    sql = 'select s.admno,name,fname,class, section,term,dbms,java,python,eng,comp from  \
          student s, marks m  where s.admno = m.admno  and m.session = "'+session+'" ORDER BY class,section,term;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :', school_phone, ' Email :', school_email,'\n\n')

    print('Whole Session Report Card:', '           Session : ', session)
    print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name','Class','section','Term', 'dbms',
                     'python', 'java', 'Eng', 'Comp', 'Total'])
    for idr, name, fname,clas1,section, term, dbms, python, java, eng, comp in records:
      total = dbms+python+java+eng+comp
      t.add_row([idr, name, fname,clas1, section, term, dbms, python, java, eng, comp, total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press Enter to continue.....')


def report_topper_list():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', port='3306', user='root', password='mysql@1111')
    cursor = conn.cursor()
    session = input('Enter Session  :')
    term = input('Enter Term :')
    clas= input('Enter class  :')
    section= input('Enter section  :')
    sql = 'select s.admno, name, fname,dbms,python,java,eng,comp, dbms+python+java+eng+comp "Total" from student s, marks m \
           where s.admno = m.admno and class = "'+clas+'" and section = "'+section+'" and session ="'+session+'" and term="'+term+'" order by total Desc;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :', school_phone, ' Email :', school_email, '\n\n')

    print('T O P P E R S    L I S T \n\n Class :',clas,'           Session : ', session, ' Term :',term)
    #print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name', 'dbms', 'python', 'java','English','Computer', 'Total'])
    for idr, name, fname, dbms, python, java, eng, comp, total in records:
        t.add_row([idr, name, fname, dbms, python, java, eng, comp,total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press Enter to continue.....')


def report_menu():
    while True:
      clear()
      print(' R E P O R T   M E N U ')
      print("\n1.  Single Term report card")
      print('\n2.  Whole class report card')
      print('\n3.  Whole Session report Card ')
      print('\n4.  Class Wise- Toppers')
      print('\n5.  Back to main menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        report_single_term()
      if choice == 2:
        report_whole_class()
      if choice == 3:
        report_whole_session()
      if choice == 4:
        report_topper_list()
      if choice == 5:
        break



def main_menu():
    while True:
      clear()
      print(' R E P O R T   C A R D   M E N U  ')
      print("\n1.  Add Student")
      print('\n2.  Modify Student Record')
      print('\n3.  Add marks')
      print('\n4.  Modify Marks')
      print('\n5.  Search Menu')
      print('\n6.  Report Menu')
      print('\n7.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_student()
      if choice == 2:
        modify_student()
      if choice == 3:
        add_marks()
      if choice == 4:
        modify_marks()
      if choice == 5:
        search_menu()
      if choice == 6:
        report_menu()
      if choice == 7:
        break


if __name__ == "__main__":
    main_menu()

