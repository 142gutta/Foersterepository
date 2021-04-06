import  socket
import threading
import pickle
# Kilde brukt til det meste: https://www.techwithtim.net/tutorials/socket-programming/

Format = "utf-8"
Header = 64
Port = 5501
DisconnectFromServer = "!bye"     #Melding som kan sendes for å bryte forbindelsen

StorageServer = socket.gethostbyname(socket.gethostname()) #Finner PC'en sin IP-adresse
Connection = (StorageServer, Port)

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Selve Socketen, denne av type TCP
ServerSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Smelle en UDP socket her for the lættis ?

ServerSocket.bind(('', Port)) #Litt usikker på om man skal ha (' ', Port) her eller om Connectiongreiene mine funker


        #clientsocket.close()

def handle_client (conn, addr) :  
    print(f"New connection: {addr} joined")   
    connected = True
    msg_length = conn.recv(Header).decode(Format)
    while connected:
        if msg_length:
            msg_length = len(msg_length)
            msg = conn.recv(msg_length).decode(Format)
            if msg == DisconnectFromServer:
                break
        if msg == "Weather":
            pickle.loads(msg)
                
    conn.close()

def StartServer():
    ServerSocket.listen() #Listening mode, hva enn det er 
    print("Server Online")
    while True:
        conn, addr = ServerSocket.accept()
        msg = "Thanks for connecting motherfucker"
        conn.send(msg.encode("UTF-8"))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Connections: {threading.activeCount()-1 }")

StartServer() 

# while True:
#     clientsocket, addr = ServerSocket.accept()                  #Får error i denne linjen, ugyldig argument
#     sentence = conn.recv(1024).deode()
#     conn.send("Hello".encode())
#     thread = threading.Thread(target=handle_client, args=(conn, addr))

#     thread.start()
#     print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")   









