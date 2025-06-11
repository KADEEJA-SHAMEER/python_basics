def circle(rad):
    return 3.14*(rad*rad)
def rectangle(h,w):
    return h*w
def square(s):
    return s*s

choice=True
while choice:
    ch=int(input("1.Find the area of circle \n2.Find the area of rectangle \n3.Find area of square."
                 "\n0.Exit.\n Enter your choice: "))
    if ch==1:
        r=float(input("enter the circle radius: "))
        result=circle(r)
        print(f"area of circle with radius {r} is : {result}")
    elif ch==2:
        l=float(input("enter the length of rectangle: "))
        b=float(input("enter the breadth of rectangle: "))
        result=rectangle(l,b)
        print(f"area of rectangle with length: {l} and breadth: {b} is : {result}")
    elif ch==3:
        l=float(input("enter the length of square: "))
        result=square(l)
        print(f"area of square with length {l} is : {result}")
    elif ch==0:
        choice=False
        print("exiting....")
    else:
        print("invalid entry")




