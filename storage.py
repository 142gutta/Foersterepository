import socket
import json
from time import sleep
import threading
import concurrent.futures
import os

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

        with conn:
            print("CONNECTED:", addr)

            command = conn.recv(1024)
            sent = False
            print("BEFORE WHILE")
            while not sent:
                print("COMMANDSONDASD;", command.decode())
                if command.decode("utf-8") == "all":
                    print("All")
                    if os.path.exists("./data.txt"):
                        print("Exists")
                        with open("data.txt", "r") as f:
                            data = f.readlines()
                            data = [float(i.strip("\n")) if i != None else 0 for i in data]
                            conn.sendall(json.dumps(data).encode("utf-8"))
                            sent = True
                            print(data)
                    else:
                        conn.send(json.dumps("No data is stored").encode())
                command = ""
        

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(receive_and_print_numbers, HOST_RECEIVE, PORT_RECEIVE)
    executor.submit(read_from_file, HOST_SEND, PORT_SEND)

