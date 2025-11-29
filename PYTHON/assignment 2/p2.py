class Vehicle:
    def calculate_fare(self, distance):
        pass

class Auto(Vehicle):
    def calculate_fare(self, distance):
        return 10 + distance * 8

class Bike(Vehicle):
    def calculate_fare(self, distance):
        return 5 + distance * 5

class Sedan(Vehicle):
    def calculate_fare(self, distance):
        return 20 + distance * 12


vehicles = [Auto(), Bike(), Sedan()]

for v in vehicles:
    print(v.__class__.__name__, "Fare =", v.calculate_fare(10))
