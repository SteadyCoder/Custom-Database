# Class route

class Route:

    __destination = "Kyiv"

    def __init__(self, routeNumber, departure, sits_number):
        self.routeNumber = routeNumber
        self.departure = departure
        self.sits_number = sits_number

    def route_full_info(self):
        return "Route number %d, route %s, sits number %d" %(self.routeNumber, self.route_info(), self.sits_number)
        
    def route_info(self):
        return "%s-%s" %(self.departure, self.__destination)

    def __eq__(self, other):
        result = False
        if isinstance(other, Route) and self.routeNumber == other.routeNumber and self.departure == other.departure and self.sits_number == other.sits_number:
            result = True
        return result

    def __str__(self):
        return "%s" %self.route_info()
    def __repr__(self):
        return "route %d %s" %(self.routeNumber, self.route_info())
