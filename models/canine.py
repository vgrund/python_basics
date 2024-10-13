class Dog:

    #class attributes
    species = 'canine'

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = set() # using a Set because we don't want repeated tricks and order doesn't matter

    @classmethod
    def register_stray(cls):
        return cls("coming soon", "unknown", "unknown")

    def bark(self):
        print(f"{self.name}: woof!")

    # "self" argument is always required, because behind the scenes Python will send a parameter
    def learn_trick(self, new_trick):
        self.tricks.add(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick}")
