#define a function
def laugh():
    print("HA"*10)

laugh()

#define a function with argument
print("*" * 10)

def sum(a, b):
    print(a + b)

sum(5, 3)

#define a function that returns a value
print("*" * 10)

def is_even(num):
    return num % 2 == 0

result = is_even(8)
print(result)

#define a function that has a optional argument
print("*" * 10)

def slugify(phrase, sep = "-"):
    return phrase.lower().strip().replace(" ", sep)

print(slugify("hello world horse face"))
print(slugify("hello world horse face", "_"))

#define a function - named arguments
print("*" * 10)

def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))

get_total(price=9.75, discount=0.5, qty=5, tax=0.01)
