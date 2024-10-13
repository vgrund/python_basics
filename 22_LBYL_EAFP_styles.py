# LBYL = Look Before You Leap
# Coding style where you explicitly test for pre-conditions before making calls or
#"leaping". Characterized by lots of if statements

def func_lbyl_style(year):
    if year.isnumeric(): # Look - Check to see if year is numeric
        year = int(year) # Leap - Convert year to int once we know it's safe
    else:
        year = 2024


# EAFP = Easier to Ask for Forgiveness than Permission
# Assume things exist or will work, and catch exceptions if you're wrong.
# Coding style characterized by lots of try/except blocks

# MORE PYTHONIC WAY OF DOING THINGS, although both are valid ways
def func_eafp_style(year):
    try:
        year = int(year) # assume it'll work and try converting year to int
    except ValueError: # catch exception if you're wrong
        year = 2024