# function returning function

def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func 

# var = outer_func()
# var()

def outer_func2(msg):
    def inner_func2():
        print(f"massag is {msg}")
    return inner_func2()
var = outer_func2('hello there !')