""" with open("file.txt", "w") as f:                #f-->pointer ho that points file.txt
    f.write("New content")
     """
""" 
#write garda existing file ma code xa vane sabai truncate(clear) garera matra write garxa i.e. overwrite so append use garne.. 

#in terms of def_function
def write_file():
    with open("file.txt", "w") as f:
        f.write("New content")

write_file()

  """


sentences=["I have a car.","He owns a manison.", "Bradly is a blues lyricist.", "Taro is a turtle specialiest.", "kelensky is a mad scientist.","New content appears here..","Hello, I'm mr. happy."]

with open("file.txt", "w") as f:  
    for i in sentences:
        f.write(f"{i}\n")
#    print()



""" sentences=["I have a car.\n","He owns a manison.\n", "Bradly is a blues lyricist.\n", "Taro is a turtle specialiest.\n", "kelensky is a mad scientist.\n","New content appears here..\n","Hello, I'm mr. happy.\n"]

with open("file.txt", "w") as f:  
    for i in sentences:
        f.writelines(f"\n{i}") """
