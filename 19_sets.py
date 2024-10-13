#sets are unordered collections with no duplicate elements
#they accept only immutable elements
#we can...
# * add and delete elements
# * iterate over elements
# * check to see if element is in a set
# * use set operatos: union, intersection, etc

stuff = {2, 4, 6, 8, True, 'abc', 4.5}
print(type(stuff))

empty_set = set()
print(type(empty_set))

#only unique values are accepted
print("*" * 10)

evens = {8, 2, 4, 6, 2, 4}
print(evens)

#adding elements
print("*" * 10)

print(evens)
evens.add(10)
print(evens)
evens.add(-2)
print(evens)

#length
print("*" * 10)

print(len(evens))

#remove
print("*" * 10)

evens.remove(6)
print(evens)

#discard works similar to remove but it won't return an error when the element doesn't exist, but remove does
print("*" * 10)

print(evens)
evens.discard(998)
print(evens)

#clear
print("*" * 10)

print(evens)
evens.clear()
print(evens)

#they are mutable, so when we compare two sets...
print("*" * 10)

print({1, 2, 3} is {1, 2, 3}) #different allocation in memory
print({1, 2, 3} == {1, 2, 3}) #same value

#checking if a value is inside a set
print("*" * 10)

print(3 in {1, 2, 3})
print(5 in {1, 2, 3})

#iterating a set
print("*" * 10)

evens = {8, 2, 4, 6, 2, 4}
for num in evens:
    print(num)

#set operators - intersection, union, difference
print("*" * 10)

#intersection
grocery_items = {"pasta", "orange", "watermellon", "ice cream", "salad"}
my_shopping_list = {"watermellon", "pasta", "salad", "strawberry", "milk"}

itens_i_could_buy = grocery_items & my_shopping_list #intersection
print(itens_i_could_buy)

#union
all_items = grocery_items | my_shopping_list #union
print(all_items)

#difference - will return items that are in left side and that are not in the right side
items_i_couldnt_buy = my_shopping_list - grocery_items #difference
print(items_i_couldnt_buy)

#we can use methods instead operators
print("*" * 10)

print(grocery_items.intersection(my_shopping_list))
print(grocery_items.union(my_shopping_list))
print(my_shopping_list.difference(grocery_items))

#why use sets?
# * sets make it very easy/fast to check if a value exists in a collection
# * sets are an easy way to remove duplicates from a collection

8 in {2, 4, 6, 8} # is more efficient than...
8 in [2, 4, 6, 8]

#that happens because behind the scenes, python must iterating over the list
#it doesn't happen in sets
