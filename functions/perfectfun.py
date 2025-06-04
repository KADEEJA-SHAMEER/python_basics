def perfect(num):
    total=0
    for i in range(1,num):
        if num%i==0:
            total+=i
    return total
num=int(input("enter a number: "))
Sum=perfect(num)
if Sum==num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")

