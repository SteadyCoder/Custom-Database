# Class route

class Route:
        def __init__(self, routeNumber, departure, destination):
            self.routeNumber = routeNumber
            self.departure = departure
            self.destination = destination

        def __str__(self):
            return "%s" %self.routeInfo()
            
        def routeFullInfo(self):
            return "Route number %d, departure place %s, destination %s" %(self.routeNumber, self.departure, self.destination)
        
        def routeInfo(self):
            return "%s-%s" %(self.departure, self.destination)


