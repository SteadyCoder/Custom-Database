from bus import * 
from route import *
from model import *


route1 = Route(54, "Lviv", "Kyiv")
route2 = Route(34, "Zhytomyr", "Kyiv")

bus1 = Bus("Etalon", 134, route1)
bus2 = Bus("Ikarus", 35, route2)

bus3 = Bus("Gazel", 42, Route(45, "Slav", "Kyiv"))

myModel = Model()

myModel.add_bus(bus1)
myModel.add_bus(bus2)
myModel.add_bus(bus3)

print myModel.list_of_buses()
print myModel.list_of_routes()

print myModel.get_bus_busNumber(134)
