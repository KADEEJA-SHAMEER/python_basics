n=int(input("enter the number of rows : "))
i=1
if n>=1:
    while i<=n:
        sqrt_n=int(i**0.5)
        if (sqrt_n*sqrt_n)==i:
            print("* "*(i*2))
        else:
            print("* "*i)
        i=i+1