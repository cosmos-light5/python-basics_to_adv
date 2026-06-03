#append le file exist na vaye new file pani banauxa
with open("file.txt", "a") as f:
    f.write("Additional content")


""" 
#in terms of def_function
def append_file():
    with open("file.txt", "a") as f:
        f.write("Additional content")

append_file()
     """