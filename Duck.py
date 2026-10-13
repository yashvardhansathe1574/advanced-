from swimmer import Swimer
#from filename import classname or method

class Duck(Swimer):
        def quack(self):
            return "Quack quack!"

if __name__ == "__main__" :
    object = Duck()
    var = object.quack()
    print(var)
    var = object.swim()
    print(var)