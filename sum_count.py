print("enter 0 to stop")
choice=True
my_list=[]
Sum=0
c=0
while choice:
    num=int(input("enter the number: "))
    if num==0:
        break
    my_list.append(num)
    Sum+=num
    c=c+1
print(f"The entered numbers are {my_list}")
print("Sum of the numbers is: ",Sum)
print("the count of numbers is: ",c)
