import socket
from time import sleep
import pickle

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12342
all_data = []
tempreturedata = []
raindata = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    command = ''
    s.connect((HOST, PORT))

    while command != "exit":

        command = input("Available commands:\n1. 'all' - Returns all data\n2. 'exit' - Exits CLI\nCommand: ")

        if command == "all":
            s.send(command.encode("utf-8"))
            response = s.recv(1024)
            
            for i in range(len(pickle.loads(response))):
                if i % 2 == 0:
                    tempreturedata.append(pickle.loads(response)[i])
                else:
                    raindata.append(pickle.loads(response)[i])
                    
            print("tempreturedata\traindata")
            for t, p in zip(tempreturedata, raindata):
                print(t, "\t\t", p)
                tempreturedata = []
                raindata = []

        elif command == "current" :

            s.send(command.encode("utf-8"))
            response = s.recv(1024)
            
            for i in range(len(pickle.loads(response))):
                if i % 2 == 0:
                    tempreturedata.append(pickle.loads(response)[i])
                else:
                    raindata.append(pickle.loads(response)[i])
            print(f"Here you have the newest forecast: < {tempreturedata[-1]}  celsius > and < {raindata[-1]} mm > of rain.")
            tempreturedata = []
            raindata = []



           
        else:
            print("Not a valid command")
"""
    # with conn:
    #     print("Connected:", addr)
    #     while True:
    #         data = conn.recv(1024)
    #         print(json.loads(data))
    """
