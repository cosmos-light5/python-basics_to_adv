#map() functions
""" -map() function takes a function and an iterable as arguments; returns a new iterable with the function applied to each element of the original iterable.
    -used to apply a specific function to each item of an iterable (like a list) and return a new iterable (like a map object) with the results.
    #syntax: map(function, iterable, ...)
            -... mean jaiit wata function lai parameter chainxa tetti wata nai iterables hunuparcha
    -often used to transform data in a list or to apply a function to each element of a list without using a for loop.
    -used with a lambda function to create a new list based on the original list.
    -used with built-in functions like str(), int(), etc. to convert data types in a list which can be useful for data processing and manipulation tasks.
    -used with user-defined functions to perform more complex transformations on the data in a list.
    """
#using regular function with map
def square(x):
    return x**2
numbers=[1,2,3,4,5]
squared_numbers=list(map(square, numbers))
print(squared_numbers)
""" Output:
[1, 4, 9, 16, 25]"""

#using lambda function with map
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x:x**2, numbers))
print(squared_numbers)
""" Output:
[1, 4, 9, 16, 25]"""

#multiple arguments/iterables with map
def add(x,y,z):          #jatti wata arguments vayo tetti wata list banaune parcha
    return x+y+z            #square garna ko lagi return x**2+y**2+z**2 garna parcha
numbers1=[1,2,3,4,5]        #-->numbers1 ko 1,2,3,4,5 lai x ma rakxa
numbers2=[1,2,3,4,5]        #-->numbers2 ko 1,2,3,4,5 lai y ma rakxa
numbers3=[1,2,3,4,5]        #-->numbers3 ko 1,2,3,4,5 lai z ma rakxa ani add function ma x+y+z garxa ani result return garxa
sum=list(map(add, numbers1, numbers2, numbers3))
print(sum)
""" Output:
[3, 6, 9, 12, 15]"""


def product(x,y,z):
    return x*y*z
numbers1=[1,2,3]
numbers2=[4,5,6]
numbers3=[7,8,9]
product_list=list(map(product, numbers1, numbers2, numbers3))
print(product_list)
""" Output:
[28, 80, 162]"""

#map with different iterables length
list1=[1,12,3,4,5,15,9,27]
list2=[10,20,30]
result=list(map(lambda x,y:x+y, list1, list2))
print(result)       #[11, 32, 33]   #map function le choto iterable ko length lai consider garxa ani tesko length samma matra map function le kaam garxa
""" Output:
[11, 32, 33] -->list2 ko 2nd index samma vayeko le operation garda mathi ko pani 2nd index samma operation gareko ho..
    """


#filter functions




numbers=[1,2,3,4,5,6,7,8,9,10]
greater_than_five=list(filter(lambda x:x>5, numbers))
print(greater_than_five)

words=['hi','hello','bye','good_bye','yes','no']
more_than_three=list(filter(lambda word:len(word)>3, words))
print(more_than_three)                  #['hello', 'good_bye']

word_with_h=list(filter(lambda word:"h" in word, words))
print(word_with_h)                      #['hi', 'hello']