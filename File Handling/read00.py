""" 
# Basic open/close pattern

fiel=open('example.txt','r') as file:
content=file.read()
file.close()
    

# Better approach with 'with' statement
with open('practice_file.txt', 'r') as file:            #'r'--> read mode vaneko ho
    content=file.read()
    print(content)
# file automatically closes when the block ends
"""

# Reading line by line
with open("practice_file.txt", "r") as f:
    line = f.readline()                                             #readline() le one line at a time read garxa
    print(line)