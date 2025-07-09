def greet(name):
    print(f"Hello, {name}")
    
greet("Sphe")    



# return value
def add(a, b):
    return a+b
result = add(2,4)
print(result)

#factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet1(name, greeting="Hello"):
    print(f"{greeting}, {name}")
        
greet1("Zee", "Good Afternoon") 

       