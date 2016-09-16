# Class model
from bus import *

class Model:

    def __init__(self):
        self.buses = []
        self.routes = []

    def add_bus(self, bus):
        if bus is not None:
            self.buses.append(bus)
        if bus.route is not None:
            self.add_route(bus.route)

    def remove_bus(self, bus):
        if bus is not None:
            for b in self.buses:
                if bus == b:
                    self.remove_route(bus.route)
                    self.buses.remove(bus)
                    break;

    def add_route(self, route):
        if route is not None:
            self.routes.append(route)

    def remove_route(self, route):
        if route is not None:
            for rt in self.routes:
                if rt == route:
                    self.routes.remove(route)

    def list_of_buses(self):
        return list(self.buses)

    def list_of_routes(self):
        return list(self.routes)

    def get_bus_busNumber(self, busNumber):
        bus = None
        if isinstance(busNumber, int):
            for b in self.buses:
                bus = b
        return bus
