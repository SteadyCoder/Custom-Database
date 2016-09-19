# Class route

class Route:

    __destination = "Kyiv"
    __route_key = "route"
    __route_number_key = "route_number"
    __sits_number_key = "sits number"

    def __init__(self, routeNumber, departure, sits_number):
        self.routeNumber = routeNumber
        self.departure = departure
        self.sits_number = sits_number

    def route_full_info(self):
        return "Route number %d, route %s, sits number %d" %(self.routeNumber, self.route_info(), self.sits_number)
        
    def route_info(self):
        return "%s-%s" %(self.departure, self.__destination)

    def dictionary_represantation(self):
        return {self.__route_key : self.route_info(), self.__route_number_key : self.routeNumber, self.__sits_number_key : self.sits_number}

    def __eq__(self, other):
        result = False
        if isinstance(other, Route) and self.routeNumber == other.routeNumber and self.departure == other.departure and self.sits_number == other.sits_number:
            result = True
        return result
    def __str__(self):
        return "%s" %self.route_info()
    def __repr__(self):
        return "route %d %s" %(self.routeNumber, self.route_info())
