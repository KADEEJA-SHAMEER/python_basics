def odd_even(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter a number: "))
flag=odd_even(num)
if flag:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
