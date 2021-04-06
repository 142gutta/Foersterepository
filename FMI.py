
#FMI-klient

#Kilde brukt til det meste: https://www.techwithtim.net/tutorials/socket-programming/


import socket
Header = 1024     #Vet ikke om denne er nødvendig
Port = 5501
StorageServer = socket.gethostbyname(socket.gethostname()) #Fra Youtube-video, denne finner riktig IP-adresse på alle PC'er.
#StorageServer = "10.111.24.92"
print(StorageServer)
Connection = (StorageServer, Port)
DisconnectMessage = "!Bye"
#GetWeather = '!Weather' #Request Weather info
#Disconnect = '!Bye' #Disconnect from server

#Setter opp selve socketen, SOCK_Stream indikerer TCP socket.
FMIclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FMIclient.connect(Connection)
#if connected:
#    print('Connected to server')
#else:
#    print("not connected")

while (text:= input(">")).lower() != DisconnectMessage:                 #usikker, hva dette er men  la inn en standard send & receive greie fra en annen forelesning, denne må vi nok 
    FMIclient.sendto(text.encode("UTF-8"), Connection)                     #endre, da vi ønsker å motta en liste/fil/noe annet, mulig vi må bruke "pickle" modulen til dette. 
    msg, addr = FMIclient.recvfrom(2048)
    print(f"{StorageServer} says: {msg.decode()}")







