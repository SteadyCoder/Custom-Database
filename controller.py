# Module controller
from model import *
from view import *
from bus import * 
from route import *
import random


myModel = Model()
    
def run():    
    route1 = Route(54, "Lviv", 38)
    route2 = Route(34, "Zhytomyr", 54)

    bus1 = Bus("Etalon", 134, route1)
    bus2 = Bus("Ikarus", 35, route2)

    bus3 = Bus("Gazel", 42, Route(45, "Slav", 44))

    myModel.add_bus(bus1)
    myModel.add_bus(bus2)
    myModel.add_bus(bus3)

    start()
        
def start():
    mode = 0
    View.menu_start()
    
    while mode != 9:
        if mode == 1:
            available_buses()
            View.menu_start()
        elif mode == 2:
            available_routes()
            View.menu_start()
        elif mode == 3:
            adding_bus_session()
            View.menu_start()
        elif mode == 4:
            deleting_bus_session()
            View.menu_start()
        elif mode == 5:
            change_existing_bus_session()
            View.menu_start()
        elif mode == 6:
            adding_route_session()
            View.menu_start()
        elif mode == 7:
            deleting_route_session()
            View.menu_start()
        elif mode == 8:
            print "Changing existing route"
            change_existing_route_session()
            View.menu_start()

        mode = int(raw_input())



# Methods for bus operation ------------------------------------
def available_buses():
    View.display(myModel.buses_list_dictionary_represantation())

def adding_bus_session():
    View.add_new_bus()
    try:
        name = str(raw_input('Name: '))
        bus_number = int(raw_input('Bus number : '))
        View.display(myModel.routes_list_dictionary_represantation())
        route_number = int(raw_input('Route number : '))
    except ValueError:
        View.error_message()
    else:
        if bus_number in myModel.get_all_bus_numbers():
            View.warn_message()
            View.success_message()
            while (bus_number in myModel.get_all_bus_numbers()):
                bus_number = random.randint(1, 200)
            route = None
            if route_number != 0:
                route = myModel.get_route_with_number(route)
            new_bus = Bus(name, bus_number, route)
            myModel.add_bus(new_bus)
        else:
            View.success_message()
            route = None
            if route_number != 0:
                route = myModel.get_route_with_number(route)
            new_bus = Bus(name, bus_number, route)
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

# Methods for route operations ------------------------------------

def available_routes():
    View.display(myModel.routes_list_dictionary_represantation())

def adding_route_session():
    View.add_new_route()
    try:
        departure = str(raw_input('Departure: '))
        route_number = int(raw_input('Route number: '))
        sits_number = int(raw_input('Sits number: '))
    except ValueError:
        View.error_message()
    else:
        if route_number in myModel.get_all_route_numbers():
            View.warn_message()
            View.success_message()
            while (route_number in myModel.get_all_route_numbers()):
                route_number = random.randint(1, 200)    

            new_route = Route(route_number, departure, sits_number)
            myModel.add_route(new_route)
        else: 
            View.success_message()
            new_route = Route(route_number, departure, sits_number)
            myModel.add_route(new_route)

def deleting_route_session():
    View.delete_route()
    try:
        available_routes()
        route_number = int(raw_input())
    except ValueError:
        View.error_message()
    else:
        if (route_number in myModel.get_all_route_numbers()):
            myModel.remove_route(myModel.get_route_with_number(route_number))
            View.success_message()
        else:
            View.wrong_message()

def change_existing_route_session():
    View.change_route_one()
    available_routes()
    try:
       choice = int(raw_input())
    except ValueError:
        View.wrong_number_message()
    else:
        if choice != 0:
            View.change_route_two()
            if (choice in myModel.get_all_route_numbers()):
                route_changing = myModel.get_route_with_number(choice)
                try:
                    departure = str(raw_input('Departure: '))
                    sits_number = int(raw_input('Sist number: '))
                except ValueError:
                    View.error_message()
                else:
                    if departure != '0':
                        route_changing.departure = departure
                    if sits_number != 0:
                        route_changing.sist_number = sits_number
