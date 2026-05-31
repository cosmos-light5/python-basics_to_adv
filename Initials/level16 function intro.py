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




""" 
#Types of function
    - perform a task     #eg. print() inside functon is a perform a task type and returns nothing just performs the coded task 
                                i.e. something equals print() garera lekhnu pardainxa print() aafai le kam garxa
    - return a value     #function where functons e.g. .round() takes argument in it and pass to the variable that is made 
                                equal to .round() i.e round() le something value return garne raixa ra aarko variable ma pass garxa wa sidhai print garna use hunxa
      """

def get_greeting(name):
    return f"hi {"name"}"           #here return is a return type function as it passes the comments from get_greetings to the invoked units 

message = get_greeting("john")
print(message)                      #print() is a perform a task type function as it just prints on code execution and returns no thing to the functions or other units.. 

""" # all functions by default returns null """

#Returning Multiple values
def calculate(x,y):
    sum=x+y
    diff=x-y
    product=x*y
    quotient=x/y
    return sum, diff, product, quotient                 #return ma vayeko sum, diff, product, quotient  function vitra ko sanga match hunxa tara function bahira ko chai any supposition hunasakxa

sum, diff, product, quotient=calculate(10,5)            #tarayaha ko sum, diff, product, quotient  chai farak ho print ko lagi reference banayeko matra ho
print(f"add: {sum}, sub:{diff}")                        #sum, diff, product, quotient  ko satta s,d,p,q = calculate(10,5) pani garna milxa function bahira ko lai

result=calculate(10,5)
print(result)               #multiple print garna ko lagi ra yesle tuple ko form ma dinxa



#diaplay as given output
num=int(input("Enter a number: "))

def fizz_Buzz(num):
  if num%3 == 0 and num%5 == 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    print("Fizz_Buzz")
  elif num%5 ==0:
    print("Buzz")
  elif num%3 == 0:
    print("Fizz")
  else:
    print(num)

fizz_Buzz(num)                      #function lai call garna nabirsine

#or
def fizz_Buzz(num):
  if num%5 ==0:
    print("Buzz")
  if num%3 == 0:
    print("Fizz")
  if num%3 != 0 and num%5 != 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    print("num")
  
    print(num)

fizz_Buzz(15)  

#Or
def fizz_Buzz(num):
  if num%3 == 0 and num%5 == 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    return "num"
  if num%5 ==0:
    return "Buzz"
  if num%3 == 0:
    return "Fizz"
  
  return num

print(fizz_Buzz(15))  


#Default keyword and Defaulr arguments
""" -Default keyword have predefined values if no arguments are provided
    -keyword arguments are specified by parameter's name"""

def increment(number, by=1):            #here by=1 is default value, ...(..,..,10) here 10 is default value
    return number + by
increment(10)

#over writing default arguments
print(greet("hello", "bob"))


#functoin (*number)     -->* paxadi ko lai args vaninxa

def product(*num):
    print(num)
    prod=1
    for i in num:
        print(i)
        prod*=i
    return prod
    
product(10,20, 30, 40,50, 6,7,8,3)