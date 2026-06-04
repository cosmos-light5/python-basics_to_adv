""" 
# Basic open/close pattern

fiel=open('example.txt','r') as file:
content=file.read()
file.close()
    

# Better approach with 'with' statement
with open('practice_file.txt', 'r') as file:            #'r'--> read mode vaneko ho
    content=file.read()                                 #file ma vayeko lines sabai read garxa
    print(content)
# file automatically closes when the block ends



with open("practice_file.txt", "r") as f:
    print(f)                #f pointer ko details info dinxa
--><_io.TextIOWrapper name='practice_file.txt' mode='r' encoding='cp1252'>

# Reading line by line
with open("practice_file.txt", "r") as f:
    line = f.readline()                                  #readline() le one line at a time read garxa
    print(line)


# reading two lines
with open("practice_file.txt", "r") as f:
    line1 = f.readline()                                 #line1 le one line read garxa 
    line2 = f.readline()                                 #ani lagatai fere line2 ko palo aauda 1st line execute vayeko le 2nd line bata read garxa..
    print(line1)
    print(line2)


# reading all lines into a list
with open("practice_file.txt", "r") as f:
    lines = f.readlines()                                #.readlines() le one list ma convert garxa with \n before every new elements
    print(lines)
    for line in lines:                                   # for loop le every sentence lai individually execute garxa
        print(line.strip())                             #lines.strip() le white spaces remove garxa

        
# Most efficient way to read line by line
with open("practice_file.txt", "r") as f:
    for line in f:
        print(line.strip())  

"""




