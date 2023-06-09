
# 1 rename a funciton
def add_self(number):
    return number+number
times_two = add_self


# 2 define an internal function

def why_bother(quote):
    def make_cap():
        return quote.capitalize()
    result = make_cap()
    return result





# 3 pass a funciton into another as a parameter

def add_two(x):
    return x+2

def outer_fucntion(function):
    num = 3
    fun = function (num)
    return fun

# 4 return a function as a return value from another funciton

def main_funciton():
    def inner_function():
        return 'value from inner funciton'
    return inner_function
the_inner_value = main_funciton()




def upper(funciton):
    def wrapper():
        fun = funciton()
        return f"Made upper case by the decorator {fun.upper()}"   
    return wrapper
@upper
def say_goodby():
    return "later gator"

print(say_goodby())