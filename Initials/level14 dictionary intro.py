#Dictionaries
""" -An unorderes, mutable collection of key-value pairs 
Key characteristics:
    -keys must be unique and immutable (string, number, tuples). values can be of any data-type and can be duplicated
    -unordered in python<3.7(ordered by insertion since 3.7+)
    -Mutable (can be changed after creation)
    -Fast lookups by key (O(1)) average case
    -syntax:
            created using {} with key-value pairs
"""
empty_dict={}
print(empty_dict)

#keys cannot be list or set but values can
mixed_dict={"str_key":"value", "int_key":55, "list_key":[1,7,0]}
print(mixed_dict)
""" Output: {'str_key': 'value', 'int_key': 55, 'list_key': [1, 7, 0]} """


#dict() implementation
using_dict_function=dict(name="Yak-dai", age=25, city="Shangri-la")
print(using_dict_function)
""" Output:{'name': 'Yak-dai', 'age': 25, 'city': 'Shangri-la'} """


from_tuples=dict([("name","Yak-dai"), ("age",25), ("city","Shangri-la")])
print(from_tuples)
""" Output: {'name': 'Yak-dai', 'age': 25, 'city': 'Shangri-la'} """


books={"Title":"Radha",
       "Auther":"Krishna Dharabasi",
       "Price":450}
print(books)

#accessing dictonary elements
""" -using keys: direct access with square bracket
    -get() method: safe access with default values
    -Keys, values and items: accessing all elements
 """

dict_function=dict(Title="Radha",
       Auther="Krishna Dharabasi",
       Price=450)
print(dict_function)
print(dict_function["Title"])
#print(dict_function["pages"])       #key_error dinxa, dictionary ma navayeko element access garna khoje ma


dict_function=dict(Title="Radha",
       Auther="Krishna Dharabasi",
       Price=450)
print(dict_function)
print(dict_function["Title"])                   
#print(dict_function["pages"])                             #unsafe way
print(dict_function.get("pages", "Not available"))         #safe way; element navaye ma None ki rakhoyeko default message output ma dinxa



#Modifying dictionary
""" -Adding or updating: using assignment with keys
    -Updating multiple key-value: using updat() method
    -Removing item: using pop(), popitem(), del, clear() 
"""

dict_function=dict(Title="Radha",
       Auther="Krishna Dharabasi",
       Price=450)
print(dict_function)
print(dict_function["Title"])
print(dict_function.get("pages", "Not available"))
""" Output:
{'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450}
Radha
Not available """

#adding key-value in dictionary
dict_function["Editon"]="Third"         #yesari nai values update garna milxa 
#dict_function["Editon"]="3rd"  --> lekhda pani error aaudaina
print(dict_function)
""" Output: {'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450, 'Editon': 'Third'} """

dict_function.update(email="hello@friend.com", Price=550)
print(dict_function)
""" Output: 
{'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 550, 'Editon': 'Third', 'email': 'hello@friend.com'} """


#removing items
books={'Title': 'Radha',
       'Auther': 'Krishna Dharabasi', 
       'Price': 550, 
       'Editon': 'Third', 
       'email': 'hello@friend.com'}

email=books.pop("email")
print(email)
print(books)
""" Output: hello@friend.com
{'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 550, 'Editon': 'Third'} """

#pop with default values if key doesnot exists
Phone_no=books.pop("contacts", "No contacts available..")
print(Phone_no)


last_item=books.popitem()                 #last time insert gare ko item remove garxa .popitem() le
print(last_item)
print(books)

#Deleting specific KeyboardInterrupt
books["temp"]="delete me"
print(books)
del books["temp"]
print(books)

#clearing all items
books.clear()
print(books)        #output: {}



#Dictionary method for merging and updating
""" -update(): updates dictionary with key-values with from another
    -| operator  (Python 3.9+): 
    -|- operator : 
 """

#update() method
books={'Title': 'Radha', 'Auther': 'Krishna Dharabasi', 'Price': 450}
details={"edition":"3rd", "Publication":"Sarada Publication"}

books.update(details)
print(books)


#Overwriting existing key
books.update({"edition": "4th", "pages": 550})                 #edition ko value overwrite gareko
print(books)


#dictionary merge operator | (Python 3.9+)
dict1={"a": 1, "b":2}
dict2={"b": 3, "c":4}

dict1.update(dict2)
print(dict1)                
""" Output:{'a': 1, 'b': 3, 'c': 4}  #merge garda dict2 ko b ko values linxa because b ko value overwrite garera update gareko hunxa"""        

#eqv method
merged= dict1 | dict2                    
print(merged)


#dictionary update operator |= (Python 3.9+)
dict1 |= dict2              #updates dict1 in-place                    
print(dict1)                #Output:{'a': 1, 'b': 3, 'c': 4}



#for python <3.9, use {**dict1, **dict2} to merge
dict1={"a": 1, "b":2}
dict2={"b": 3, "c":4}

early_merge={**dict1, **dict2}
print(early_merge)  