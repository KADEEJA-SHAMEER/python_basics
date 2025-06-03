n=input("enter the number of elements you want to enter: ")
my_list=[]
my_list2=[]
if int(n)>1:
    for i in range(1,int(n)+1):
       num=input(f"enter value {i} : ")
       my_list.append(num)
    for i in my_list:
        if i not in my_list2:
            my_list2.append(i)
    print(my_list2)