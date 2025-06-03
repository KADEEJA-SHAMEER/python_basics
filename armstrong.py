# n = int(input("enter a number: "))
# x=n
# Sum=0
# while n>0:
#     r = int(n%10)
#     Sum=Sum+(r*r*r)
#     n=int(n/10)
# if Sum==x:
#     print(f"{x} is an armstrong number")
# else:
#     print(f"{x} is not an armstrong number")
n=input("enter the number: ")
total=0
for i in n:
    total=total+(int(i)**3)
if total==int(n):
    print(f"{n} is an armstrong number")
else:
     print(f"{n} is not an armstrong number")