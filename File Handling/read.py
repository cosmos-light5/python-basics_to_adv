""" with open("file.txt", "r") as f:
    content = f.read()
    print(content)
 """
"""
#in terms of def_function
def read_file():
    with open("file.txt", "r") as f:
        content = f.read()
        print(content)

read_file()


 
#to return the content from the function instead of printing it:
def read_file():
    with open("file.txt", "r") as f:
        return f.read()

content = read_file()
print(content) 

"""

""" with open("file.txt", "r") as f:
    line = f.readline()                                             #readline() le one line at a time read garxa
    print(line)
      """


with open("file.txt", "r") as f:
    line = f.readlines()                                             #readline() le lines lai list ma read garxa
    print(line)                                         #['New content appears here..\n', "Hello, I'm mr. happy.\n"]



with open("file.txt", "r") as f:
    line = f.readline()
    print(line)                         #alternatively 
    for line in f:
        print(line)



