import socket
import json
from time import sleep

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
            response = s.recv(100000)
            print(json.loads(response))
            """
            all_data.append(json.loads(response))
            
            split_list = [i.split() for i in all_data]
            print(all_data)
            print(len(split_list))
            
            for i in range(len(all_data)):
                if i % 2 == 0:
                    raindata.append(all_data[i])
                else:
                    tempreturedata.append(all_data[i])
        print("tempreturedata\raindata")
        for t, p in zip(tempreturedata, raindata):
            print(t, "\t\t", p)
"""
           
        else:
            print("Not a valid command")

    # with conn:
    #     print("Connected:", addr)
    #     while True:
    #         data = conn.recv(1024)
    #         print(json.loads(data))
