num_patients=int(input("enter the number of patients : "))
if num_patients<=20:
    my_list=[]
    total_earning=0
    i=1
    while i<=num_patients:
        age=int(input(f"enter the age of patient {i} : "))
        if age>0 and (age<=120):
            my_list.append(age)
            i=i+1
        else:
            print("re enter a value greater than 0 and less than 120")
            continue
    for age in my_list:
        if age<17:
            total_earning+=200
        elif (age>=17) and age<=40:
            total_earning+=400
        else:
            total_earning+=300
    print("total earnings of the day : ",total_earning)
else:
    print("maximum 20 patients are allowed a day")


