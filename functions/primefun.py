def prime(num):
    a=int(num/2)+1
    for i in range(2,a):
        if num%i==0:
           return False
    return True
num=int(input('Enter the number: '))
is_prime=prime(num)
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not prime number")

