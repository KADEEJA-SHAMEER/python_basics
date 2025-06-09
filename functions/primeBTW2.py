def prime(num):
    if num<2:
        return False
    a=int(num ** 0.5)+1
    for i in range(2,a):
        if num%i==0:
           return False
    return True
def check(m1,m2):
    prime_nums=[]
    isprime=True
    for i in range(m1,m2+1):
        isprime=prime(i)
        if isprime:
            prime_nums.append(i)
    return prime_nums
n1=int(input("enter the starting number: "))
n2=int(input("enter the ending number: "))
result=check(n1,n2)
print(f"prime numbers between {n1} and {n2} is :{result}")
