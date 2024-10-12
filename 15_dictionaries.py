#dictionary type
empty_dict = {}
print(type(empty_dict))

#keys can be any immutable type: numbers, strings, booleans, etc
#values can be whatever we want
print("*" * 10)

movie = {"title": "Amadeus", "imdb_score": 8.3}
print(type(movie))
print(movie)

#accessing data
print("*" * 10)

print(movie["imdb_score"])

#adding and updating data
print("*" * 10)

movie["title"] = movie["title"].upper()
print(movie)

movie["rating"] = "R"
print(movie)

#check if a key exists whithin dict
print("*" * 10)

prices = {
    "blueberries": 1.10,
    "watermellon": 5.15,
    "strawberry": 3.45,
    "coconut": 6.49
}

shopping_list = ["blueberries", "coconut", "orange"]

#in version
for item in shopping_list:
    if item in prices:
        price = prices[item]
        print(f"{item} is ${price}")
    else:
        print(f"I don't have {item} today")

#get version
print("*" * 10)

for item in shopping_list:
    price = prices.get(item)
    if price:
        print(f"{item} is ${price}")
    else:
        print(f"I don't have {item} today")

#removing itens
print("*" * 10)

print(prices)
item = prices.pop("strawberry")
print(item)
print(prices)

print("*" * 10)
print(prices)
item = prices.popitem() #remove the last item
print(item)
print(prices)

print("*" * 10)
print(prices)
del prices["watermellon"]
print(prices)

print("*" * 10)
print(prices)
prices.clear()
print(prices)

#mutable
print("*" * 10)

stuff = {
    "a": 1,
    "b": 5
}

stuff2 = stuff.copy()

print(stuff is stuff2) #diferent objects in memory
print(stuff == stuff2) #same value

#mergin dictionaries
print("*" * 10)

d1 = {"a": 1, "b": 2, "c":3}
d2 = {"a": 4, "d": 5, "e":6}

print(d1)
print(d2)
merged_dic = {**d1, **d2}
print(merged_dic)
print(d1)
print(d2)

#we could also call update
print("*" * 10)
d1.update(d2)
print(d1)
print(d2)

#dict union
# "|" operator returns a new dict containing the items from the left and the right dicts.
# In the case of duplicated keys, the right side wins
print("*" * 10)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4, "a": 10}
dict3 = dict1 | dict2

print(dict3)

