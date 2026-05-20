#intro to for loops
#-indentation is important in python(for forloops)
""" for variable in sequence:
   code to execute """
for number in [1,2,3,4,5]:
  print(number)
#OR
for i in range(5):
  print(i) 
""" output:
        1
        2
        3
        4
        5 """

#to print numbers from 2 to 20
for i in range(2,21):
  print(i)

""" output:
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20 """


#multiples of 3 from 1 to 30
for i in range(1,11):
  i*=3
  print(i)
""" output:
    3
    6
    9
    12
    15
    18
    21
    24
    27
    30 """


#OR
for i in range(3,31,3):
    print(i)
""" output:
    3
    6
    9
    12
    15
    18
    21
    24
    27
    30 """


for i in range(1,31,3):
    print(i)
""" output:
    1
    4
    7
    10
    13
    16
    19
    22
    25
    28 """
#remove no. 12
for i in range(1,11):
  i*=3
  if i==12:
    print()
  else:
    print(i)
""" output:
    3
    6
    9

    15
    18
    21
    24
    27
    30 """

 #OR
for i in range(3,31,3):   #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end ="")
""" output:
  369151821242730 -->no gap because of end="" """
    
for i in range(3,31,3): #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end="a ")
""" output:
  3a 6a 9a 15a 18a 21a"""

for i in range(3,31,3): #3-3 increment gareko xa i.e. multiple of 3
  if i!=12:
    print(i,end="a ")
    print()
    print()
    print(i,end =" ")
""" output:
      3a 
      3
      6a 
      6
      9a 
      9
      15a 
      15
      18a 
      18
      21a 
      21
      24a 
      24
      27a 
      27
      30a 
      30 """


#long logical conditions
for i in range(3,31,3):
  if i!=12 and i%5 != 0:
    print(i)

""" output:
    3
    6
    9
    18
    21
    24
    27 """

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
print("total characters: ", count-1) #count lai 1 bata initialize gareko le last ma count-1 gareko kina bhane loop ko last ma count 1 increment hunxa, so total characters print garna count-1 gareko.


#upper and lower case conversion
char="X-Man and GODzilla"
print(char.lower())
print(char.upper())
""" output:
x-man and godzilla
X-MAN AND GODZILLA """

#shorter way to find vowel and consonents
count=0
x=input("enter any word: ")
for char in x:
  if char.lower() in "aeiou":
    count+=1
    print(" vowel")
  else:
    print(" consonant")
print("total no. of vowels: ", count)

""" output:
enter any word: Jane
 consonant
 vowel
 consonant
 vowel
total no. of vowels:  2 """


#properly done
count=0
ccount=0
vcount=0
x=input("enter any word: ")
for char in x:
  if char.lower() in "aeiou":
    vcount+=1
    print(vcount, end=" ")
    print(char, ":", end="")        
    print(" vowel")
  else:
    ccount+=1
    print(count, end=" ")
    print(char, ":", end="")      
    print(" consonant")
  count+=1
print("total no. of vowels: ", vcount)
print("total no. of consonants: ", ccount)
print(f"total no. of characters: {count}")

""" output:
enter any word: JacKey
0 J : consonant
1 a : vowel
2 c : consonant
3 K : consonant
2 e : vowel
5 y : consonant
total no. of vowels:  2
total no. of consonants:  4
total no. of characters: 6 """
  