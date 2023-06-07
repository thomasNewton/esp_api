def plus_one(number):
    return number + 1
add_one = plus_one   # function is assigned to a variable , then called from its new name
add_one(5)


def plus_two(number):
    def sub_two(number):
        return number -2
    result = sub_two(number)
    return result
print(plus_two(4))
#print(sub_two(5))   will not find this funciton


# pass a function as a parameter into another funciton
def p_one(number):
    return number + 1

def function_call(function):
    number_to_add =6
    return function(number_to_add)

print(function_call(p_one))


# return a functon from another function  hello_funciton returns say_hi
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function() # hello is a variable we have assigned the funciton to
print(f"hello is a funciton {type(hello)} we can call it with hello()= {hello()}")

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)
    # message_sender is called, not returned by the outer funciton, 
    message_sender() #the inner has acces to outer params (message)

print_message("Some random message")

# Background concepts  --- now to make our first decorator

def uppercase_decorator(funcion):  # we will pass the 'decorated' funciton into the decorator
    def wrapper():
        func = funcion()  # new variable for the function that was passed in
        make_uppercae = func.upper()  # looks like its assuming function will have this method?
        return make_uppercae
    return wrapper   # returns a link to the wrapper method but does not run it

def say_hi():
    return 'hi there'
print(f"the say_hi method before decoator is added {say_hi()}")
decorate = uppercase_decorator(say_hi)  # now to call it use decorate() 
say_hi = decorate
print(f"aftrer decorator is applyed and say_hi is reassigned to the decorator {say_hi()}")
print(f"the decorator output if run directly {decorate()}")

# the @decorator syntax is shorthand for the above
@uppercase_decorator
def say_by():
    return "later gator"
# all done with the @ shorthand---
print(say_by())


def deco(function):
    def wrap(x,y,z):
        funct = function(x,y)
        add_mo = funct +z
        return add_mo
    return wrap

def addit(x,y):   # the original funciton takes 2 params
    return x+y    # but we 'decorated it' so that it now takes 3

addit = deco(addit)  # we could have also just used a new varable name 
print(addit(1,2,3))


@deco   # this does the same thing .. in one line  it will return (x*y)+z
def mult(x,y):
    return x*y

print(mult(20,3,4))

def cake(fun):
    def wrapper():
       fu=fun()
       return_value = fu +"more text"
       return return_value
    return wrapper



def greeting():
    s1=  input("enter first name ")
    s2 = input("enter last name ")
    output = f"Hello {s1} {s2}"
    return output


print(greeting())