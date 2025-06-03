n=input("enter the number of elements you want to enter: ")
my_list=[]
my_list2=[]
count=0
if int(n)>1:
    for i in range(1,int(n)+1):
       num=input(f"enter value {i} : ")
       if num not in my_list:
            count=count+1
       my_list.append(num)
    print(f"The count of unique value is : {count}")