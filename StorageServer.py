import  socket
import threading

# Kilde brukt til det meste: https://www.techwithtim.net/tutorials/socket-programming/


Port = 5500
DisconnectFromServer = "!bye"     #Melding som kan sendes for å bryte forbindelsen

StorageServer = socket.gethostbyname(socket.gethostname()) #Finner PC'en sin IP-adresse
Connection = (StorageServer, Port)

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Selve Socketen, denne av type TCP

ServerSocket.bind(Connection) #Litt usikker på om man skal ha (' ', Port) her eller om Connectiongreiene mine funker






#Handle_client er direkte kopiert fra TechWithTim fra linken over for å debugge, funket ikke
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    #while connected:


#Denne kjører heller ikke riktig, får problemer i While True loopen
def StartServer():
    ServerSocket.listen #Listening mode, hva enn det er 
    print(f"[Listening] server is listening on {StorageServer}") #Bekrefter at server er på
    while True:
        conn, addr = ServerSocket.accept()                  #Får error i denne linjen, ugyldig argument
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")        













StartServer()  

