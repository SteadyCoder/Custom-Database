from bus import * 
from route import *
from model import *


myRoute = Route(54, "Lviv", "Kyiv")

myBus = Bus("Etalon", 134, myRoute)

bus2 = Bus("Ikarus", 35, myRoute)

myModel= Model()

myModel.addRace(myBus)
myModel.addRace(bus2)

print myModel.races

