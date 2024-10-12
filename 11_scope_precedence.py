#global variable is not changed by the function
#local variable is not the same to global
animal = "abc"
def outer():
    animal = "Bird"
    print("INSIDE FUNC: ", animal)

outer()
print("OUTSIDE FUNC: ", animal)

#global keyword - changing a global variable
print("*" * 10)

score = 100

def double_score():
    global score
    score *= 2

double_score()
print(score)