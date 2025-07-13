import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kadeeja@123",
    database="task1"
)
my_cursor=mydb.cursor()
# creating database
my_cursor.execute("create database task1")

# creating table
my_cursor.execute("create table student (std_id int primary key,s_name varchar(50),age int)")

# inserting values
my_cursor.execute("insert into student (std_id,s_name,age) values (1,'kadeeja',21)")
mydb.commit()

# inserting user values
a=input("enter student id: ")
b=input("enter  student name: ")
c=input("enter age : ")
query="insert into student(std_id,s_name,age) values(%s,%s,%s)"
value=(a,b,c)
my_cursor.execute(query,value)
mydb.commit()

# selecting
my_cursor.execute("select * from student ")
result=my_cursor.fetchone()
print(result)
# # pip install mysql-connector-python