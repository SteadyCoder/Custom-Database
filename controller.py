# Module controller
from model import *
import constants
from view import *
from bus import *
from route import *
import random
import pickle

myModel = None
    
def run(file_name):    
    read_file(file_name)
    start(file_name)
    
def read_file(file_name):
    my_file = open(file_name, constants.file_read_option)
    global myModel
    try:
        myModel = pickle.load(my_file)
    except (EOFError, pickle.UnpicklingError):
        myModel = Model()
    finally:
        my_file.close()

def write_to_file(file_name):
    my_file = open(file_name, constants.file_write_option)
    global myModel
    try:
        pickle.dump(myModel , my_file)
    except pickle.PicklingError:
        View.error_serialize_message()
    finally:
        my_file.close()
    

def start(file_name):
    mode = constants.const_zero_number
    View.menu_start()
    
    while mode != 10:
        try: 
            mode = int(raw_input(constants.const_choose))
        except ValueError:
            View.wrong_option()
            mode = constants.const_zero_number

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
            change_existing_route_session()
            View.menu_start()
        elif mode == 9:
            search_bus_session()
            View.menu_start()
        elif mode == 10:
            write_to_file(file_name)
            View.exit_message()
        elif mode not in range(1, 11):
            View.wrong_number_message()
            View.menu_start()
       

# Methods for bus operation ------------------------------------
def available_buses():
    View.display(myModel.buses_list_dictionary_represantation())

def adding_bus_session():
    View.add_new_bus()
    try:
        name = str(raw_input(constants .const_name))
        if not len(name):
            raise ValueError
        bus_number = int(raw_input(constants.const_bus_number))
        View.display(myModel.routes_list_dictionary_represantation())
        route_number = int(raw_input(constants.const_route_number))
    except ValueError:
        View.error_message()
    else:
        if bus_number in myModel.get_all_bus_numbers():
            View.warn_message()
            View.success_message()
            while (bus_number in myModel.get_all_bus_numbers()):
                bus_number = random.randint(1, 200)
            route = None
            if route_number != constants.const_zero_number:
                route = myModel.get_route_with_number(route_number)
            new_bus = Bus(name, bus_number, route_number)
            myModel.add_bus(new_bus)
        else:
            View.success_message()
            route = None
            if route_number != constants.const_zero_number:
                route = myModel.get_route_with_number(route_number)
            new_bus = Bus(name, bus_number, route_number)
            myModel.add_bus(new_bus)

def deleting_bus_session():
    View.delete_bus()
    try:
        available_buses()
        bus_number = int(raw_input(constants.const_bus_number))
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
        choice = int(raw_input(constants.const_bus_number))
    except ValueError:
        View.wrong_number_message()
    else:
        if choice != constants.const_zero_number:
            View.change_bus_two()
            if (choice in myModel.get_all_bus_numbers()):
                bus_changing = myModel.get_bus_with_busNumber(choice)
                try:
                    name = str(raw_input(constants.const_name))
                    View.display(myModel.routes_list_dictionary_represantation())
                    route_number = int(raw_input(constants.const_route_number))
                except ValueError:
                    View.error_message()
                else:
                    if route_number in myModel.get_all_route_numbers():
                        if name !=  constants.const_zero_string:
                            bus_changing.name = name
                        if route_number != constants.const_zero_number:
                            bus_changing.route_number = route_number
                    else:
                        View.wrong_number_message()

# Methods for route operations ------------------------------------

def available_routes():
    View.display(myModel.routes_list_dictionary_represantation())

def adding_route_session():
    View.add_new_route()
    try:
        departure = str(raw_input(constants.const_departure))
        route_number = int(raw_input(constants.const_route_number))
        hours = str(raw_input(constants.const_time_hours))
        minutes = str(raw_input(constants.const_time_minutes))
        if int(hours) < 0 or int(hours) > 24 or int(minutes) < 0 or int(minutes) > 59:
            raise ValueError
    except ValueError:
        View.error_message()
    else:
        departure_time = time_validation(hours, minutes)
        if route_number in myModel.get_all_route_numbers():
            View.warn_message()
            View.success_message()
            while (route_number in myModel.get_all_route_numbers()):
                route_number = random.randint(1, 200)

            new_route = Route(route_number, departure, departure_time)
            myModel.add_route(new_route)
        else: 
            View.success_message()
            new_route = Route(route_number, departure, departure_time)
            myModel.add_route(new_route)

def deleting_route_session():
    View.delete_route()
    try:
        available_routes() 
        route_number = int(raw_input(constants.const_route_number))
    except ValueError:
        View.error_message()
    else:
        if (route_number in myModel.get_all_route_numbers()): 
            myModel.remove_route(myModel.get_route_with_number(route_number))
            View.success_message()
        else:
            View.wrong_number_message()

def change_existing_route_session():
    View.change_route_one()
    available_routes()
    try:
        choice = int(raw_input(constants.const_route_number))
    except ValueError:
        View.wrong_number_message()
    else:
        if choice != constants.const_zero_number: 
            if (choice in myModel.get_all_route_numbers()):
                View.change_route_two()  
                route_changing = myModel.get_route_with_number(choice)
                try:
                    departure = str(raw_input(constants.const_departure))
                    hours = str(raw_input(constants.const_time_hours))
                    minutes = str(raw_input(constants.const_time_minutes))
                    if hours != constants.const_empty_string:
                        if int(hours) not in range(0, 25):
                            raise ValueError
                    if minutes != constants.const_empty_string:
                        if int(minutes) not in range(0, 60):
                            raise ValueError
                except ValueError:
                    View.error_message()
                else:
                    departure_time = time_validation(hours, minutes)
                    if departure != constants.const_empty_string:
                        route_changing.departure = departure
                    if departure_time != constants.const_zero_string and departure_time != constants.const_check_point:
                        route_changing.departure_time = departure_time
            else:
                View.wrong_number_message()

def search_bus_session():
    View.search_for_bus
    try:
        departure = str(raw_input(constants.const_departure))
    except ValueError:
        View.error_message()
    else:
        if departure == "":
            View.error_message()
        else:
            routes = []
            for r in myModel.routes:
                if departure == r.departure:
                    routes.append(r.dictionary_represantation())
            View.display(routes)


def time_validation(hours, minutes):
    result = hours + ":" + minutes
    if len(minutes) == 1:
        minutes = "0" + minutes
    if len(hours) == 1:
        hours = "0" + hours
    if hours != "" or minutes != "":
        result = hours + ":" + minutes
    
    return result
