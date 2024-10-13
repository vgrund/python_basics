from models.canine import Dog

dog = Dog("Joe", "Husky", 123)

print(type(dog))
print(isinstance(dog, Dog))

print(dog)
print(dog.name)
print(dog.breed)
print(dog.location)
print(dog.tricks)

print("*" * 10)
dog.learn_trick("sit")
print(dog.tricks)

print("*" * 10)
dog.bark()

print("*" * 10)
dog.perform_trick("sit")
dog.perform_trick("stay")

print("*" * 10)
print(dog.species)
print(Dog.species)

#class method is similar to a static method in C#. Any change to these method values affect only the class not the instances
print("*" * 10)
second_dog = Dog.register_stray()
print(second_dog.name)
print(second_dog.location)
print(dog.name)
