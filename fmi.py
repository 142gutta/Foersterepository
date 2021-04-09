import socket
from time import sleep
import pickle

HOST = socket.gethostbyname(socket.gethostname()) #Gets the hosts local IP address
PORT = 12342 #Port
tempreturedata = [] #Creates empty list
raindata = [] # Creates empty list
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP socket as s
command = '' # Creates a empty sting
s.connect((HOST, PORT)) # Connects host and port


def view_forecast(): #Creates a function
    """sends command/input to storage to recive desirable data and recives this data.
    seperates the data in too two lists with a forloop""" 
    s.send(command.encode("utf-8")) # sends command/input to storage to recive desirable data
    response = s.recv(8192) # Recives desireble data from storage
        
    for i in range(len(pickle.loads(response))): # Foreloop that goes through all data sendt by storage
        if i % 2 == 0: #Checks if an element is in possition with a even number.
            tempreturedata.append(pickle.loads(response)[i]) #adds this nummber to tempreturedatalist
        else:
            raindata.append(pickle.loads(response)[i])#If it it not a even number it adds it to a raindatalist
              
while True: #infinite while loop
    command = input("Available commands:\n1. 'all' - Returns all data\n3. 'current' returns newest data\n2. 'exit' - Exits CLI\nCommand: ")#Asks for input from user
    if command == "all": #Checks of input is equal "all"
        view_forecast() # Starts view_forecast
        print("tempreturedata\traindata") #Prints tempreture and raindata
        for t, p in zip(tempreturedata, raindata): #Goes thougtht for tempreture and p for raindata
            print(t, "\t\t", p) #print data trom tempreturedata and raindata
            tempreturedata = []#Resets tempreturedata to avoid duplicates
            raindata = []#Resets raindata to avoid duplicates


    elif command == "current":# Checks if cammand/input is equal "current"
        view_forecast() #Starts view_forecast
        print(f"Here you have the newest forecast: < {tempreturedata[-1]}  celsius > and < {raindata[-1]} mm > of rain.")#Prints a string with the newest tempreturedata and raindata
        tempreturedata = []#Resets tempreturedata to avoid duplicates
        raindata = []#Resets raindata to avoid duplicates

        
    elif command == "exit":#Checks if input/command is equal to "exit"
        print("hope you liked it bye")#Print goodbye message
        s.close()#Closes the connection
        break#Breakes the foreloop

    else:
        print("Not a command")#prints "not a command" if command/input is not equal to "current", "exit" or "all"


