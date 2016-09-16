# Class route

class Route:
    def __init__(self, routeNumber, departure, destination):
        self.routeNumber = routeNumber
        self.departure = departure
        self.destination = destination

    def routeFullInfo(self):
        return "Route number %d, departure place %s, destination %s" %(self.routeNumber, self.departure, self.destination)
        
    def routeInfo(self):
        return "%s-%s" %(self.departure, self.destination)

    def __eq__(self, other):
        result = False
        if isinstance(other, Route) and self.routeNumber == other.routeNumber and self.departure == other.departure and self.destination == other.destination:
            result = True
        return result

    def __str__(self):
        return "%s" %self.routeInfo()
    def __repr__(self):
        return "route %d %s" %(self.routeNumber, self.routeInfo())
