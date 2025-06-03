n=int(input("enter the number of elements you want to enter: "))
my_list=[]
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
    print(my_list)
    my_list.sort()
    print(f"larget element is {my_list[n-1]}")