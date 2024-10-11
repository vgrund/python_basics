#while count to 10
count = 1
while count <= 10:
    print(f"Count: {count}")
    count += 1

#for
print("*" * 10)

word = "hello"
for char in word:
    print(char)

#for - range
print("*" * 10)
for num in range(10, 20, 4):
    print(num)

#for - break
print("*" * 10)

for letter in "abcdefghi":
    if letter == 'd':
        break
    print(letter)

#for - continue
print("*" * 10)

for letter in "abcdefghijlmnopqrstuvxyz":
    if letter in "aeiou":
        continue
    print (letter)