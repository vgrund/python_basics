color = input("What is the color?")

if color == "green":
    print("BEGINNER") # must be idented or it'll not work
elif color == "blue":
    print("INTERMEDIATE")
elif color == "black":
    print("ADVANCED")
else:
    print("COLOR NOT VALID")

# nesting conditional
print("*" * 10)
if "light" in color:
    if "blue" in color:
        print(f"{color} is a beatiful color")
    elif "purple" in color:
        print(f"{color} is my favorite color")
    else:
        print("This color should be nice")
elif "dark" in color:
    if "blue" in color:
            print(f"{color} is a nice color")
    elif "purple" in color:
        print(f"{color} is a wonderful color")
    else:
        print("This color should be nice")
else:
    print("The color should be Light or Dark")