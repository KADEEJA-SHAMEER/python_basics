import os
file_name=input("enter the file name with .txt: ")
f=open(file_name,"a")
print("file created successfully")
choice=True
while choice:
    ch=int(input("1.To add data \n2.To read \n3.To delete file."
                 "\n4.To overwrite data \n0.Exit.\n Enter your choice: "))
    if ch==1:
        name=input("enter name: ")
        age=input("enter age: ")
        email=input("enter email: ")
        f.write(f"Name:{name},email:{email},Age:{age}")
        print("data added successfully")
    elif ch==2:
        f=open(file_name,"r")
        c=int(input("do you want to read line or words(1/0"))
        if c==1:
            n=int(input("enter the number of lines: "))
            for i in range(1,n+1):
                print(f.readline())
        elif c==0:
            print(f.read())
        else:
            print("invalid option")
    elif ch==3:
        f.close()
        os.remove(file_name)
        print("file deleted successfully")
        break
    elif ch==4:
        f=open(file_name,"w")
        data=input("enter the data to overwrite: ")
        f.write(data)
        print("data overwritten successfully")
    elif ch==0:
        choice=False
        print("exiting....")
    else:
        print("invalid entry")