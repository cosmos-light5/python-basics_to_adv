#list
""" -[]
    -mutable(can be updated: added or removed or modified)
    -ordered i.e. indexed mutable items
    -collection of items may contain lists inside a list
    -may be an empty list 
    -may contain repeated elements
    -list items may be of different data types"""
#creating a list
empty_list = []
print(empty_list)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)

mixed_data_types = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}, [1, 2, 3]]
print(mixed_data_types)

cars=["Roles Royace","Mercedies Bentz","Farari","Porche","Volkeswagen"]
print(len(cars[3]))