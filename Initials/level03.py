#conditional statements (if, elif, else):

#to check of the no. is positive or negeative or zero
""" x=int(input("please enter a number: "))

if x==0:
  print("The given number is zero.")
elif x<=0:
  print("The given number is negative number.")
elif x>=0:
  print("The given number is Positive number.")
else:
  print("The given input is not a number.") """
  
"""   # simple calclulator:
p=int(input("enter a number: "))
r=input("enter operator: ")
q=int(input("enter a number: "))

if r=="*":
  print("Product: ", p*q)
elif r=="-":
  print("Difference: ", p-q)
elif r=="/":
  print("Quotient: ", p/q)
elif r=="+":
  print("Sum: ", p+q)
else:
  print("invalid input..") 




#grade calculation:
x=int(input("Enter your total marks: "))

if x>90:
  print("Grade A")
elif x>=80:
  print("Grade B")
elif x>=70:
  print("Grade C")
else:
  print("Grade D")
"""

""" oneline if else:
syntax: value_if_true if condition else value_if_false
"""
""" temp=20
weather="hot" if temp>=20 else "cold"
print("weather==>", weather) 

#falsy values: 0, 0.0, 0j, None, False, [], (), {}, set() i.e empty collections, range(0)
#truthy values: all values except falsy values are truthy values


#example of falsy values:
if 0:
  print("This is falsy value.")
if None:
  print("This is falsy value.")
if []:
  print("This is falsy value.")

if 42:
  print("This is truthy value.")
if "Hello":
  print("This is truthy value.")
if [1, 2, 3]:
  print("This is truthy value.")"""

#rounding off a number:
x=3.14159
print(round(x, 2)) #rounds off x to 2 decimal places

my_float= 3.14159
y=f"{my_float:.3f}" #formats my_float to 2 decimal places
print(y)


""" while False:
    condition """