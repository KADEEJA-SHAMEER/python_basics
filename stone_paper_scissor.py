import random
s=random.randint(1,3)
system=""
user=""
if s==1:
    system="stone"
elif s==2:
    system="paper"
elif s==3:
    system="Scissor"
ch=int(input("1.stone \n2.paper \n3.scissor \nenter your choice: "))
if ch==1:
    user="stone"
elif ch==2:
    user="paper"
elif ch==3:
    user="Scissor"
print(f"System:{system} v/s You:{user}")
if ch==s:
    print("It is a tie!!!")
elif ch==1 and s==2:
    print("System wins!!")
elif ch==1 and s==3:
    print("You wins!!")
elif ch==2 and s==1:
    print("You wins!!")
elif ch==2 and s==3:
    print("System wins!!")
elif ch==3 and s==1:
    print("system wins!!")
elif ch==3 and s==2:
    print("You wins!!")
else:
    print("invalid choice")