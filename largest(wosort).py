n=int(input("enter the number of elements you want to enter: "))
my_list=[]
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
    large=my_list[0]
    for i in range(1,n):
        if my_list[i]>=large:
            large=my_list[i]
    print(f"largest element is {large}")
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         if my_list[i]>my_list[j]:
    #             temp=my_list[i]
    #             my_list[i]=my_list[j]
    #             my_list[j]=temp
    # print(my_list)
    # print(f"larget element is {my_list[n-1]}")
else:
    print("enter a number greater than 1")