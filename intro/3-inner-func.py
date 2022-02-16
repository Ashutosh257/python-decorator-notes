
# We can write functions inside another functions


def parent():
    
    print("Inside parent")

    def first_child():
        print("first child invoked")

    def second_child():
        print("second child invoked")
    
    second_child()
    first_child()


parent()

# now if we try to print first_child or second_child 
# we get an error since the scope of those functions is inside the parent function
# will give error on invocation

# first_child() 


#?? Both of them reside inside of parent(), locally. 
#?? What if you wanted to access functions that live inside another function?
#?? Can you return them out of an existing parent function? 
#?? Get them out of the local scope, and be usable outside of it? 