class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy
    
    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"
    
    def __str__(self):
        return f"Human {self.name} is {self.age} years old and has {self.energy} energy."
    
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
