
#* Everything in python is an object! Even classes


def add_one(number):
    """ Adds one to number
    
    Arguments:
        number (int): number 
    
    Returns: 
        int: returns number+1
    """
    return number+1

print(f"add_one: {add_one}")
print(f"add_one(): {add_one(3)}")

# memory address of "add_one" is stored in "add_one_also", any changes made will 
# affect both since they are pointing the same object in memory addr.
add_one_also = add_one

print(f"add_one_also: {add_one_also}")
print(f"add_one_also(): {add_one_also(7)}")



