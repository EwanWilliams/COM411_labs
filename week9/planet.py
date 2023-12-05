from human import Human
from robot import Robot

class Planet:

    def __init__(self, name="Planet"):
        self.name = name
        self.inhabitants = {
            "humans" : [],
            "robots" : []
        }
    
    def __repr__(self):
        return f"planet(name={self.name}, humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"
    
    def __str__(self):
        return f"Planet name is {self.name}, there are {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."
    
    def add_human(self, human):
        self.inhabitants["humans"].append(human)
    
    def remove_human(self, human):
        self.inhabitants["humans"].remove(human)
    
    def add_robot(self, robot):
        self.inhabitants["robots"].append(robot)
    
    def remove_robot(self, robot):
        self.inhabitants["robots"].remove(robot)



if __name__ == "__main__":
    test_planet = Planet("Earth")
    test_human = Human("Fuck")

    print(test_planet)
    test_planet.add_human(Human())
    test_planet.add_human(test_human)
    test_planet.add_robot(Robot())
    print(repr(test_planet))
    print(test_planet)
    test_planet.remove_human(test_human)
    print(test_planet)
