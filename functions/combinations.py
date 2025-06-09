def combinations(num):
    if num==1:
        return 1
    else:
        result=num*combinations(num-1)
    return result
n=int(input("enter the total number: "))
r=int(input("enter the number items you want to choose: "))
n_fact=combinations(n)
r_fact=combinations(r)
nr_fact=combinations(n-r)
nCr=int(n_fact/(r_fact*nr_fact))
print(f"number of combinations: {nCr}")

