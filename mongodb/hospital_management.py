import pymongo
from datetime import datetime

my_client=pymongo.MongoClient("mongodb://localhost:27017")
mydb=my_client["Hospital"]

choice=input("Are you a new user or not (y/n): ")
if choice=="y" or choice=="Y":
    mycol = mydb["Registration"]
    count = mycol.count_documents({})
    name = input("enter your name: ")
    age = int(input("Enter your age: "))
    phone_no=int(input("Enter your phone number: "))
    data = {"_id": count + 300, "name": name, "age": age,"phone_no":phone_no}
    x=mycol.insert_one(data)
    print(f"Your ID is: {count+300}. Yu need this id for further operations!!")
    print("WELCOME!!!")

elif choice=="n"or choice=="N":
    print("WELCOME!!!")
else:
    print("invalid entry")
while True:
    ch=int(input("1.Book your Appointments.\n2.View your appointments.\n0.exit\nEnter your choice: "))

    if ch==1:
        user_id=int(input("Enter your id: "))
        Id=mydb['Registration']
        x=Id.find_one({"_id":user_id})
        if x:
            print("\n ....Available departments....")
            my_dep=mydb['department']
            for d in my_dep.find():
                print(f"> ID:{d['_id']} | {d['name']}")
            dep_id=input("Enter th ID of the department you want to visit: ")
            dep_doc = my_dep.find_one({"_id": dep_id})
            if dep_doc:
                department_name = dep_doc['name']
            else:
                print("Invalid department ID.")
                exit()
            doc=mydb['doctor']
            for Doc in doc.find({"dept_id":dep_id}):
                print(f"> {Doc["name"]}")
            doctor=input("Enter the name of the doctor you want to visit: ")
            today=datetime.today()
            mycol=mydb['Booking']
            booking = mycol.count_documents({})

            book={"_id":booking+1,"user_id":user_id,"department":department_name,"doctor":doctor,"date":today}
            y=mycol.insert_one(book)
            print(".....Your booking is successfully completed!!!!....")

    elif ch==2:
        user_id=int(input("enter your id: "))
        mycol = mydb['Registration']
        x = mycol.find_one({"_id": user_id})
        if x:
            book=mydb['Booking']
            for b in book.find({'user_id':user_id}):
                print(f"> ID:{b['user_id']} | {b['department']} |  {b['doctor']}  |  {b['date']}")

    elif ch==0:
        print("exiting........")
        break







