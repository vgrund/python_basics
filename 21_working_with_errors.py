#common errors:
# * SyntaxError
# * IndexError
# * ValueError
# * NameError
# * TypeError
# * KeyError



#try/except
def save_price(price):
    try:
        converted = float(price)
        print(converted)
    except ValueError:
        print("Thas is not a valid price")

save_price("5.6")
save_price("a")

#chained excepts
print("*" * 10)

def divide(a, b):
    try:
        print(a/b)
    except TypeError:
        print("You entered an invalid number")
    except ZeroDivisionError:
        print("Only Black Holes can divide by zero")

divide(1,10)
divide(5, "a")
divide(10, 0)

#we can raise a exception whenever we want to
print("*" * 10)

def save_name(name):
    if name == "" or name is None:
        raise ValueError("Name has to have at least one character")
    print(name)

save_name("abc")
save_name("")