with open("file.txt", "r") as f:
    content = f.read()
    print(content)


#in terms of def_function
def read_file():
    with open("file.txt", "r") as f:
        content = f.read()
        print(content)

read_file()


""" 
#to return the content from the function instead of printing it:
def read_file():
    with open("file.txt", "r") as f:
        return f.read()

content = read_file()
print(content) 

"""
