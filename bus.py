# Class Bus
from route import *

class Bus:

    __name_key = "name"
    __bus_number_key = "bus number"
    __route_key = "route"
    __const_no_route = "No route"

    def __init__(self, name, busNumber, route_number):
        self.name = name
        self.busNumber = busNumber
        self.route_number = route_number

    def bus_info(self):
        return "Name %s, bus number %d, route_number %s" %(self.name, self.busNumber, self.route_number)

    def update_bus_route(self, route_number):
        self.route_number = route_number

    def dictionary_represantation(self, route):   
        if route is None or self.route_number == 0:
            return {self.__name_key : self.name, self.__bus_number_key : self.busNumber, self.__route_key : self.__const_no_route}
        else: 
            return {self.__name_key : self.name, self.__bus_number_key : self.busNumber, self.__route_key : route.route_info()}

    def __eq__(self, other):
        result = False
        if isinstance(other, Bus) and self.name == other.name and self.busNumber == other.busNumber and self.route_number == other.route_number:
            result = True
        return result
    def __str__(self):
        return "bus : %d" %self.busNumber
    def __repr__(self):
        return "bus \"%s\" : %d; route %s" %(self.name, self.busNumber, self.route_number)
