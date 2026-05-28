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
    print(i)                    # i ko value print huda, keys matra print garxa but not in manner of list

#looping through values
for j in books.values():
    print(j)

#looping through key-value pairs
for key, value in books.items():
    print(f"{key}: {value}")

