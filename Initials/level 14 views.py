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


books["published year"]=2020

print(key_view)
print(books)