  #while loops
#   while condition:
#   code to execute while condition is true

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    
#   break - exits the loop immediately
#   useful for search operations or when the condition is met
#   common in infinite loops i.e. when the number of iterations is not known beforehand


#   continue - skips the rest of the code in the loop and jumps to the next iteration
#   useful for filtering and skipping certain iterations based on a condition
#   it doesnot exit the loop as break, it just skips the current iteration and moves to the next one
for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i)


#   pass statement
#   used when a statement is required syntactically but you do not want any code to be executed  
#   no operation statement i.e. does nothing, serves as a placeholder for code that will be implemented later
#   it allows you to create empty loops, functions, or classes without causing syntax errors
#   useful during development or when creating stubs

for i in range(5):
    if i % 2 == 0:
      pass    
    print(i)

# looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}s.")

#looping over a tuple
colors = ("red", "green", "blue")
for color in colors:
    print(f"The color is {color}.")

#getting the index and value using enumerate
animals = ["cat", "dog", "rabbit"]
for index, animal in enumerate(animals):
    print(f"Index: {index}, Animal: {animal}")

#looping over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

#looping over a string  [strings are sequences of characters, so we can iterate over them character by character]
#useful for counting, validating or transforming

message = "Hello, World!"
for char in message:
    print(char)