# Class Bus
from route import *

class Bus:
    def __init__(self, name, busNumber, route = None):
        self.name = name
        self.busNumber = busNumber
        self.route = route

    def busInfo(self):
        if self.route is None:
            return "Name %s, bus number %d, no route" %(self.name, self.busNumber)
        else:
            return "Name %s, bus number %d, route %s" %(self.name, self.busNumber, self.route.routeInfo())
    def updateBusRoute(self, route):
        if route is not None:
            self.route = route

    def __eq__(self, other):
        result = False
        if isinstance(other, Bus) and self.name == other.name and self.busNumber == other.busNumber and self.route == other.route:
            result = True
        return result

    def __str__(self):
        return "bus : %d" %self.busNumber
    def __repr__(self):
        return "bus \"%s\" : %d; route %s" %(self.name, self.busNumber, self.route)
