import socket
import threading
import example
import pickle

a_list = example.get_List_of_Weather(1,10,1)
print(a_list)
HEADER = 1024
PORT = 5501
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(ADDR)
print("Connected")

data = pickle.dumps(a_list)

def send(msg):
    print("sending message")
    client.sendto(msg, (ADDR)) 

send(data)
""" 
message = msg.encode(FORMAT)
msg_length = len(message)
send_length = str(msg_length).encode(FORMAT)
send_length += b' '*(HEADER - len(send_length))
client.send(send_length)
client.send(message)
"""
