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

    def __str__(self):
        return "Name %s, bus number %d route %s" %(self.name, self.busNumber, self.route)
    def __repr__(self):
        return "'bus name %s'" %self.name
