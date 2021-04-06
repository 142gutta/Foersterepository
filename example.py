from time import sleep

from station import StationSimulator

# https://www.geeksforgeeks.org/python-merge-two-lists-into-list-of-tuples/
def merge(list1, list2):
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list
      
# Driver code



def get_List_of_Weather(interval_for_sim, sim_range, sim_sleep):
    """interval for simulation in seconds
    simulation range, amount of intervals
    sleep period"""
    # Instantiate a station simulator
    bergen_station = StationSimulator(simulation_interval=interval_for_sim)
    # Turn on the simulator
    bergen_station.turn_on()

    # Two lists for temperature and precipitation
    temperature = []
    precipitation = []

    # Capture data for 72 hours
    # Note that the simulation interval is 1 second
    for _ in range(sim_range):
        # Sleep for 1 second to wait for new weather data
        # to be simulated
        sleep(sim_sleep)
        # Read new weather data and append it to the
        # corresponding list
        temperature.append(bergen_station.temperature)
        precipitation.append(bergen_station.rain)

    # Shut down the simulation
    bergen_station.shut_down()

    new_list = merge(temperature, precipitation)
    return new_list
    #print (new_list)
    # Print the collected data
    # print("Temperature\tPrecipitation")
    # for t, p in zip(temperature, precipitation):
    #     print(t, "\t\t", p)
