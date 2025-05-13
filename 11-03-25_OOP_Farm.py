
from abc import ABC, abstractmethod

# Base Animal class (Abstract)
class Animal(ABC):
    def __init__(self, name, age):
        self._name = name          # encapsulated attribute
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        print(f"{self._name} is being fed!")

    def get_name(self):
        return self._name

    def get_species(self):
        return self.__class__.__name__

# Subclasses
class Cow(Animal):
    def make_sound(self):
        print("Moo!")

    def milk(self):
        return "Milk"

class Chicken(Animal):
    def make_sound(self):
        print("Cluck!")

    def lay_egg(self):
        return "Egg"

class Sheep(Animal):
    def make_sound(self):
        print("Baa!")

    def shear(self):
        return "Wool"

# FarmStructure class
class FarmStructure:
    def __init__(self, name, structure_type):
        self.name = name
        self.structure_type = structure_type

    def describe(self):
        return f"{self.name} ({self.structure_type})"

# Farm class
class Farm:
    def __init__(self, name):
        self.name = name
        self._animals = []
        self._structures = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)

    def add_structure(self, structure):
        self._structures.append(structure)

    def remove_structure(self, structure):
        if structure in self._structures:
            self._structures.remove(structure)

    def show_population(self):
        print(f"Welcome to {self.name}!")
        print("Farm Population:")
        counts = {}
        for animal in self._animals:
            species = animal.get_species()
            counts[species] = counts.get(species, 0) + 1
        for species, count in counts.items():
            print(f"- {species}: {count}")

    def list_structures(self):
        print("Structures:")
        for structure in self._structures:
            print(structure.describe())

    def daily_routine(self):
        print("----- Morning Routine ------")
        products = []
        for animal in self._animals:
            animal.feed()
            animal.make_sound()
            if isinstance(animal, Cow):
                products.append(animal.milk())
            elif isinstance(animal, Chicken):
                products.append(animal.lay_egg())
            elif isinstance(animal, Sheep):
                products.append(animal.shear())
        print("Collected products:", ", ".join(products))

# Demo setup
if __name__ == "__main__":
    my_farm = Farm("The Belval Farm")

    # Adding animals
    my_farm.add_animal(Cow("Bessie", 5))
    my_farm.add_animal(Cow("MooMoo", 3))
    my_farm.add_animal(Chicken("Clucker", 1))
    my_farm.add_animal(Chicken("Feathers", 2))
    my_farm.add_animal(Chicken("Eggy", 1))
    my_farm.add_animal(Sheep("Wooly", 4))
    my_farm.add_animal(Sheep("Fluffy", 2))
    my_farm.add_animal(Sheep("Bouncer", 3))
    my_farm.add_animal(Sheep("Cotton", 1))
    my_farm.add_animal(Sheep("Sheepy", 5))

    # Adding structures
    my_farm.add_structure(FarmStructure("Red Barn", "Barn"))
    my_farm.add_structure(FarmStructure("Hen Palace", "Coop"))

    # Display info
    my_farm.show_population()
    print()
    my_farm.list_structures()
    print()
    my_farm.daily_routine()
