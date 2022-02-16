
#? functions are first class objects meaning they can be passed as arguments to functions just like any other objects


def say_hello(name):
    return f"Hello: {name}"

print(f"{say_hello('Ash')}")

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

print(f"{be_awesome('Dan')}")

# these are two separate functions and stored at different memory addr.
print(f"say_hello: {say_hello}")
print(f"be_awesome: {be_awesome}")

print('------------------------------------------------------------')

# We can add functions to list just like we add variables 
my_list = [say_hello, be_awesome]

# __name__: provides name of the object which calls/triggers it
print(f"my_list[0]: {my_list[0].__name__}")

# this proves that even functions are first class objects and can be passed to other functions as arguments
print(f"{my_list[1].__name__}: {my_list[1]('Ash')}")

print('------------------------------------------------------------')



def greet(func):
    return func("Bob")

# here we send 'say_hello' function as an argument without the parenthesis
# the argument holds the memory address of 'say_hello' function defined above 
# so basically the address is sent which is stored in a temp arg: 'func' making 'say_hello' and 'func' pointing at same addr.   
# and later func is invoked 
print(f"{greet(say_hello)}")