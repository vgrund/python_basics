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

#logical - AND, OR, NOT
print("*" * 10)

age = 19
if age > 18 and age < 21:
    print("You can enter the venue but cannot drink.")

day_of_week  = "saturday"
if day_of_week == "saturday" or day_of_week == "sunday":
    print("it's the weekend")
else:
    print("it's a workday")

year_born_in = input("what year were you born in?")

if not year_born_in.isnumeric():
    year_born_in = input("That isn't a number. Try again please. What year were you born in?")

year_born_in = int(year_born_in)

print(f"You were born {2024-year_born_in } years ago")