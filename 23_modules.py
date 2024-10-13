# a module is simply a Python file that contains code that can be re-used in other files.
# modules allow us to break up complex programs into smaller, more manageable pieces across multiple files
# there are 3 main types Built-In (comes with Python), Custom (those we create) and 3rd Party (other people have written)

# https://docs.python.org/3/library/

# built-in modules
import random
import calendar
from math import cos, pi # from <module> import <method> - syntax to import specific pieces of a module

print(random.randint(1,10))
print(calendar.weekday(2024,10,13))
print(cos(45)) #from math module
print(pi) #from math module

#custom modules
import custom_modules.person_repository as person_repository
#could be...
#from custom_modules.person_repository import update

person_repository.update("Vinicius")

#3rd party modules
#we use pip to install 3rd party modules in our application
#python package repository website https://pypi.org/

#installing art package: python3 -m pip install art
import art

print(art.art("woman"))
print(art.art("coffee"))
print(art.art("random"))

print(art.text2art("Hello World"))

#python3 -m pip install translate
from translate import Translator

translator = Translator(to_lang="pt")
translation = translator.translate("Hi. How's you going?")
print(translation)
