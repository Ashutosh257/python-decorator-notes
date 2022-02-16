

def parent(num):
    
    # print("Inside parent")

    def first_child():
        return "first child invoked"

    def second_child():
        return "second child invoked"
    
    if num == 1:
        #? returns the reference(memory addr) of function 'first_child' 
        #? return first_child -> returns reference of it
        #? return first_child() -> the parenthesis will invoke the function and not return a reference 
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(3)

# will print the reference of functions inside 'parent'
print(f"first addr: {first}")
print(f"second addr: {second}")

print('------------------------------------------------------------')

# will print the refered functions inside 'parent'
# will return the stings inside first_child and second_child functions  
print(first())
print(second())