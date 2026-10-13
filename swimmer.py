from flyer import Flyer
#from filename import classname or method
class Swimer(Flyer):
    def swim(self):
        return "Swimming deep in the water!"

if __name__ == "__main__" :
    object = Swimer()
    var = object.swim()
    print(var)
    var = object.Fly()
    print(var)
