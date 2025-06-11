def nearelement(li,num):
    li.sort()
    l=len(li)
    for j in range(0,l):
        if li[j]>=num:
            targ=li[j-1]
            break
    return targ
n=int(input("enter the number of elements you want to enter: "))
my_list=[]
if n>1:
    for i in range(0,n):
       num=int(input(f"enter number {i+1} : "))
       my_list.append(num)
    target=int(input("enter the target: "))
    nearest=nearelement(my_list,target)
    print(f"Nearest element to {target} is: {nearest}")