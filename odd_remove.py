n=int(input("enter the number of elements you want to enter: "))
my_list=[]
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
    for i in range(0,n):
        if my_list[i]%2!=0:
            my_list[i]="&"
    print(my_list[::-1])