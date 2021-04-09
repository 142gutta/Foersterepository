INF142 - Mandatory Assignment 
Group 34: Jonas Riisøen Land, Åsmund Austrheim & Hans Jørgen Jacobsen


- MVP:

How to use:
    1) Activate the server, storage.py, either in CLI or VScode terminal. The server will print a confirmation when it is online.
    2) Activate the weather station, weather_station.py in CLI. It will immediately start to send packets to server. Between weather_station and storage, we have chosen a UDP connection. A file, data.txt will be created and used to store this data.
    3) Activate the user-client, fmi.py, in CLI. You will now have access to different commands:
            a. "All" : Returns all data to the user, presented ass a list with temperature and rain.
            b. "Current": Returns the latest data recorded in the DB.
            c. "Exit": Exit from the CLI, also clears out data.txt when activated (in order to clear   out space).
        FMI and Storage is connected through a TCP-connection, and Storage will send the entire data.txt file according to the MVP project description.    

- EXTENSIONS:
We have added two extensions to the MVP, both running from the same file. The extensions are (1) Graphical User Interface, and (2) Integration with Matplotlib:

    Required python libraries:
        - PySimpleGUI
        - Matplotlib

    How to use:
        1) Install PySimpleGUI using Pip.
        2) Run part 1. and 2. according to MVP-description.
        3) Launch GUI.py instead of FMI.py. 

    Functionality: 
        TAB 1:
            Within tab 1 of the program we have tried to create a user-friendly experience which shows current temperature which updates with the click of the *-button, as well as a quote to match the current temperature and rain levels. As well as avg. temp and rain last 10 days.

        TAB2:
            Within tab 2 we integrate matplotlib into the GUI. By the push of a button you have the plot of rain and temperature within given intervals
 

- SOURCES: 

    General socket programming:

    "https://realpython.com/python-sockets/?fbclid=IwAR2c7jCEnN9JCJ9fpHV36m6QB9H0vbBlYwer5vPqa5SARfo0sdZZuQMXiRk#echo-server"

    "https://www.techwithtim.net/tutorials/socket-programming/?fbclid=IwAR1AXufR2Qz_kc4BCcBLQNRP7UausKkrW2Jmc0l-92wjNkILTRX65-40INw"

    "https://pythontic.com/modules/socket/udp-client-server-example?fbclid=IwAR30_NeEmn4iweAOVN17t6lZfmO00JEBd3ZD7XOBNVh89eeSGvvuoGfd8pI"

    Concurrent futures, JSON, Pickle: 

    "https://docs.python.org/3/library/concurrent.futures.html"

    PySimpleGUI:

    "https://www.youtube.com/watch?v=icvLQA1YvZo"

    "https://realpython.com/pysimplegui-python/"

    "https://pysimplegui.readthedocs.io/en/latest/"

    Integrating matplotlib in PySimpleGUI:

    "https://pysimplegui.readthedocs.io/en/latest/cookbook/?fbclid=IwAR3SzL4AjfZsR9NIABFkeQ4JX-0do1IkvtPci6fqssd96YgmCLIoMv2zBy4#animated-matplotlib-graph"


















