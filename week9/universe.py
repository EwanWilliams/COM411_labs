from planet import Planet
from human import Human
from robot import Robot
from matplotlib import pyplot as plt
import random

class Universe:

    def __init__(self):
        self.planets = []
    
    def __repr__(self):
        return f"universe(planets={self.planets})"

    def __str__(self):
        return f"The universe contains {len(self.planets)} planets."
    
    def generate(self):

        new_planet = Planet(f"Planet{random.randint(1, 10000)}")

        for i in range(random.randint(1, 100)):
            new_planet.add_human(Human(f"human{i}"))
        for i in range(random.randint(1, 100)):
            new_planet.add_robot(Robot(f"robot{i}"))

        self.planets.append(new_planet)
    

    def show_populations(self, selection=""):
        x = []
        y = []

        if selection == "humans" or selection == "robots":
            label = selection
            for planet in universe.planets:
                y.append(len(planet.inhabitants[selection]))
                x.append(planet.name)
        else:
            label = "total"
            for planet in universe.planets:
                y.append((len(planet.inhabitants['humans']) + len(planet.inhabitants['robots'])))
                x.append(planet.name)
            
        plt.bar(x, y)
        plt.xlabel("Planets")
        plt.ylabel(f"{label} population")
        plt.tight_layout()
        plt.savefig(f"{label}_pop_plot.png")
        plt.close()


if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    universe.generate()
    universe.generate()

    print(universe)
    #print(repr(universe))
    universe.show_populations("humans")
    universe.show_populations("robots")
    universe.show_populations()
