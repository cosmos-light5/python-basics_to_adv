#conditional statements (if, elif, else):

#to check of the no. is positive or negeative or zero
x=int(input("please enter a number: "))

if x==0:
  print("The given number is zero.")
elif x<=0:
  print("The given number is negative number.")
elif x>=0:
  print("The given number is Positive number.")
else:
  print("The given input is not a number.")
  
""" oneline if else:
syntax: value_if_true if condition else value_if_false
"""
""" while False:
    condition """