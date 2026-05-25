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


even_num=[]
even=[x for x in range(0,20,2)]
print(even)


tuple1=(1,2,3)
tuple2=(4,5,6)
combined = tuple1 + tuple2
print(combined)