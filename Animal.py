# Define a class named Animal
class Animal:
    # Instance method to display the sound of an animal
    def sound(self):
        print("Animal Sound")

    # Instance method to display a test message
    def test(self):
        print("This is the test method")


# Main program execution starts here
if __name__ == "__main__":
    # Create an object (instance) of the Animal class
    animal = Animal()

    # Call the sound() method using the object
    animal.sound()

    # Call the test() method using the object
    animal.test()