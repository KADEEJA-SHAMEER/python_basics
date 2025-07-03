n=int(input("enter the number: "))
i=1
while i<=n:
    if i%2!=0:
        print("* "*(i*2))
    else:
        print("* "*i)
    i=i+1
