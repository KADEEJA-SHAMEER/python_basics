print("enter 0 to stop")
choice=True
my_list=[]
my_list2=[]
while choice:
    num=int(input("enter the number: "))
    if num==0:
        break
    my_list.append(num)
for i in my_list:
    if i%2==0:
        my_list2.append(i)
print(f"The list is {my_list}")
print(f"even numbers from the above list is :{my_list2}")