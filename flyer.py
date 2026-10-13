class Flyer:

    ROLLNO = 69 #global static

    def __init__(self):
        self.Name = "Chaitnya" #Instance

    def Fly(self):
        var = 10 #local
        return "Flying high in the sky!"

    def test():
        return "This is the test method."

if __name__ == "__main__":
    var = Flyer.test()
    print(var)