import copy 

#concat two lists
evens = [2, 4, 6]
odd = [1, 3, 5]
concat = evens + odd
print(concat)

#repeat the list
print("*" * 10)

mult = [1, 2, 3] * 2
print(mult)

#search for a value
print("*" * 10)

colors = ["blue", "black", "purple", "white"]

response = input("What color would you like? ")

while response.lower().strip() not in colors:
    response = input("I don't know that color! Please try again: ")

print(f"Ok, you choose {response}")

#count
print("*" * 10)

print(mult)
count = mult.count(2)
print(count)

#reverse
print("*" * 10)

print(mult)
mult.reverse()
print(mult)

#sort
print("*" * 10)

print(mult)
mult.sort()
print(mult)

#lists are mutable
print("*" * 10)
a_list = [1, 2, 3]
a_list2 = a_list

print(id(a_list)) # id returns the position in memory
print(id(a_list2)) # the position are the same

a_list.append(4)
print(id(a_list)) # even when we change the list is changed the id remains the same
print(id(a_list2))

#comparing lists
print("*" * 10)
#use "==" to compare the contents
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
is_same_value = nums1 == nums2
print(is_same_value)

# use "is" to compare the identity/ location in memory
is_same_list = nums1 is nums2
print(is_same_list)

nums2 = nums1
is_same_list = nums1 is nums2
is_same_value = nums1 == nums2
print(is_same_list, is_same_value)

#split and join
print("*" * 10)

birthday = "01/06/2000"
splited = birthday.split("/")
print(splited)

joined = "--".join(splited)
print(joined)

#list unpack
print("*" * 10)

user = ["Joe", "Ed", "John", "Billy", "Ted"]
first, second, third, *losers = user
print(first)
print(second)
print(third)
print(losers)

item = [4, "Pizza", "Plain", 16.98]
quantity, *others, price = item # remaining values goes to "*" variable
print(quantity)
print(others)
print(price)

#shallow copy of lists
print("*" * 10)

list1 = [12, 9, 3, 7]
list2 = list1.copy()

print(list1)
print(list2)

print(list1 is list2)
print(list1 == list2)

list1 = [1, 2, [3, 4]]
list2 = list1.copy() # shallow copy

print(list1)
print(list2)
print(list1[2] is list2[2]) #the nested list is not a copy, they are the same in memory

list2 = copy.deepcopy(list1) #we need to import copy
print(list1[2] is list2[2]) #deepcopy make a copy of nested elements, now they are not the same in memory
