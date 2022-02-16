# python3 4-return-value-from-decorator.py

from decorate import greet_twice


@greet_twice
def greet(name):
    print("Creating!")
    return f"Hello {name}"


print(greet("Ash"))

print('------------------------------------------------------------')

hi_ash = greet("Ash")
print(f"hi_ash: {hi_ash}")
