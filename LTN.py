a=int(input("enter  number 1: "))
b=int(input("enter  number 2: "))
c=int(input("enter  number 3: "))
if a>=b:
    if a>=c:
        print(f"{a} is greater")
    else:
        print(f"{c} is greater")
elif b>=c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")


