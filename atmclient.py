import socket
import random
import time

def client_prog():
    HOST = '10.33.3.25'
    PORT = 6060
    FORMAT='utf-8'

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    userID = input("Enter your card ID\n-> ")
    password = input("Enter your passcode\n-> ")
    client.send(userID.encode(FORMAT))
    client.send(password.encode(FORMAT))
    response=client.recv(1024).decode(FORMAT)
    error_rate=0
    if response=="FALSE":
        print(f"Your provided information is invalid.")
    else:
        print(f"Logged in!")
        cnt = 0 
        time_in = time.time()
        file = open('client_time','a')

        while True:
            if cnt == 100 :
                time_diff = time.time()-time_in
                file.write(f"10 {time_diff}\n") 
            # option = input("Which action would you like to perform?\nEnter 1 for Balance Inquiry\nEnter 2 for Withdrawal\nEnter 3 for Deposit\n->")
            option=str(random.randint(1,3))
            print(option)
            client.send(option.encode(FORMAT))

            if option=="1":
                while True:
                    balance=client.recv(1024).decode(FORMAT)
                    randomnum=random.randint(1,10)
                    if randomnum>0 and randomnum<10-error_rate:
                        client.send("YES".encode(FORMAT))
                        print(f"Your balance is {balance} BDT")
                        cnt = cnt + 1
                        break
                    else:
                        client.send("NO".encode(FORMAT))
            if option=="3":
                # deposit_amount=input("Enter the amount you want to deposit.\n->") 
                deposit_amount = str(random.randint(100,10000))
                client.send(deposit_amount.encode(FORMAT))
                while True:
                    res=client.recv(1024).decode(FORMAT)
                    randomnum=random.randint(1,10)
                    if randomnum>0 and randomnum<10-error_rate:
                        client.send("YES".encode(FORMAT))
                        print(f"{deposit_amount} BDT has been deposited. Your new balance is {res} BDT.\n")  
                        cnt = cnt + 1
                        break
                    else:
                        client.send("NO".encode(FORMAT))
            if option=="2":
                # withdraw_amount=input("Enter the amount you want to withdraw.\n-> ")
                withdraw_amount = str(random.randint(100,10000))
                client.send(withdraw_amount.encode(FORMAT))
                while True:
                    validity=client.recv(1024).decode(FORMAT)
                    randomnum=random.randint(1,10)
                    if randomnum>0 and randomnum<10-error_rate:
                        client.send("YES".encode(FORMAT))
                        if validity=="FALSE":
                            print(f"Not enough balance :(")
                            cnt = cnt + 1
                            break
                        else:
                            print(f"{withdraw_amount} BDT has been withdrawn.\nYour new balance is {validity} BDT\n") 
                            cnt = cnt + 1 
                            break
                    else:
                        client.send("NO".encode(FORMAT))
            # cont=input("Do you want to continue?\nEnter 1 to continue\nEnter 2 to exit\n->")
           
            # client.send(cont.encode(FORMAT))
            # if cont=="2":
            #     print("Thank you for banking with us.\n")
            #     break       


if __name__ == '__main__':
    client_prog()
