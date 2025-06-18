def remove_repeated(li):
    a=[]
    total=0
    for x in li:
        if x not in a:
            a.append(x)
            total=total+x
    return total
n=int(input("Enter the number of elements you want to enter: "))
if n>1:
    my_list=[]
    for i in range(1,n+1):
        num=int(input(f"enter number {i} : "))
        my_list.append(num)
    result=remove_repeated(my_list)
    print(f" the sum of unique elements in the list are: {result}")