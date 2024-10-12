#dict of lists
test_scores = {
    "Bill": [80, 65, 70],
    "Paul": [50, 65, 35]
}

#list of dicts
waitlist = [
    {
        "email": "paul@gmail.com",
        "localtion": "Canada",
        "first_name": "Paul"
    },
    {
        "email": "bill@gmail.com",
        "localtion": "USA",
        "first_name": "Bill"
    }
]

#dict of dict
print("*" * 10)

produce = {
    "orange": {
        "price": 2.25,
        "qty": 20,
        "organic": True,
        "producer": "The farm"
    },
    "watermellon": {
        "price": 5.00,
        "qty": 5,
        "organic": True,
        "producer": "Happy Watermellon farm"
    }
}

print(produce["watermellon"]["producer"], produce["watermellon"]["price"])