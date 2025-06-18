def prime(li):
    total=0
    l=len(li)
    for x in range(0,l):
        if x%2!=0:
            isprime=True
            a = int(li[x] ** 0.5) + 1
            for j in range(2, a):
              if li[x] % j == 0:
                  isprime=False
                  break
            if isprime:
                total+=li[x]
    return total
n=int(input("enter the number of elements you want to enter: "))
my_list=[]
if n>1:
    for i in range(0,n):
       num=int(input(f"enter number {i+1} : "))
       my_list.append(num)
       Sum=prime(my_list)
print("sum of prime numbers in the odd index is: ",Sum)