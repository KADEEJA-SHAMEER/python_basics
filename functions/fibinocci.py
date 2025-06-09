def fibonacci(num):
    if num==1:
        return [0]
    elif num==2:
        return [0,1]
    else:
        a=0
        b=1
        my_list=[0,1]
        for i in range(3,num+1):
            c=a+b
            a=b
            b=c
            my_list.append(c)
        return my_list
n=int(input("enter the number of elements: "))
if n>0:
    result = fibonacci(n)
    print(f"The first {n} fibonacci numbers are : {result}")
else:
    print("please enter a number greater than zero")