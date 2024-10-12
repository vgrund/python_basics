#iterating over lists
langs = ["Python", "C#", "Javascript", "Java"]

for lang in langs:
    print(f"language: {lang}")

#what if we need the index?
print("*" * 10)

print("The language rank is:")
for idx in range(len(langs)):
    print(f"# {idx+1}. {langs[idx]}")

#nested lists
print("*" * 10)

couples = [
    ["Beyonce", "Jay-Z"],
    [ "Johnny", "June"],
    ["John", "Yoko"],
    ["Will", "Jada"]
]

print(couples)
print(couples[1])
print(couples[1][0])

#iterating
print("*" * 10)

for couple in couples:
    print(couple)
    for person in couple:
        print(f"Sending invite to... {person}")