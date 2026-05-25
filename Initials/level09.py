animation=["Ponyo","spirited away","Tomb of fireflies","Ponyo","spirited away","howling castle"]
for ani in animation:
  print(ani)

 #output: 
""" Ponyo
spirited away
Tomb of fireflies
Ponyo
spirited away
howling castle """

animation=["Ponyo","spirited away","Tomb of fireflies","Ponyo","spirited away","howling castle"]
for index, ani in enumerate(animation):
  print(f"{index}: {ani}")
""" output:
0: Ponyo
1: spirited away
2: Tomb of fireflies
3: Ponyo
4: spirited away
5: howling castle
"""

cars=["Roles Royace","Mercedies Bentz","Toyota","Farari","Porche","Toyota","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
count = cars.count("Toyota")              #given element ko count return garxa
print(count)


animation="Tomb of fireflies"
print(animation.startswith("p"))        #'.startswith' works with string only...
print(len(animation))

#practice
fruits = ["apple","banana","cherry","date"]

for fruit in fruits:
  if fruit.startswith("a"):
    print(f"\'{fruit}\' starts with \'a\'")
  elif fruit.startswith("b"):
    print(f"\'{fruit}\' starts with \'b\'")
  #else chahidaina displayed output aanusar
  print(f"\'{fruit}\' has \'{len(fruit)}\' letters.")
""" output:
  'apple' starts with 'a'
  'apple' has '5' letters.
  'banana' starts with 'b'
  'banana' has '6' letters.
  'cherry' has '6' letters.
  'date' has '4' letters."""
  

tuple1=(1,2,3)
tuple2=(4,5,6)
combined = tuple1 + tuple2
print(combined)
""" output:
(1, 2, 3, 4, 5, 6) """


#comparing forloop and list comprehension
num=[1,2,3,4,5]
cubes=[]
for x in num:
  cube=x**3
  cubes.append(cube)
print(cubes)
""" output:
[1, 8, 27, 64, 125] 
"""

num=[1,2,3,4,5]
cube=[x**3 for x in num]      #list comprehension
print(cube)

""" output:
[1, 8, 27, 64, 125] 
"""

#List comprehensions
""" purpose: to create a new list based on an existing list applying operations no the elementsto modify or filter.
    syntax: new_list = [expression for item in iterable if condition]
    pros: more concise and often faster than traditional loops
    can include conditions: filter items during creation
    
    list comprehension with conditions
    filtering:includes only items that meet a condition
    transforming conditionally: applies various operation based on conditions
    Multiple conditions: can include and or if else..
    """

even_num=[]
even=[x for x in range(0,20,2)]
print(even)
""" output:
[0, 2, 4, 6, 8, 10,"""


num=[1,2,3,4,5, 6, 7, 8, 9, 10]
list=[]
for x in num:
  if x%2==0:
    list.append(x)
print(list)
""" output:
[2, 4, 6, 8, 10]"""


#using above in list comprehension
num=[1,2,3,4,5, 6, 7, 8, 9, 10]
even=[x for x in num if x%2==0]
print(even)
""" output:
[2, 4, 6, 8, 10]"""

#celcius to fahrenheit
celcius=int(input("Enter temperature in celcius: "))

fahreinheit=(9/5)*celcius + 32
print(fahreinheit)
""" output:
Enter temperature in celcius: 100
212.0"""

#convert given list of celcius to fahrenheit using for loop and list comprehension
celcius=[11,36,47.5, 0]

for temp in celcius:
  fahreinheit=[(9/5)*temp + 32]   #[..,..,..] diye result ma item nai list dinxa..
  print(fahreinheit)
""" output:
[51.8]
[96.8]
[117.5]
[32.0]"""

celcius=[11,36,47.5, 0]
fahreinheit=[]            # list vitra rakhne vanera specify gareko

for temp in celcius:
  fahr=[(9/5)*temp + 32]
  fahreinheit.append(fahr)
print(fahreinheit)
""" output:
[[51.8], [96.8], [117.5], [32.0]]"""

#comphrension list ma gareko
celcius=[11,36,47.5, 0]
fahreinheit=[((9/5)*temp + 32) for temp in celcius]
print(fahreinheit) 
""" output:
[51.8, 96.8, 117.5, 32.0]"""


###
num=list(range(1,11))
cubes=[x**3 for x in num]
print(cubes)
""" output:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000] 
"""

num=list(range(1,11))
print(num)
for x in num:
  print(x)
""" output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""