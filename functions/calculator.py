def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("division by zero not possible")
        return 0
    else:
        return a/b
def mod(a,b):
    if b==0:
        print("division by zero not possible")
        return 0
    else:
        return a%b
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
op=input("enter an operator: ")
if op=="+":
    result=add(a,b)
    print(f"sum of {a},{b} is {result}")
elif op=="-":
    result = sub(a, b)
    print(f"difference of {a},{b} is {result}")
elif op=="*":
    result = mul(a, b)
    print(f"product of {a},{b} is {result}")
elif op=="/":
    result = div(a, b)
    print(f"division of {a},{b} is {result}")
elif op=="%":
    result = mod(a, b)
    print(f"reminder of {a} divided by {b} is {result}")
else:
    print("invalid operator")