#list
""" -[]
    -mutable(can be updated: added or removed or modified)
    -ordered i.e. indexed mutable items
    -collection of items may contain lists inside a list
    -may be an empty list 
    -may contain repeated elements
    -list items may be of different data types"""
#creating a list
""" empty_list = []
print(empty_list)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)

mixed_data_types = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}, [1, 2, 3]]
print(mixed_data_types)

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print(len(cars[3]))     #given index ko element ko length dinxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print(cars[3])            #index ko element dinxa
 

#negative indexing
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print((cars[-1]))             #last element bata -1,-2,-3 count hudai first tira ko position ma aauxa

#add garxa tara nested list banaudaina!!..
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
more_cars= cars + ["Nissan","Toyota"]
print(more_cars)

#To repeat or copy same list multiple times and give a new list without nesting
cars=["Mercedies Bentz"]
print(cars*3)

#in operator
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print("Mitsubisi" in cars)          #list ma xa ki xaina bhanera check garxa and return ma true or false lina

"""

#unavailable index ko notify garna ko lagi
index=-1
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
if 0 <= index or index < len(cars):
  print(cars[index])
else:
  print("Index out of range")

#Basic slicing
''' syntax:
        list[start:stop: step] '''
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[2:4])            #0index bata 2nd index ko bata start till stop-1 samma..

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[:])        #shallow copy garxa