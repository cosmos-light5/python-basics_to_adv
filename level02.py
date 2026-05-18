name= "Ram"
age=5
print("My name is {} and I am {} yrs old.".format(name , age))
print(f"My name is {name} and I am {age} yrs old.") #f-string is a string literal that is prefixed with 'f' or 'F'. It allows you to embed expressions inside string literals, using curly braces {}. The expressions inside the curly braces are evaluated at runtime and then formatted using the __formatt__ing__protocol. This makes it easier to create strings that include variable values or expressions without having to use concatenation or the format() method.
print("My name is ",name, "and I am", age, "yrs old.")