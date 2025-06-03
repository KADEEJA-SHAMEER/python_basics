n=int(input("enter the number of elements you want to enter: "))
my_tuple=()
my_list=list(my_tuple)
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
    for i in range(0,n):
        if my_list[i]%7==0:
            my_list[i]="%"
        elif my_list[i]%2==0:
            my_list[i]="@"
        else:
            continue
    my_tuple=tuple(my_list)
    print(my_tuple)
