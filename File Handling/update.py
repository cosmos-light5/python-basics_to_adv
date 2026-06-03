#update mode (read-write)--> '+'

with open("file.txt","r+") as f:
    content=f.read
    f.write("More Content")

""" 
#interms of def_function:
def update_file():
with open("file.txt","r+") as f:
    content=f.read
    f.write("More Content") 
    
update_file()  
    """