Len=int(input("enter the number of lines pattern you want: "))
space=Len-1
for i in range(1,Len+1):
      print(" "*space,"* "*i)
      space-=1
