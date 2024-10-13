class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!")

class Lion(Cat):
    def __init__(self, name, pride_name):
        #instead of set name like the line below...
        #self.name = name

        #we can call de Cat's init function using "super()", that way we reuse code
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars!")
