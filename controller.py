# Module controller
from model import *
from view import *
from bus import * 
from route import *


myModel = Model()
    
def run():    
    route1 = Route(54, "Lviv", "Kyiv")
    route2 = Route(34, "Zhytomyr", "Kyiv")

    bus1 = Bus("Etalon", 134, route1)
    bus2 = Bus("Ikarus", 35, route2)

    bus3 = Bus("Gazel", 42, Route(45, "Slav", "Kyiv"))

    myModel.add_bus(bus1)
    myModel.add_bus(bus2)
    myModel.add_bus(bus3)

    start()
        
def start():
    mode = 0
    View.menu_start()
    
    while mode != 8:
        if mode == 1:
            print "Display list of available buses"
            available_buses()
            View.menu_start()
        elif mode == 2:
            print "Adding bus"
            View.menu_start()
        elif mode == 3:
            print "Deleting bus"
            View.menu_start()
        elif mode == 4:
            print "Changing existing bus"
            View.menu_start()
        elif mode == 5:
            print "Adding route"
            View.menu_start()
        elif mode == 6:
            print "Deleting route"
            View.menu_start()
        elif mode == 7:
            print "Changing existing route"
            View.menu_start()

        mode = int(raw_input())




def available_buses():
    View.display_all_buses(myModel.buses_list_dictionary_represantation())

def adding_bus_session():
    View.add_new()


