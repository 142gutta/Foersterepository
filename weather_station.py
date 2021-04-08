from time import sleep
import socket
from station import StationSimulator
import json


HOST = socket.gethostbyname(socket.gethostname())
PORT = 11111
SIM_INT = 2

if __name__ == "__main__":

    # Instantiate a station simulator
    bergen_station = StationSimulator(simulation_interval=SIM_INT)
    # Turn on the simulator
    bergen_station.turn_on()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        while True:
            #Data3 = {"Temp": [] , "Rain": [], }


            d = bergen_station.temperature
            e = bergen_station.rain
            f = (d, e)

            data = json.dumps(d).encode('utf-8')
            data2 = json.dumps(e).encode('utf-8')
            #data5 = json.dumps(f).encode('utf-8')

            #Data3["Temp"].append(d)
            #Data3["Rain"].append(e)

            #data4 = json.dumps(Data3).encode('utf-8')
            
            s.sendto(data, (HOST, PORT))
            s.sendto(data2, (HOST, PORT))
            print(f"Sending weatherdata to {HOST}")
            #s.sendto(data4, (HOST, PORT))
            #s.sendto(data5, (HOST, PORT))

            sleep(SIM_INT)

    # Shut down the simulation
    bergen_station.shut_down()