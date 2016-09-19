# Class Bus
from route import *

class Bus:

    __name_key = "name"
    __bus_number_key = "bus number"
    __route_key = "route"
    __const_no_route = "No route"

    def __init__(self, name, busNumber, route = None):
        self.name = name
        self.busNumber = busNumber
        self.route = route

    def bus_info(self):
        if self.route is None:
            return "Name %s, bus number %d, no route" %(self.name, self.busNumber)
        else:
            return "Name %s, bus number %d, route %s" %(self.name, self.busNumber, self.route.route_info())

    def update_bus_route(self, route):
        self.route = route

    def dictionary_represantation(self):
        if self.route is None:
            return {self.__name_key : self.name, self.__bus_number_key : self.busNumber, self.__route_key : self.__const_no_route}
        else:
            return {self.__name_key : self.name, self.__bus_number_key : self.busNumber, self.__route_key : self.route.route_info()}
    def __eq__(self, other):
        result = False
        if isinstance(other, Bus) and self.name == other.name and self.busNumber == other.busNumber and self.route == other.route:
            result = True
        return result
    def __str__(self):
        return "bus : %d" %self.busNumber
    def __repr__(self):
        return "bus \"%s\" : %d; route %s" %(self.name, self.busNumber, self.route)
