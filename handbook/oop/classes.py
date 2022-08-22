# https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python exercises

# Ex1
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


i1 = Car("blue", 30000)
i2 = Car("red", 20000)

for x in (i1, i2):
    print(x.color, x.mileage)


# Ex2
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

