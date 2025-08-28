# Assignment 1: Design Your Own Class

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"
import inspect
print("Smartphone ___init___ signature:")
inspect.signature(Smartphone.__init__)

# Inherited class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        # Call the parent constructor
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def get_info(self):
        # Override the parent method (Polymorphism)
        return f"{super().get_info()}, Cooling System: {self.cooling_system}"

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} with advanced cooling!")


# Activity 2: Polymorphism Challenge

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def move(self):
        print("The dog is running on four legs.")


class Bird(Animal):
    def move(self):
        print("The bird is flying in the sky.")


class Fish(Animal):
    def move(self):
        print("The fish is swimming in the water.")


# Driver Code
if __name__ == "__main__":
    # Assignment 1 demo
    phone1 = Smartphone("Samsung", "S23", 256)
    phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, "Liquid Cooling")

    print(phone1.get_info())
    phone1.call("123-456-789")

    print(phone2.get_info())
    phone2.play_game("PUBG")

    print("\nPolymorphism Challenge:")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()