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
    -outer function le inner function return garne wa memorize garne function rakhe ko variable call garne
    """

def power_raiser(x):
  def inner_value(y):
    return x**y
  return inner_value

square=power_raiser(2)            #power_raiser() returns the inner_value function with x=2, which is assigned to square
cube=power_raiser(3)              # vaneko paila inner function lai memory ma store garne argument diyinxa as 1st variable ko value (here x) ani paxi diyeko value y ma basera compute hunxa

print(square(2))
print(cube(3))