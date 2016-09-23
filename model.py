# Class model
from bus import *

class Model:

    def __init__(self):
        self.buses = []
        self.routes = []

    def add_bus(self, bus):
        if bus is not None:
            self.buses.append(bus)

    def remove_bus(self, bus):
        if bus is not None:
            for b in self.buses:
                if bus == b:
                    self.buses.remove(bus)
                    break;

    def add_route(self, route):
        if route is not None:
            self.routes.append(route)

    def remove_route(self, route):
        if route is not None:
            for rt in self.routes:
                if rt == route:
                    self.__delete_route_from_buses(route)          
                    self.routes.remove(route)

    def __delete_route_from_buses(self, route):
        for bus in self.buses:
            if bus.route_number == route.routeNumber:
                bus.route_number = 0

    def list_of_buses(self):
        return list(self.buses)

    def list_of_routes(self):
        return list(self.routes)

    def get_bus_with_busNumber(self, busNumber):
        bus = None
        if isinstance(busNumber, int):
            for b in self.buses:
                if b.busNumber == busNumber:
                    bus = b
                    break
        return bus
    def get_bus_with_name(self, bus_name):
        bus = None
        if isinstance(bus_name, str):
            for b in self.buses:
                if b.name == bus_name:
                    bus = b
                    break
        return bus

    def get_route_with_number(self, routeNumber):
        route = None
        if isinstance(routeNumber, int):
            for r in self.routes:
                if r.routeNumber == routeNumber:
                    route = r
                    break
        return route
    
    def get_route_with_departure(self, departure):
        route = None
        if isinstance(departure, str):
            for r in self.routes:
                if r.departure == departure:
                    route = r
                    break
        return route

    def get_all_bus_numbers(self):
        return [x.busNumber for x in self.buses]
    def get_all_bus_names(self):
        return [x.name for x in self.buses]
    def get_all_route_numbers(self):
        return [x.routeNumber for x in self.routes]
    def get_all_route_names(self):
        return [x.route_info() for x in self.routes]

    def buses_list_dictionary_represantation(self):
        return [x.dictionary_represantation(self.get_route_with_number(x.route_number)) for x in self.buses]
    def routes_list_dictionary_represantation(self):
        return [x.dictionary_represantation() for x in self.routes]
