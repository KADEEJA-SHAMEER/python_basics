n=int(input("enter the number of rows :  "))
if n>=1:
    j=1
    for i in range(1,n+1):
        print("* "*(i*j))
        j=i*j
