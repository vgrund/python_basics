scores = {
    "team a": 90,
    "team b": 64,
    "team c": 72,
    "team d": 20,
    "team e": 56,
    "team f": 38
}

#keys, values, items
print(scores.keys())
print(scores.values())
print(scores.items())

for team in scores.keys():
    print(team)

for score in scores.values():
    print(score)
    
for team, score in scores.items():
    print(f"The team \'{team}\' score is {score}")