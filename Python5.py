class Superhero:
    """Represents a superhero with a name, power, and catchphrase."""
    def _init_(self, name, power, catchphrase):
        """Initializes a Superhero object."""
        self.name = name
        self.power = power
        self.catchphrase = catchphrase

    def describe(self):
        """Prints a description of the superhero."""
        print(f"This is {self.name}!")
        print(f"Their amazing power is: {self.power}")
        print(f"And their catchphrase is: '{self.catchphrase}'")

    def use_power(self):
        """Demonstrates the superhero using their power."""
        print(f"{self.name} uses their incredible {self.power}!")

class Animal:
    """Represents a generic animal."""
    def move(self):
        """Defines a generic move action for animals."""
        print("This animal moves.")

class Car:
    """Represents a car."""
    def move(self):
        """Defines the move action for a car."""
        print("The car is driving.")

class Plane:
    """Represents a plane."""
    def move(self):
        """Defines the move action for a plane."""
        print("The plane is flying.")

def animal_actions(entity):
    """Demonstrates polymorphism by calling the move() method on different entities."""
    entity.move()

# --- Activity 1: Design Your Own Class (Superhero) ---
print("--- Activity 1: Superhero Class ---")
superman = Superhero("Superman", "Super Strength and Flight", "Up, up, and away!")
superman.describe()
superman.use_power()
print("-" * 30)

# --- Activity 2: Polymorphism Challenge ---
print("--- Activity 2: Polymorphism Challenge ---")
animal = Animal()
car = Car()
plane = Plane()

animal_actions(animal)
animal_actions(car)
animal_actions(plane)
print("-" * 30)