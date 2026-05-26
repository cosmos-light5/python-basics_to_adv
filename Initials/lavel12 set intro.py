#set intro
""" -an unordered collection of unique elements 
    -unordered (items have no defined order, you cannot access items by index)
    -no redundant items (each item is unique, duplicates are removed automatically)
    -elements must be immutable (cannot be changed after creation, e.g. numbers, strings, tuples but not lists or dictionaries)
    -sets are mutable (you can add or remove items from a set after it is created)
    -fast membership testing [o(1) average time complexity for checking if an item is in a set]
    -created using curly braces {} or the set() constructor i.e.
                syntax:set_name = {item1, item2, item3} or set_name = set([item1, item2, item3])
    -common operations: union, intersection, difference, symmetric difference"""

empty=set()       #set{} --> creates dictionary so use ()
print(empty)


str=("hello, welcome to nepal..")
str_set=set("hello, welcome to nepal..")
print(str)
print(str_set)                  #the set will contain unique characters from the string as string is iterable, and the order of characters in the set may not be the same as in the original string due to the unordered nature of sets.
""" Output:set()
hello, welcome to nepal..
{'p', 't', 'm', ' ', '.', ',', 'o', 'c', 'n', 'h', 'e', 'l', 'w', 'a'} """


#to eliminate repetition from list
num=[1,2,2,2,33,44,44,5,5,6,7,77,77,77,898,0]
unique=list(set(num))         #list lai set ma convert gareko unique element gain garna
print(unique)
""" Output:
[0, 1, 2, 33, 898, 5, 6, 7, 44, 77] """


#Membership testing vaneko use of in operator ho..

#subset and superset
citrus={"lemon","orange"}
fruits={"apple","banana","mango","cherry","date"}

print(citrus.issubset(fruits))              #Output:False
print(fruits.issubset(citrus))              #Output:False

books={"Pearl harbour","palpasa cafe","uttam gyan"}
books.add("you can win")               #.add le matra eut element add garxa
print(books)

books={"Pearl harbour","palpasa cafe","uttam gyan","you can win"}
books.update("Into the wind","you can win")            #.update le 2 or more elements add garxa raindividual characters xarera display garxa ani 'iterable's matra rakhne eg. string
print(books)                                           #unique elements rakhne vayeko le you can win dekhaudaina


#removing elements from set
""" -remove():removes an element, rises key error if not found 
    -discard():removes an element if present, no error if not found
    -pop():removes and returns an arbitary element
    -clear():removes all elements"""

books={"Pearl harbour","palpasa cafe","uttam gyan","you can win","Into the wind"}
books.remove("Into the wind")

books.remove("Art of bravery")              #navako element remove garda throws as key error ........
books.discard("Art of bravery")             #no error when element does not exist


removed=books.pop()
print('removed:', removed)                  #randomly pop garxa any element
print(books)                                #gives the remaining elements

books.clear()                               #removes all elements
print(books)