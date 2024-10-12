#local scope don't apply to loop or conditional
for char in "OCTOPUS":
    color = "magenta"
    print(char)

if True:
    animal = "Osprey"

print("AFTER LOOP", color)
print("AFTER CONDITIONAL", animal)

#but it does to functions
print("*" * 10)

def func():
    a = 10
    print(a)

print(a)