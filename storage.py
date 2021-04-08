import socket
import json
from time import sleep
import threading
import concurrent.futures
import os
import pickle
HOST_RECEIVE = socket.gethostbyname(socket.gethostname())
PORT_RECEIVE = 11111

HOST_SEND = socket.gethostbyname(socket.gethostname())
PORT_SEND = 12342


                

def receive_and_print_numbers(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print("UDP SERVER UP AND RUNNING")

        while True:
            data, host = s.recvfrom(1024)
            print(f"Received weatherdata from {host} ")
            with open("./data.txt", "a+") as f:
                f.write(f"{json.loads(data)}\n")



def read_from_file(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()

        while conn:
            print("CONNECTED:", addr)

            command = conn.recv(1024)
            sent = False
            print("BEFORE WHILE")
            while not sent:
                print("COMMANDSONDASD;", command.decode())
                if command.decode("utf-8") == "all" or command.decode("utf-8") == "current":
                    if os.path.exists("./data.txt"):
                        print("Exists")
                        if os.path.getsize("./data.txt") > 0:
                            with open("data.txt", "r") as f:
                                data = f.readlines()
                                data = [float(i.strip("\n")) if i != None else 0 for i in data]
                                print(f"here we have data{data}")
                                Message = pickle.dumps(data)
                                conn.sendto(Message,(HOST_SEND, PORT_SEND))
                                sent = True
                                print(data)
                        else:
                            conn.send(pickle.dumps("No data is stored").encode())
                    command = ""
        

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(receive_and_print_numbers, HOST_RECEIVE, PORT_RECEIVE)
    executor.submit(read_from_file, HOST_SEND, PORT_SEND)

