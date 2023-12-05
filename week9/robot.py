class Robot:
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    def __init__(self, name="Robot", energy=0):
        self.name = name
        self.energy = energy
        self.age = 0

    def __repr__(self):
        return f"robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old and has {self.energy} energy."

    @staticmethod
    def the_laws():
        print(Robot.laws)

    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1
    
    def eat(self, amount):
        self.energy += amount
        if self.energy > self.MAX_ENERGY:
            self.energy = self.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0
