#accepting any number of arguments using "*"
def average(*args):
    print(type(args)) # "*" collects all arguments as a tuple
    total = 0
    for arg in args:
        total += arg

    return total / len(args)

print(average(1,2,3,4,5,6,7,8,9,10))

# "**" creates a dictionary with "n" number of key/value pairs
print("*" * 10)

def print_ages(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
            print(f"{k} is {v} years old")

print_ages(max=67, sue=59, kim=14)

#order matter
# parameters => *args => default parameters => **kwargs
print("*" * 10)

def func(person, *args, status="single", **kwargs):
     print(f"person is: {person}")
     print(f"status is: {status}")
     print(f"args is: {args}")
     print(f"kwargs is: {kwargs}")

func("colt", 1,2,3,4,5, age=82, mood="thrilled")
print("**")
func("colt", 1,2,3,4,5, status="married", age=82, mood="thrilled")

#mutable object is reused
print("*" * 10)

def add_twice(val, lst=[]):
     lst.append(val)
     lst.append(val)
     return lst

print(add_twice(7))
print(add_twice(5)) #as we can see, the same list reference in memory is used

#to solve that, if we don't want that behavior we could set the default value to None...
def add_twice_v2(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst

print(add_twice_v2(7))
print(add_twice_v2(5))

#if we have a list and a "*arg" function, we could use "*" to unpack the list
print("*" * 10)

nums = [1, 2, 3, 4, 5]

print(*nums)
print(average(*nums))
