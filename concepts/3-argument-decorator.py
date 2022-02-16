# python3 3-argument-decorator.py

#* import do_twice decorator from 'decorate' file
from decorate import do_twice


@do_twice
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Ash")

@do_twice
def say_whee():
    print("Whee!")

say_whee()