import socket
def client_prog():
    HOST = '10.33.3.25'
    PORT=7070
    FORMAT='utf-8'

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    message = input("Enter PRI for prime check \nEnter PAL for palindrome check\n-> ")
    client.send(message.encode(FORMAT))

    if message=="PRI":
        inputtxt = input("Enter a number\n-> ")
    else:
        inputtxt = input("Enter a string\n-> ")

    client.send(inputtxt.encode(FORMAT))
    response=client.recv(1024).decode(FORMAT)
    print(response)
    # if response=="YES":
    #     if message=="PRI":
    #         print(f"The number is prime.")
    #     else:
    #         print(f"The input is a palindrome.")
    # else:
    #     if message=="PRI":
    #         print(f"The number is not prime.")
    #     else:
    #         print(f"The input is not a palindrome.")
       

if __name__ == '__main__':
    client_prog()
