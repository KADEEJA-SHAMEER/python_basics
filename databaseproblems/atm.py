import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kadeeja@123",
    database="task1"
)

def transaction_history(acc_num,trans_type,amount):
    my_cursor.execute("insert into transaction_history(acc_no,trans_type,amount) values(%s,%s,%s)",(acc_num,trans_type,amount))
    mydb.commit()

my_cursor=mydb.cursor()
my_cursor.execute("select acc_no from bank")
acc_nos=my_cursor.fetchall()
print(acc_nos)
acc_nos = [row[0] for row in acc_nos]
print(acc_nos)

while True:
    choice=int(input("1.withdraw\n2.deposit\n3.check bank balance\n4.Transfer money\n5.See Transaction History\n0.exit\n Enter your choice: "))
    if choice==1:
        acc_no=int(input("enter your account number: "))
        if acc_no in acc_nos:
            amount=int(input("enter the amount you want to withdraw: "))
            my_cursor.execute("select balance from bank where acc_no=%s",(acc_no,))
            balance=my_cursor.fetchone()
            current_balance=balance[0]
            if current_balance>=amount:
                current_balance-=amount
                my_cursor.execute("update bank set balance=%s where acc_no=%s",(current_balance,acc_no))
                mydb.commit()
                transaction_history(acc_no,'withdraw',amount)
                print(f"withdrawal is successful!!!\n Your current account balance is {current_balance}")
            else:
                print("Insufficient Balance\n Withdrawal is not possible" )
        else:
            print("Account not found")

    elif choice==2:
        acc_no = int(input("enter your account number: "))
        if acc_no in acc_nos:
            amount=int(input("Enter the amount you want to deposit: "))
            my_cursor.execute("select balance from bank where acc_no=%s", (acc_no,))
            balance = my_cursor.fetchone()
            current_balance = balance[0]
            current_balance+=amount
            my_cursor.execute("update bank set balance=%s where acc_no=%s", (current_balance, acc_no))
            mydb.commit()
            transaction_history(acc_no, 'deposit', amount)
            print(f"successfully deposited the amount {amount}!!!\n Your current account balance is {current_balance}")
        else:
            print("Account not found")

    elif choice==3:
        acc_no = int(input("enter your account number: "))
        if acc_no in acc_nos:
            my_cursor.execute("select balance from bank where acc_no=%s", (acc_no,))
            balance = my_cursor.fetchone()
            current_balance = balance[0]
            print(f"Your current account balance is {current_balance}")
        else:
            print("Account not found")

    elif choice==4:
        acc_no = int(input("Enter your account number: "))
        rec_acc = int(input("Enter the recipient's account number: "))
        if acc_no in acc_nos:
            if rec_acc in acc_nos:
                amount = int(input("Enter the amount you want to transfer: "))
                my_cursor.execute( "SELECT acc_no, balance FROM bank WHERE acc_no IN (%s, %s)",(acc_no, rec_acc))
                results = my_cursor.fetchall()
                balances = {row[0]: row[1] for row in results}
                if acc_no in balances and rec_acc in balances:
                    if balances[acc_no] >= amount:
                        new_sender_balance = balances[acc_no] - amount
                        new_receiver_balance = balances[rec_acc] + amount
                        my_cursor.execute("UPDATE bank SET balance = %s WHERE acc_no = %s",(new_sender_balance, acc_no))
                        my_cursor.execute( "UPDATE bank SET balance = %s WHERE acc_no = %s",(new_receiver_balance, rec_acc))
                        mydb.commit()
                        transaction_history(acc_no, 'money transfer', amount)
                        print("Transfer successful!")
                        print(f"Your new balance: ₹{new_sender_balance}")
                    else:
                        print("Insufficient funds!")
                else:
                    print("Could not retrieve both account balances.")
            else:
                print("Recipient account not found.")
        else:
            print("Your account number is invalid.")

    elif choice==5:
        acc_no=int(input("enter your account number: "))
        if acc_no in acc_nos:
            my_cursor.execute("select * from transaction_history where acc_no=%s",(acc_no,))
            result=my_cursor.fetchall()
            for row in result:
                acc = row[1]  # acc_no
                tx_type = row[2]  # transaction_type
                amt = row[3]  # amount
                print(f"Account Number: {acc} \n Type of Transaction: {tx_type} \n Amount: ₹{amt}")

    elif choice==0:
        print("exiting......")
        break

    else:
        print("Invalid choice")









    

