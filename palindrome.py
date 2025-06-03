# n=int(input("enter a number: "))
# x=n
# total=0
# while n>0:
#     r=n%10
#     total=total*10+r
#     n=int(n/10)
# if x==total:
#     print(f"{x} is palindrome")
# else:
#     print(f"{x} is not a palindrome")
n=input("enter the number: ")
x=n[::-1]
if x==n:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")