# n=int(input("enter the number: "))
# i=2
# print("*")
# while i<=n:
#     a = (int(i / 2) + 1)
#     c = 0
#     for x in range(2, a):
#         if i%x==0:
#             c=c+1
#     if c==0:
#         print("* "*(i+1))
#     else:
#         print("* "*i)
#     i=i+1
n=int(input("enter the number: "))
if n>=1:
    i=2
    print("*")
    while i<=n:
        a = (int(i / 2) + 1)
        isprime=True
        for x in range(2, a):
            if i%x==0:
                isprime=False
                break
        if isprime:
            print("* "*(i+1))
        else:
            print("* "*i)
        i=i+1