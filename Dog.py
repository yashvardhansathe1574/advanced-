# Import the Animal class from Animal.py
from Animal import Animal


# Dog is a child class of Animal
class Dog(Animal):
    pass


# Main program
if __name__ == "__main__":
    # Create an object of Dog
    dog = Dog()

    # Call inherited methods from Animal
    dog.sound()
    dog.test()