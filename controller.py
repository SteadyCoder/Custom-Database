# Module controller
from model import *
from view import *
from bus import * 
from route import *
import random


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
            available_buses()
            View.menu_start()
        elif mode == 2:
            adding_bus_session()
            View.menu_start()
        elif mode == 3:
            deleting_bus_session()
            View.menu_start()
        elif mode == 4:
            change_existing_bus_session()
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
    View.display(myModel.buses_list_dictionary_represantation())

def adding_bus_session():
    View.add_new_bus()
    try:
        name = str(raw_input('Name: '))
        bus_number = int(raw_input('Bus number : '))
        View.display(myModel.routes_list_dictionary_represantation())
        route = int(raw_input('Route number : '))
    except ValueError:
        View.error_message()
    else:
        if bus_number in myModel.get_all_bus_numbers():
            View.warn_message()
            View.success_message()
            while (bus_number in myModel.get_all_bus_numbers()):
                bus_number = random.randint(1, 200)
            new_bus = Bus(name, bus_number, myModel.get_route_with_number(route))
            myModel.add_bus(new_bus)
        else:
            View.success_message()
            new_bus = Bus(name, bus_number, myModel.get_route_with_number(route))
            myModel.add_bus(new_bus)

def deleting_bus_session():
    View.delete_bus()
    try:
        available_buses()
        bus_number = int(raw_input())
    except ValueError:
        View.error_message()
    else:
        if (bus_number in myModel.get_all_bus_numbers()):
            myModel.remove_bus(myModel.get_bus_with_busNumber(bus_number))
            View.success_message()
        else:
            View.wrong_number_message()

def change_existing_bus_session():
    View.change_bus_one()
    available_buses()
    try:
       choice = int(raw_input())
    except ValueError:
        View.wrong_number_message()
    else:
        print int(choice)
        if choice != 0:
            View.change_bus_two()
            if (choice in myModel.get_all_bus_numbers()):
                bus_changing = myModel.get_bus_with_busNumber(choice)
                try:
                    name = str(raw_input('Name: '))
                    View.display(myModel.routes_list_dictionary_represantation())
                    route_number = int(raw_input('Route number : '))
                except ValueError:
                    View.error_message()
                else:
                    if route_number in myModel.get_all_route_numbers():
                        if name != '0':
                            bus_changing.name = name
                        if route_number != 0:
                            bus_changing.route = myModel.get_route_with_number(route_number)
                    else:
                        View.wrong_number_message()



