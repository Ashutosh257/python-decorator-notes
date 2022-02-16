# python3 2-better-syntax.py

def my_decorator(func):
    def wrapper(msg):
        print("before")
        func(msg)
        print("after")

    return wrapper

#* better way of writing "say_hello = my_decorator(say_hello)" by adding @my_decorator above the function which you want to decorate
@my_decorator
def say_hello(msg):
    print(msg)


#? we are basically reassigning or overwriting the 'say_hello' function by the 'wrapper' function of my_decorator
print(f"say_hello: {say_hello}")

say_hello("Using DECORATOR!")

print('------------------------------------------------------------')

def say_hellos(msg):
    print(msg)

#? lets say we do not wanna decorate a function then we just dont add the '@my_decorator' syntax
say_hellos("NOT Using DECORATOR!!")

