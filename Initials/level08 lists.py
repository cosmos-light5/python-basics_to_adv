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
print(mixed_data_types)             #nested list print garxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print(len(cars[3]))     #given index ma vayeko element ko length dinxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print(cars[3])            #given index ko element dinxa, if list ma vayeko index vanda badhi index diyema error dinxa
print(len(cars))             #list ma vayeko total items ko length dinxa

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
"""

#in operator
""" -used to check if an item exists in a list or not
    -can be used in conditional statements or for the boolean value of on return
    -returns true if the item exists in the list 
        and false if it does not exist in the list
    -syntax: item in list  """
"""cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print("Mitsubisi" in cars)         



#unavailable index ko notify garna ko lagi
index=-1
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
if 0 <= index or index < len(cars):
  print(cars[index])
else:
  print("Index out of range")

#List slicing
''' -syntax: list[start:stop: step
    -Default values: start=0, stop=len(list), step=1
    -Negative indexing: works with slicing too
    -Creating copies:   [:]=creates a shallow copy ] '''

#ommitting start and stop index
municipality=["Kathmandu","Lalitpur","Bhaktapur","Kavre","Dhading"]
print(municipality[2:])           #2st index bata last samma print garxa
print(municipality[:3])           #0 index bata 3rd index i.e 2nd element samma print garxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[2:4])            #0 index bata 2nd index ko bata start till stop-1 samma..

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[:])        #shallow copy garxa



cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[::-1])           #reverse garxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[3:])           #3rd index bata last samma print garxa

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[:4])           #0 index bata 4th index ko bata start till stop-1 samma print garxa



cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[:-2])              #last ko two elements hatayera output dinxa..
print(cars[-3:])        #last 3 element print garxa but not in reverse order

#using step in slicing
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
print(cars[1:7:2])           #1st index bata 7th index samma 2 step ma print garxa
print(cars[::3])             #0 index bata last index samma 3 step ma print garxa

#modifying list items
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
cars[0] = "Hundai"        #index wise replace gareko
print(cars)

#multiple elements replacing
cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
new_cars = cars[2:4] = ["Lamborghini","Bugatti"]     #index wise replace gareko
print(new_cars)   

"""

#listing methods
""" -append(): adds an item to the end of the list
    -insert(): adds an item at the specified position
    -extend(): adds all items of an iterable to the end of the list


    
    -index(): returns the index of the first item with the specified value
    -count(): returns the number of items with the specified value
    -sort(): sorts the items of the list in place
    -reverse(): reverses the elements of the list in place
    -copy(): returns a shallow copy of the list  """


""" cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
cars.append("koneigeggs")          #list ko last ma element add garxa
print(cars)

cars.insert(2,"Lamborghini")          #index wise element add garxa
print(cars)

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
more_cars=["wrangler_Jeep","Bugatti"]
cars.extend(more_cars)           #list ko last ma elements add garxa
print(cars)
 """
#removing items from list
""" -remove(): removes the first item with the specified value
    -pop(): removes and returns an item at the given index (default is the last item)
    -del(): removes an item at the specified index or deletes the entire list
    -clear(): removes all items from the list  """


cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
removed_cars = cars.pop()             #last element remove garxa
print(removed_cars)                    #output: Toyota
print(cars)                             #output: ['Roles Royace', 'Mercedies Bentz', 'Farari', 'Porche', 'Volkeswagen', 'Mitsubisi', 'Nissan']

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
removed_cars = cars.pop(2)           #given index ko element remove garxa
print(removed_cars)                    #output: Farari
print(cars)     


cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
cars.remove("Porche")         #given element remove garxa
print(cars)

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
cars.remove("Porche")         #given element remove garxa
print(cars[3])
print(cars)


cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
del cars[0]            #given index ko element remove garxa
print(cars)

del cars[3:5]           #given index ko range ma elements remove garxa ie. 3rd and 4th index ko elements remove garxa
print(cars)  


cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen","Mitsubisi", "Nissan","Toyota"]
cars.clear()           #list ko sabai elements remove garxa
print(cars)             #output: []