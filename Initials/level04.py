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

    
for i in range(3,31,3): #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end="a ")


for i in range(3,31,3): #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end="a ")
    print()
    print()
    print(i,end =" ")

#long logical conditions
for i in range(3,31,3):
  if i!=12 and i%5 != 0:
    print(i)


#to find vowel and consonents (conventional way)
msg= input("give characters to check: ")
print()
count=1
for char in msg:  
  if char >= "A"and char<="Z" or char>="a" and char<="z":
    if char=='A'or char=='a' or char=='E'or char=='e' or char=='I'or char=='i' or char=='O'or char=='o' or char=='U'or char=='u':
      print(count, end=" ")
      print(char, ":", end="")
      print(" Vowels")
    else:
      print(count, end=" ")
      print(char, ":", end="")
      print(" Consonants")
  else:
    print("NOT a character..")
  count+=1
print("total characters: ", count-1)
"""

#upper and lower case conversion
char="X-Man and GODzilla"
print(char.lower())
print(char.upper())

#shorter way to find vowel and consonents


  #while loops
#   while condition:
#   code to execute while condition is true

  