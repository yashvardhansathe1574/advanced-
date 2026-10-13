class MagicMethods:

    def __init__(self):
        pass

    def __init__(self, start=0):      # Magic Method
        self.input_start(start)

    def __init__(self, start=0, end=0):
        self.input_start(start, end)

    def input_start(self, start=0):
        end = 100
        for no in range(start, 101):
            print(no, end=" ")

    def input_start(self, start=0, end=50):   # Overloading
        for no in range(start, end + 1):
            print(no, end=" ")


if __name__ == "__main__":      # Boundary of magic method
    x = MagicMethods()
    print("Next Line")
    y = MagicMethods(5, 50)