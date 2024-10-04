color = "red"

# type string
print(type(color))

# string length
print("*" * 20)
print(len(color))

# interpolation
print("*" * 20)
print(f"Color is: {color}")

# concatenation
print("*" * 20)
print("A" + "B")

# string indexing
print("*" * 20)
print(color[1])
print(color[-1]) # last character
print(color[1:3]) # slices
print(color[:3]) # slices
print(color[2:]) # slices
print(color[0:5:2]) # slices with a step

# Null - Lack of value
print("*" * 20)
color = None
print(color)
color = "black"

# print a string repeated times
print("*" * 20)
print(color * 5)

# scape characters
print("*" * 20)
print("hello\nworld")
print("hello\tworld")
print("she said \"lol\"")

# multiline string
print("*" * 20)
print(""" 
abc
    def
ghi
"jlm"
""")