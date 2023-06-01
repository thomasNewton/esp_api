import sys

def add_args(args):
    print(args)
    total = 0
    for x in args[1:]:
        total +=int(x)
    return total


def addup(*numbers):
    total = 0
    for i in numbers:
        if type(i) == (int or float):
            total += int(i)
        else:
            print(f"{i} is a: {type(i)}  cant be passed like this...")
    return total
    
    
def display_arg(*args, **kwargs):
    print( "args are:")
    for arg in args:
        print(arg)
    print("\nkwargs are:")
    for kwarg in kwargs:
        print(kwarg)
    
    

if __name__ == "__main__":
    args = sys.argv  # first arg is always the script itself  
    add1 = add_args(args)
    print(add1)
    
    # *  unpack operator ...loops through all params past like its a big list
    # first few can be set, with the rest variables
  
    print(addup(1,2))
    print(addup(1,2,3))
    print(addup(1,args)) # will not run rignt
    print(addup(*args)) # all the args are now strings but it evaluates each one
    
    a1 = "Bob"      #string
    a2 = [1,2,3]    #list
    a3 = {'a': 222, #dictionary
          'b': 333,
          'c': 444}
    
    display_arg(a1, a2, a3, param1=True, param2=12, param3=None)
    
    
