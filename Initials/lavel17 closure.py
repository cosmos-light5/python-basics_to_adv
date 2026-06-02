#closure: closure is a function object that has access to variables in its enclosing scope, even after the outer function has finished executing. It allows the inner function to remember and access the variables from the outer function, creating a "closure" around those variables.
""" -nested functon
    -remembers the value from the (enclosing) function's scope even after the function has finished executing
    -can access variables from the enclosing scope
    #key characteristics of closure:
         -remembering: closure remembers value in the scope
         Persistence: These values persist even after the outer function has finished executing
         -state:they can maintain state between function calls
         -Return: The outer function returns the inner function itself (not just it's result)"""

""" -nested function banaune
    -memory ma store garna function ma argument pass garne
    -outer function le inner function return garne wa memorize garne function rakhe ko variable call garne arguement pass garera
    """

def power_raiser(x):
  def inner_value(y):
    return x**y
  return inner_value

square=power_raiser(2)            #power_raiser() returns the inner_value function with x=2, which is assigned to square
cube=power_raiser(3)              # vaneko paila inner function lai memory ma store garne argument diyinxa as 1st variable ko value (here x) ani paxi diyeko value y ma basera compute hunxa

print(square(2))
print(cube(3))

#decorator: a decorator is a design pattern in Python that allows you to modify the behavior of a function or class method without changing its source code. It is a higher-order function that takes another function as an argument and extends its behavior without explicitly modifying it. Decorators are often used to add functionality, such as logging, timing, or access control, to existing functions in a clean and reusable way.


def my_decorator(func):
  def wrapper(*args, **kwargs):
    print(f"Arguments: {args}, keyword arguments: {kwargs}")
    result = func(*args, **kwargs)  # Call the original function
    print("function execution completed")
    return result
  return wrapper

@my_decorator
def add(a,b, extra_no):
  return a + b + extra_no

@my_decorator
def greet(name):
  return f"Hi, {name}"

@my_decorator
def multiply(a,b, extra_no):
  return a * b * extra_no

print(add(3,5, extra_no=10))
print(greet("Alo"))
print(multiply(4,2, extra_no=11))