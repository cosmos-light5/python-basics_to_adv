#function 
""" -block of reusable code designed to perform a specific task
    -enhance code modularity, readability and maintainability by allowing you to breakdown complex problems into smaller and manageable units
    -defined using keyword 'def' followed by name, parenthesis and a colon
    -function's body is indented below the definition line
    -e.g. print(), random(), type(), range(),..."""

def greet():
    print("hello world \nWelcome!")

greet()

#Arguments and parameters
""" -Parameters are the variables listed in the function definition
    -Arguments are the values that are passed the function when it's called
     """

def greets(f_name,l_name):              #here f_name and l_name are parameters i.e. variables
    print(f"hello {f_name} {l_name}")
    print("Welcome")

greets("Michel","Danny")                #here Michel and Danny are arguments passed to the function
greets("Prakash","Thapa")
greets("Taka","Noboru")

input=("enter greeting: ")
def greets(f_name,l_name, greeting):
    print(f"{greeting} {f_name} {l_name}")
    print("Welcome")

greets("Michel","Danny","Ola,")
greets("Prakash","Thapa","Jhorle,")
greets("Taka","Noboru", "konichiwa,")

#Parameters
""" -input variable that you define for a function
    -argument is an actual value for the parameters """

def get_greeting(name):
    return f"hi {"name"}"

message = get_greeting("john")
print(message)


def increment(number, by=1):
    return number + by
increment(10)


#functoin (*number)     -->* paxadi ko lai args vaninxa

def product(*num):
    print(num)
    prod=1
    for i in num:
        print(i)
        prod*=i
    return prod
    
product(10,20, 30, 40,50, 6,7,8,3)