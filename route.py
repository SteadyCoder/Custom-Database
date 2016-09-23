# Class route

class Route:

    __destination = "Kyiv"
    __route_key = "route"
    __route_number_key = "route_number"
    __departure_time_key = "time 24H"

    def __init__(self, routeNumber, departure, departure_time):
        self.routeNumber = routeNumber
        self.departure = departure
        self.departure_time = departure_time

    def route_full_info(self):
        return "Route number %d, route %s, time %d" %(self.routeNumber, self.route_info(), self.departure_time)
        
    def route_info(self):
        return "%s-%s" %(self.departure, self.__destination)

    def dictionary_represantation(self):
        return {self.__route_key : self.route_info(), self.__route_number_key : self.routeNumber, self.__departure_time_key : self.departure_time}

    def __eq__(self, other):
        result = False
        if isinstance(other, Route) and self.routeNumber == other.routeNumber and self.departure == other.departure and self.departure_time == other.departure_time:
            result = True
        return result
    def __str__(self):
        return "%s" %self.route_info()
    def __repr__(self):
        return "route %d %s" %(self.routeNumber, self.route_info())
