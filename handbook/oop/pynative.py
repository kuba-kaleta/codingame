# https://pynative.com/python-object-oriented-programming-oop-exercise/

# Ex 1
class Vehicle1:
    def __init__(self, max_speed, mileage):
        self. max_speed = max_speed
        self.mileage = mileage


# Ex 2
class Vehicle2:
    pass


# Ex 3
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __str__(self):
        return f"{self.name}, {self.mileage}, {self.max_speed}"

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount


sb = Bus("Volvo", 180, 12, 50)
print(sb, sb.seating_capacity())


# Ex4
class Car(Vehicle):
    pass


c = Car("Audi", 240, 18, 5)
print(c.color)

# Ex 6
print("Total Bus fare is:", sb.fare())


# Ex 7
print(type(sb))

# Ex 8
print(isinstance(sb, Vehicle))



