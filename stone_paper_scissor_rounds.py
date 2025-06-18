import random
system=0
user=0
s=0
ch=0
i = 1
while True:
    print(f"!! Round {i} !!")
    game={1:'stone',2:"paper",3:"scissor"}
    s=random.randint(1,3)
    ch = int(input("\n1.stone \n2.paper \n3.scissor \nenter your choice: "))
    if ch not in game:
        print("invalid entry")
    else:
        print(f"{game[s]} v\\s {game[ch]}")
        if s==ch:
            print("\nIts a tie!!")
        elif (ch==1 and s==2) or (ch==2 and s==3) or (ch==3 and s==1):
            print(f"\nSystem wins Round {i}!!")
            system+=1
        elif (ch==1 and s==3) or (ch==2 and s==1) or (ch==3 and s==2):
            print(f"\nYou wins Round {i}!!")
            user+=1
        else:
            print("invalid choice")
    c=input("\n Do you want to play another round(y/n): ")
    if c=='y' or c=='Y':
        i=i+1
        continue
    elif c=='n'or c=='N':
        break
    else:
        print("invalid entry")
print(f"System have {system} points &&& you have {user} points")
if system==user:
    print("Its a tie!!")
elif system>user:
    print("System wins the game!!")
else:
    print("You wins the game!!")