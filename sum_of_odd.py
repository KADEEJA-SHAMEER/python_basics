n=int(input("enter the number of elements you want to enter: "))
my_list=[]
Sum=0
if n>1:
    for i in range(1,n+1):
       num=int(input(f"enter number {i} : "))
       my_list.append(num)
       if num%2==0 and num%3==0:
           continue
       else:
           Sum+=num
    print(f"sum of elements except even numbers which is divisible by 3: {Sum}")

