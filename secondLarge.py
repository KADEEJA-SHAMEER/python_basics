n=int(input("enter the number of elements you want to enter: "))
my_tuple=()
my_list=list(my_tuple)
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
    my_tuple = tuple(my_list)
    large = my_tuple[0]
    secLarge=0
    for i in range(1, n):
        if my_tuple[i] >large:
            secLarge=large
            large = my_tuple[i]
        elif my_tuple[i]>secLarge and my_tuple[i]!=large:
            secLarge=my_tuple[i]
        else:
            continue
    print(f"the second largest element is : {secLarge}")