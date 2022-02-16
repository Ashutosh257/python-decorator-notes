
import functools

# for file: 3-argument-decorator.py
def do_twice(func):
    #* we use args, kwargs to make the wrapper function flexible 
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


# for file: 4-return-value-from-decorator.py
def greet_twice(func):
    def wrapper_greet_twice(*args, **kwargs):
        #? when first time the 'greet' function is called, it prints and then returns the string
        #? the string comes here but there is no print statement or a variable to store in! 
        #? hence the value is lost and line:18 is invoked  
        #! if we add return before the below function then it will stop the execution of the wrapper and wont proceed any further   
        func(*args, **kwargs)
        #* the decorator eats the value if the second function doesn't return!
        #? here the 'greet' function is called again. 'Creating is printed'. the string 'Hello name' is returned
        #? the string comes here and is returned further to line:12 in "4-return-value-from-decorator.py" file    
        return func(*args, **kwargs)
    return wrapper_greet_twice   



# for file: 5-maintain-og-value-of-decorator.py 
def greet_twice_preserve_og_func(func):
    #? To fix this, decorators should use the @functools.wraps decorator. 
    #? It preserves the information about the original function.  
    @functools.wraps(func)
    def wrapper_greet_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_greet_twice   