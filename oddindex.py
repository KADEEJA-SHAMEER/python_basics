n=int(input("enter the number of elements you want to enter: "))
my_list=[]
Sum=0
if n>1:
    for i in range(0,n):
       num=int(input(f"enter number {i+1} : "))
       my_list.append(num)
       if i%2!=0:
           if num%2==0:
               Sum=Sum+num
    print("sum of even numbers in the odd index is: ",Sum)