#formatted paramaters
name= "Ram"
age=5
print("My name is {} and I am {} yrs old.".format(name , age))
print(f"My name is {name} and I am {age} yrs old.") #f-string is a string literal that is prefixed with 'f' or 'F'. It allows you to embed expressions inside string literals, using curly braces {}. The expressions inside the curly braces are evaluated at runtime and then formatted using the __formatt__ing__protocol. This makes it easier to create strings that include variable values or expressions without having to use concatenation or the format() method.
print("My name is ",name, "and I am", age, "yrs old.") 
""" output:
My name is Ram and I am 5 yrs old.
My name is  Ram and I am 5 yrs old. """

#escape sequence
print("Hello \n world")
print("hello \tworld")
print("hello \\ world")
print("\'hello world\'")
""" output:
Hello 
 world
hello   world
hello \ world
'hello world'
 """

#inputs and arithmetic operations
num01=int(input("enter a number: "))
num02=int(input("enter a number: "))
add=num01 + num02
sub= num01 - num02
div= num01/num02
mod=num01%num02
expo=num01**num02
print("sum: {}\ndiff: {}\nquotient: {}\nremainder: {} \nexponential: {}".format(add, sub, div, mod, expo))

""" output:
enter a number: 4
enter a number: 2
sum: 6
diff: 2
quotient: 2.0
remainder: 0 
exponential: 16 """

#boolean and comparision operators
x=10
y=20
print("x==y ", x==y)
print("x!=y", x!=y)
print()
print("x<y :", x<y)
print("x>y :", x>y)
print("x<=y :", x<=y)
print("x>=y :", x>=y)

""" output:
x==y  False
x!=y True

x<y : True
x>y : False
x<=y : True
x>=y : False """

a = 2
b = 3
b += a

print("b = ", b)

b /= a #ceiling division
print("b = ", b)

b // a #floor division
print("b = ", b)

a=1
b=2
c=3
print (a,b,c)  #output--> 1 2 3
print(a,b,c, sep=",")  #output--> 1,2,3