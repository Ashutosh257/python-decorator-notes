# python3 1-simple-decorator.py

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper

# the function that we have to pass as an argument
def say_hello():
    print("Hello!")

# decorating the function: say_hello
#? We can assign the value to a random variable as well 
random_variable = my_decorator(say_hello)
random_variable()

#? random_variable is referenced to the wrapper function 
print(f"random_variable ref: {random_variable}")

print('------------------------------------------------------------')

#? we can also assign the decorator to the same variable name as the function which we pass as an argument to the decorator
say_hello = my_decorator(say_hello)
say_hello()


#? say_hello is referenced to the wrapper function as well
print(f"say_hello ref: {say_hello}")

