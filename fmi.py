import socket
from time import sleep
import pickle

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12342
all_data = []
tempreturedata = []
raindata = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
command = ''
s.connect((HOST, PORT))


def view_forecast():
    s.send(command.encode("utf-8"))
    response = s.recv(1024)
        
    for i in range(len(pickle.loads(response))):
        if i % 2 == 0:
            tempreturedata.append(pickle.loads(response)[i])
        else:
            raindata.append(pickle.loads(response)[i])
              
while True:
    command = input("Available commands:\n1. 'all' - Returns all data\n3. 'current' returns newest data\n2. 'exit' - Exits CLI\nCommand: ")
    if command == "all":
        view_forecast()
        print("tempreturedata\traindata")
        for t, p in zip(tempreturedata, raindata):
            print(t, "\t\t", p)
            tempreturedata = []
            raindata = []


    elif command == "current":
        view_forecast()
        print(f"Here you have the newest forecast: < {tempreturedata[-1]}  celsius > and < {raindata[-1]} mm > of rain.")
        tempreturedata = []
        raindata = []

        
    elif command == "exit":
        print("hope you liked it bye")
        break

    elif command != "current" or "all":
        print("Not a command")


