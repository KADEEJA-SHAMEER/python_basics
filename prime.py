a=int(input("enter a number: "))
c=0
n=(int(a/2)+1)
for i in range(2,n):
    if a%i==0:
       c=c+1
if c>0:
    print("not a prime number")
else:
    print( "a prime number")