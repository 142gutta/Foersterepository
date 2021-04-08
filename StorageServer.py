import  socket
import threading
import pickle
# Kilde brukt til det meste: https://www.techwithtim.net/tutorials/socket-programming/

Format = "utf-8"
Header = 1024
Port = 5501
DisconnectFromServer = "!bye"     #Melding som kan sendes for å bryte forbindelsen

StorageServer = socket.gethostbyname(socket.gethostname()) #Finner PC'en sin IP-adresse
Connection = (StorageServer, Port)

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Selve Socketen, denne av type TCP
ServerSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Smelle en UDP socket her for the lættis ?

ServerSocket.bind(('', Port)) #Litt usikker på om man skal ha (' ', Port) her eller om Connectiongreiene mine funker
ServerSocket2.bind(('', Port))
print()

        #clientsocket.close()





def GetWeather ():
    while True:
        list_weather = []      
        data, addr = ServerSocket2.recvfrom(1024)
        print ("received message"), data
        pickle_list = (pickle.loads(data))
        list_weather.append(pickle_list)
        print(f"Complete list of weatherdata {list_weather}")



def StartServer():
    ServerSocket.listen() #Listening mode, hva enn det er
    print("Server Online") 
    thread_udp = threading.Thread(target=GetWeather())
    thread_udp.start()

StartServer()






"""
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

    conn.close()
list_weather = []
def handle_client2 (conn, addr):
    while True:
        conn, addr = ServerSocket2.recvform(1024)
        print("Pickleman is here"), conn
        picklelist = pickle.loads(conn)
        list_weather.append(picklelist)

print(list_weather)


    print("its pickle time")
    msg_length = conn.recv(Header).decode(Format)
    while True:
            if msg_length:
                print("Received pickle")
                msg = conn.recv(msg_length).decode(Format)
                print(msg)
                #conn, addr = ServerSocket2.recvfrom(1024)
                print("pickle has been delivered")
                print(pickle.loads(conn))
                if msg == DisconnectFromServer:
                    break

        



def StartServer():
    ServerSocket.listen() #Listening mode, hva enn det er 
    print("Server Online")
    while True:
        conn, addr = ServerSocket.accept()
        msg = "Thanks for connecting motherfucker"
        conn.send(msg.encode("UTF-8"))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        thread_udp = threading.Thread(target=handle_client2, args=(conn, addr))
        thread_udp.start()
        print(f"Connections: {threading.activeCount()-1 }")

StartServer() 

# while True:
#     clientsocket, addr = ServerSocket.accept()                  #Får error i denne linjen, ugyldig argument
#     sentence = conn.recv(1024).deode()
#     conn.send("Hello".encode())
#     thread = threading.Thread(target=handle_client, args=(conn, addr))

#     thread.start()
#     print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")   

"""







