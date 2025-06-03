n=int(input("enter a  number: "))
Sum=0
for i in range(1,n):
    if n%i==0:
        Sum=Sum+i
if Sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")