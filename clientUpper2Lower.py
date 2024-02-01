import socket

def client_prog():
    HOST = '10.33.3.25'
    PORT=5000
    FORMAT='utf-8'

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    message = input(" -> ")
    client.send(message.encode(FORMAT))
    response=client.recv(1024).decode(FORMAT)
    print(f"After conversion to lowercase: {response}")    

if __name__ == '__main__':
    client_prog()
