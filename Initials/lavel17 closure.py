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




#decorator
""" -are powerful and flexible features in python that allows you to modify and enhance functions and methods without changing theit code
    -they follow the principle of open/closed i.e codes should be open for extension but closed for modification. This means that you can add new functionality to existing functions without changing their source code, which promotes code reusability and separation of concerns.
    -It is a higher-order function that takes another function as an argument, adds some functionality and returns a new function withou modifying the original function code. 
    -Decorators are often used to add functionality, such as logging, timing, or access control, to existing functions in a clean and reusable way. 
    syntax:
    @decorator_name
    def decorator(func):
      pass
      
      Alternatively,
      function_to_be_decorated=decorator_name(function_to_be_decorated)
      """


def my_decorator(func):                 #yaha 'func' can be replaced with any name, matra parameter ho that represents the function being decorated.
  def wrapper(*args, **kwargs):
    print(f"Arguments: {args}, keyword arguments: {kwargs}")
    result = func(*args, **kwargs)  
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


#scope in python

""" -scope is the region of a program where a variable is defined and can be accessed. 
    -It determines the visibility and lifetime of variables in a program. 
  There are four types of scope in Python:
    -local scope: variables defined inside a function are in the local scope and can only be accessed within that function.
    -enclosing scope: variables defined in the enclosing function (the outer function) can be accessed by the inner function (the nested function) but not by the outer function itself.
    -global scope: variables defined at the top level of a module or script are in the global scope and can be accessed from anywhere in the program.
    -built-in scope: variables and functions that are built into Python are in the built-in scope and can be accessed from anywhere in the program without needing to import any modules.
  LEGB rule: 
      when you try to access a variable, Python follows the LEGB rule to determine where to look for the variable:
        -Local: Python first looks for the variable in the local scope (inside the current function).
        -Enclosing: If the variable is not found in the local scope, Python looks for it in the enclosing scope (the outer function).
        -Global: If the variable is not found in the enclosing scope, Python looks for it in the global scope (the top level of the module).
        -Built-in: If the variable is not found in the global scope, Python looks for it in the built-in scope (the standard library). If the variable is not found in any of these scopes, a NameError is raised.
        """
#global variable jahile top mai lekhne..


#lambda function: 
""" -a lambda function is a small anonymous function defined using the lambda keyword
    -can take any number of arguments but can only have one expression
    - are often used for short, simple operations that can be defined in a single line of code.
     -syntax: lambda arguments: expression"""


say_hello=lambda:"Hello world"
print(say_hello())                      #print garda variable name paxi () rakhne because tyo lambda function baneko hunxa..


max=lambda x,y: x if x>y else y
#max=lambda a,b:max(a,b)   # built in function lai lambda function ma rakhna mildaina, because lambda function ma expression matra hunxa, tyo built in function call garna mildaina..
print(max(10,20))           #best for DSA, because we can use lambda function as a key in sorting, filtering, etc..






numbers=[1,2,3,4,5,6,7,8,9,10]
greater_than_five=list(filter(lambda x:x>5, numbers))
print(greater_than_five)

words=['hi','hello','bye','good_bye','yes','no']
more_than_three=list(filter(lambda word:len(word)>3, words))
print(more_than_three)

word_with_h=list(filter(lambda word:"h" in word, words))
print(word_with_h)