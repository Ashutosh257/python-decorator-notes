# python3 5-maintain-og-value-of-decorator.py

from decorate import greet_twice_preserve_og_func


@greet_twice_preserve_og_func
def say_whee():
    print("Whee!")


say_whee()
print(f"say_whee: {say_whee}")
print(f"say_whee.__name__: {say_whee.__name__}")
