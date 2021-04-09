import socket
import json
from time import sleep
import concurrent.futures
import os
import pickle

HOST_RECEIVE = socket.gethostbyname(socket.gethostname()) #Ip address to recive data
PORT_RECEIVE = 11111#Port to recive

HOST_SEND = socket.gethostbyname(socket.gethostname())#Ip address to send data
PORT_SEND = 12342#Port to send 


                

def receive_and_print_numbers(host, port):
    """opens a UDP socket and binds this connection. Recives data from weather_station and writes
    this into a data.txt file"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:#opens a UDP socket as s
        s.bind((host, port))#Binds host and port
        print("UDP SERVER UP AND RUNNING")#Prints "UPD UP AND RUNNING"

        while True:#infinite whileloop
            data, host = s.recvfrom(1024)#Recives data with UDP socket
            print(f"Received weatherdata from {host} ")#Prints for every packet recived from weather_station
            with open("./data.txt", "a+") as f:#Opens a txt file
                f.write(f"{json.loads(data)}\n")#writes recived data in data.txt



def read_from_file(host, port):
    """Starts a connection with fmi.py thougth a TCP socket. Recives a command/input from fmi.py
    and sends data by reading from data.txt and uses pickle to send the data to fmi.py"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#Opens a TCP socket as s
        s.bind((host, port))#Binds host and port
        s.listen()#Listens for connection
        conn, addr = s.accept()#Accepts connection

        while conn:#While loop that runs as long as there is a connection
            print("CONNECTED:", addr)#Prints "CONNECTED" and the address that is bound to the socket

            command = conn.recv(1024)#Recives command/input from fmi.py
            sent = False
            while not sent:#While loop that runs as long as message is not sent
                if command.decode("utf-8") == "all" or command.decode("utf-8") == "current":#Checks if command is equala to "all" or "current"
                    if os.path.exists("./data.txt"):#Checks if there is a file called data.txt
                        print("Exists")
                        if os.path.getsize("./data.txt") > 0:#Checks if there is something in the data.txt file
                            with open("data.txt", "r") as f:#Opens data.txt
                                data = f.readlines()#Reads the lines and sets it equal to a variable "data"
                                data = [float(i.strip("\n")) if i != None else 0 for i in data]#strips the \n in data.txt
                                Message = pickle.dumps(data)#Dumps data with pickle and stores it in a variable
                                conn.sendto(Message,(HOST_SEND, PORT_SEND))#Sends data to fmi.py
                                sent = True#Sets variable sent equal to True
                                #print(data)#Prints the data in storage.py
                        else:
                            conn.send(pickle.dumps("No data is stored").encode())#Prints no data stored if there is no data.txt file
                    command = ""#Resets the fmi.py command/input to an empty string 
        

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:#sets concurrent.futures.ThreadPoolExecutor as executor
    executor.submit(receive_and_print_numbers, HOST_RECEIVE, PORT_RECEIVE)#Starts recive_and_print_numbers
    executor.submit(read_from_file, HOST_SEND, PORT_SEND)#starts read_from_file

