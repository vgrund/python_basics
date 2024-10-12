#variable is available in nested functions
def outer():
    animal = "Bird"
    def inner():
        print("INSIDE INNER FUNC: ", animal)
    inner()

outer()