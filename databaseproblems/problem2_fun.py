import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",

    user="root",
    password="Kadeeja@123",
    database="task1"
)
def insert():
    name = input("enter your name: ")
    course = input("enter your course: ")
    department = input("enter your department: ")
    phone_no = input("enter your phone number: ")
    email = input("enter your email id: ")
    query = "insert into stud(std_name,course,department,std_phno,email) values (%s,%s,%s,%s,%s)"
    value = (name, course, department, phone_no, email)
    my_cursor.execute(query, value)
    mydb.commit()
    stud_id = my_cursor.lastrowid
    print(f"Data inserted successfully , your id is {stud_id}")
def delete():
    Id = int(input("Enter your id: "))
    query = "delete from stud where std_id=%s"
    my_cursor.execute(query, (Id,))
    mydb.commit()
    if my_cursor.rowcount == 0:
        print(f"No record found with ID: {Id}")
    else:
        print(f"data deleted for the student id: {Id}")
def update():
    ch = int(input(
        "what do you want to update \n1.name \n2.course \n3.department \n4.phone number\n5.Email \nEnter your choice: "))
    Id = int(input("enter your id: "))

    if ch == 1:
        name = input("enter new name: ")
        my_cursor.execute("update stud set std_name=%s where std_id=%s", (name, Id))
        mydb.commit()
        if my_cursor.rowcount == 0:
            print(f"No record found with ID: {Id}")
        else:
            print(f"name updated for the student of id :{Id}")

    elif ch == 2:
        course = input("enter new course: ")
        my_cursor.execute("update stud set course=%s where std_id=%s", (course, Id))
        mydb.commit()
        if my_cursor.rowcount == 0:
            print(f"No record found with ID: {Id}")
        else:
            print(f"course updated for the student of id :{Id}")

    elif ch == 3:
        department = input("enter new department: ")
        my_cursor.execute("update stud set department=%s where std_id=%s", (department, Id))
        mydb.commit()
        if my_cursor.rowcount == 0:
            print(f"No record found with ID: {Id}")
        else:
            print(f"Department updated for the student of id :{Id}")
    elif ch == 4:
        phno = input("enter new phone number: ")
        my_cursor.execute("update stud set std_phno=%s where std_id=%s", (phno, Id))
        mydb.commit()
        if my_cursor.rowcount == 0:
            print(f"No record found with ID: {Id}")
        else:
            print(f"Phone number updated for the student of id :{Id}")

    elif ch == 5:
        email = input("enter new email: ")
        my_cursor.execute("update stud set email=%s where std_id=%s", (email, Id))
        mydb.commit()
        if my_cursor.rowcount == 0:
            print(f"No record found with ID: {Id}")
        else:
            print(f"Email updated for the student of id :{Id}")

    else:
        print("invalid entry")

def fetch():
    Id = int(input("enter your id: "))
    my_cursor.execute("select * from stud where std_id=%s", (Id,))
    result = my_cursor.fetchall()
    if my_cursor.rowcount == 0:
        print(f"No record found with ID: {Id}")
    else:
        print(f" Student data for Id :{Id}\n {result}")

my_cursor=mydb.cursor()
while True:
    choice=int(input("1. insert data \n2. delete data \n3. update data\n4. fetch data\n5. exit \nenter your choice:"))
    if choice==1:
        insert()
    elif choice==2:
        delete()
    elif choice==3:
        update()
    elif choice==4:
        fetch()
    elif choice==5:
        print("exiting.....")
    else:
        print("invalid entry")

