def say_hi():
    print("say hello")
    
def plus_two(n):
    def minus_two(n):
        return n-2
    result = minus_two(n)
    return result
    
    
if __name__ == "__main__":
    say_hi()

    hello = say_hi
    hello()
    print(type(hello))
    print(type(hello()))
    print(plus_two(4))
  