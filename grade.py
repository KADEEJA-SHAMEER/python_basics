a=int(input('enter  your mark out of 100: '))
if a<=100:
     if a>=90:
        print("A")
     elif a>=80:
        print("B")
     elif a>=70:
         print("C")
     elif a>=60:
         print("D")
     else:
         print("F")
else:
    print("invalid entry")