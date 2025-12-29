class Vehicle():
    
    def __init__(self, color, maxSpeed):
        self.color = color
        self._maxSpeed = maxSpeed

    def getMaxSpeed(self):
        return self._maxSpeed

    def setmaxSpeed(self, maxSpeed):
        self._maxSpeed = maxSpeed
        
    def print(self):
        print("Color:", self.color)
        print("Max Speed:", self._maxSpeed)

class Car(Vehicle):
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def print(self):
        #self.print()
        print("No of Gears :", self.numGears)
        print("Is Converitble :", self.isConvertible)

c = Car("red", 100, 8, True)
c.print()
