from time import sleep
import socket
from station import StationSimulator
import json


HOST = socket.gethostbyname(socket.gethostname())#Gets local IP-address, stores it as variable HOST
PORT = 11111#Sets 11111 as PORT
SIM_INT = 2#Sets variable SIM_INT equal to 2

if __name__ == "__main__":

    # Instantiate a station simulator
    bergen_station = StationSimulator(simulation_interval=SIM_INT)
    # Turn on the simulator
    bergen_station.turn_on()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:#Sets UDP socket as s

        while True:#While loop

            Tempreture_data = bergen_station.temperature#Stores tempreture data from bergen_station as Tempreture_data
            Rain_data = bergen_station.rain#Stores rain data from bergen_station as Rain_data

            Tempreture_data_send = json.dumps(Tempreture_data).encode('utf-8')#Encodes Tempreture_data with json.dumps
            Rain_data_send = json.dumps(Rain_data).encode('utf-8')#Encodes Rain_data with json_dumps
    
            
            s.sendto(Tempreture_data_send, (HOST, PORT))#Sends tempreture data to storage.py
            s.sendto(Rain_data_send, (HOST, PORT))#Sends rain data to storage.py
            print(f"Sending weather data to {HOST}")#print "Sending weather data to" HOST
    
            sleep(SIM_INT)#Sleeps for 2 seconds

    # Shut down the simulation
    bergen_station.shut_down()