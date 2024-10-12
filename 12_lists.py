print(type([]))

#lists can hold any type in a mixed way
print("*" * 10)

stuff = [4, 5.6, True, False, [], 'hi']
print(stuff)

#tranform a string to a list
print("*" * 10)

print(list("hello"))

#accessing data in lists
print("*" * 10)

print(stuff[1])

#get the last item
print("*" * 10)

print(stuff[-1])

#the length 
print("*" * 10)

print(len(stuff))

#updating elements
print("*" * 10)

print(stuff[5])
stuff[5] = "bye"
print(stuff[5])

#add a new item to the list
print("*" * 10)

print(stuff)
stuff.append("new item")
print(stuff)

#append a list/iterable to another
print("*" * 10)
new_list = [2.1, -5, "apple"]

print(stuff)
stuff.extend(new_list)
print(stuff)

stuff.extend("abc")
print(stuff)

#insert an item in a specific position of a list
print("*" * 10)

print(stuff)
stuff.insert(1, "inserted")
print(stuff)

#slices
print("*" * 10)

print(stuff[3:7])

print(stuff[7:])

print(stuff[:5])

print(stuff[::2]) #from the begining skip 1

nums = [4, 5, 6, 7]
print(nums)
print(nums[1:3])
nums[1:3] = ['a', 'b', 'c', 'd']
print(nums)
nums[1:5] = [5, 6]
print(nums)

#clear a list
print("*" * 10)

print(nums)
nums.clear()
print(nums)

#remove the first match
print("*" * 10)
stuff.append(5.6)
print(stuff)
stuff.remove(5.6)
print(stuff)

#remove just the last element
print("*" * 10)

print(stuff)
last_element = stuff.pop()
print(last_element)
print(stuff)

a_element = stuff.pop(1) #pop can remove an item in an index
print(a_element)
print(stuff)

#del keyword
print("*" * 10)

print(stuff)
del stuff[-1]
print(stuff)

del stuff[2:]
print(stuff)
