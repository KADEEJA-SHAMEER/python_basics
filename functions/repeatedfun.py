def remove_repeated(li):
    a=[]
    for x in li:
        if x not in a:
            a.append(x)
    return a
n=int(input("Enter the number of elements you want to enter: "))
if n>1:
    my_list=[]
    for i in range(1,n+1):
        num=int(input(f"enter number {i} : "))
        my_list.append(num)
    result=remove_repeated(my_list)
    print(f" the unique elements in the list are: {result}")