def prime(num):
    if num < 2:
        return False
    a = int(num ** 0.5) + 1
    for i in range(2, a):
        if num % i == 0:
            return False
    return True
n=int(input("enter the number of elements you want to enter: "))
my_list=[]
Sum=0
if n>1:
    for i in range(0,n):
       num=int(input(f"enter number {i+1} : "))
       my_list.append(num)
       if i%2==0:
           isprime=prime(num)
           if isprime:
               Sum=Sum+num
    f=open("sum_prime.txt","w")
    f.write(f"{Sum}")
    f.close()
    print("sum of prime numbers in the odd index is: ",Sum)
# f=open("demo1.txt","r")
# print(f.read())
# f.close()
