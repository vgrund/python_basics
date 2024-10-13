#like lists, tuples are ordered, indexed collections
#unlike lists, tuples are immutable. They cannot change once created

colors = ("purple",  "blue", "green", "black")
print(type(colors))

#empty tuple - although that no make sense, because once they are created, can't be changed
empty_tuple = ()
empty_tuple2 = tuple()
print(type(empty_tuple))
print(type(empty_tuple2))

#acessing elements
print("*" * 10)

print(colors[2])
print(colors[0:2]) # slices
print(colors.index("blue")) # index returns the index of a value
print(colors.count("purple")) # the count of a value

#iterating tuple
print("*" * 10)

for color in colors:
    print(color)

#tuples are immutable, but nested objects are not
print("*" * 10)

stuff =(1, 2, [])

print(stuff)
stuff[2].append('added') #first and second items are integers and can't be changed, but the list in the third position can be changed - it don't has to do with the index, but the type
print(stuff)

#why use tuples?
# * they are more efficient than lists <- How?
# * use them for data that shouldn't change
# * some methods return them like dict.items()
# * they can be used as keys in a dictionary
print("*" * 10)

tuple_as_key_in_dicts = {(2, 1): 'home', (10, 5): 'work'}
print(tuple_as_key_in_dicts)