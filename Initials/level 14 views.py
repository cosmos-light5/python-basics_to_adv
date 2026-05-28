#Dictionary views
""" -dict.keys(): returns a view of all keys
    -dict.values(): returns a view of all values
    -dict.items(): returns a view of all key-value pairs
    -views are dynamic: reflect changes to the dictionaries i.e dictionary herda list jaso hunxa tara hami le keys add garda tesko values pani auto add garna ko lagi views use garxaun..
"""


books={'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450, "edition":"3rd", "Publication":"Sarada Publication"}
key_view=books.keys()
value_view=books.values()
item_view=books.items()

print(key_view)
print(value_view)
print(item_view)



books={'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450, "edition":"3rd", "Publication":"Sarada Publication"}
books["published year"]=2020        #Dynamic nature i.e. key ra value add garko

print(key_view)
print(books)

#conversion dict to list
books={'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450, "edition":"3rd", "Publication":"Sarada Publication"}
book_details=list(books.keys())
print(book_details)

#views support iteration, membership testing and length
for key in key_view:
    print(key)

print("price" in key_view)
print(len(item_view))

#Looping through dictionaries
""" -looping through keys: Default behaviour
    -looping through values: using values() method
    -looping through key-value pairs: using items() method
    -Conditional looping: Filtering during iteration 
"""


#looping through keys
books={'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450, "edition":"3rd", "Publication":"Sarada Publication","published year":2020}
for i in books:
    print(i)                    # i ko value print huda, keys matra print garxa as default but not in manner of list
#or equ 
for i in books:
    print(f"{i}: {books[i]})             # i default keys hunxa  

#looping through values
for j in books.values():
    print(j)

#looping through key-value pairs
for key, value in books.items():
    print(f"{key}: {value}")

#sample
capital_cities={
    "Nepal": "Kathmandu",
    "India":"New Delhi",
    "USA":"Washington, D.C.",
    "Japan":"Tokyo"
}

for i in capital_cities:
  print(f"The capital city of {i} is {capital_cities[i]}.")


capital_cities={
    "Nepal": "Kathmandu",
    "India":"New Delhi",
    "USA":"Washington, D.C.",
    "Japan":"Tokyo"
}

for key, values in capital_cities.items():
  if key=="Nepal":
    print(f"The capital city of {key} is {values}.")


#practice
products={
    "laptop":70000,
    "mouse":500,
    "keyboard":1200,
    "monitor":1500,
}
count=0
for key, value in products.items():
    if value>1000:
        count+=1
print(f"{count} products cost more than 1000.")


#basic dictionary comprehension
cube = {x: x**3 for x in range(1,20)}       multiple of3
print(cube)


cube = {x: x**3 for x in range(10) if 6 != x}
print(cube)

#swappping keys and values positions
# Original dictionary
old_dict = {'a': 1, 'b': 2, 'c': 3}

# Swap keys and values
new_dict = {value: key for key, value in old_dict.items()}

# Display the output
print(new_dict)
