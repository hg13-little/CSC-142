class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._miles_per_gallon = miles_per_gallon

    @property
    def name (self):
        return self._name
    
    @property
    def range(self):
        return self._fuel_capacity * self._miles_per_gallon
    
    @property
    def cost_per_gallon(self):
        return self._cost_per_gallon / self._miles_per_gallon
    
    motorcycle = Vehicle("motorcycle", 7, 35, )
    