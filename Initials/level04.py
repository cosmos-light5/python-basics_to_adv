#intro to loops
#for loops
#for variable in sequence:
#  code to execute
""" for number in [1,2,3,4,5]:
  print(number)
print("\n")
for i in range(5):
  print(i) 

#to print numbers from 2 to 20
for i in range(2,21):
  print(i)

#multiples of 3 from 1 to 30
for i in range(1,11):
  i*=3
  print(i)

#OR
for i in range(3,31,3):
    print(i)


for i in range(1,31,3):
    print(i)
"""
#remove no. 12
for i in range(1,11):
  i*=3
  if i==12:
    print()
  else:
    print(i)
 
 #OR
for i in range(3,31,3):   #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end ="")


#   while condition:
#   code to execute while condition is true

  