"""animation=["Ponyo","spirited away","Tomb of fireflies","Ponyo","spirited away","howling castle"]
for ani in animation:
  print(ani)

 #output: 
Ponyo
spirited away
Tomb of fireflies
Ponyo
spirited away
howling castle

animation=["Ponyo","spirited away","Tomb of fireflies","Ponyo","spirited away","howling castle"]
for index, ani in enumerate(animation):
  print(f"{index}: {ani}")


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

  

tuple1=(1,2,3)
tuple2=(4,5,6)
combined = tuple1 + tuple2
print(combined)



#comparing forloop and list comprehension
num=[1,2,3,4,5]
cubes=[]
for x in num:
  cube=x**3
  cubes.append(cube)
print(cubes)


num=[1,2,3,4,5]
cube=[x**3 for x in num]      #list comprehension
print(cube)

"""

#List comprehensions
""" purpose: to create a new list based on an existing list applying operations no the elementsto modify or filter.
    syntax: new_list = [expression for item in iterable if condition]
    pros: more concise and often faster than traditional loops
    can include conditions: filter items during creation"""

even_num=[]
even=[x for x in range(0,20,2)]
print(even)


num=[1,2,3,4,5, 6, 7, 8, 9, 10]
list=[]

for x in num:
  if x%2==0:
    list.append(x)
print(list)

#using above in list comprehension
num=[1,2,3,4,5, 6, 7, 8, 9, 10]
even=[x for x in num if x%2==0]
print(even)


#celcius to fahrenheit
celcius=int(input("Enter temperature in celcius: "))

fahreinheit=(9/5)*celcius + 32
print(fahreinheit)


#convert given list of celcius to fahrenheit using for loop and list comprehension
celcius=[11,36,47.5, 0]
count=0
for temp in celcius:
  count+=1
  fahreinheit=[(9/5)*temp + 32]   #[..,..,..] diye result ma item nai list dinxa..
  print(fahreinheit)


celcius=[11,36,47.5, 0]
fahreinheit=[]            # list vitra rakhne vanera specify gareko

for temp in celcius:
  fahr=[(9/5)*temp + 32]
  fahreinheit.append(fahr)
print(fahreinheit)

#comphrension list ma gareko
celcius=[11,36,47.5, 0]
fahreinheit=[((9/5)*temp + 32) for temp in celcius]
print(fahreinheit)