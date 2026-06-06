""" def write00_file():
    with open("practice_file.txt", "w") as f:           #practice_file.txt file banaeyra tes ma write grne ani testing New content vaneko
        f.write("testing New content")

write00_file()


cent=["Iro is the general commander.", "Chopper is playful GOAT.", "Potato is the steam part of the potato plant.", "Ice fishing is the better way to obtain food in antartic nations."]   #yaha list element ko sentences ko end ma \n feed garda pani hunxa 
with open("practice_file0.txt", "w") as f:          #mathi written vayeko clear garera yo list lai every line lai new line feed garxa
    for i in cent:
        f.write(f"{i}\n")                           #changes pracrice_fiel.txt ma check garne

 """



cent=["Iro is the general commander.", "Chopper is playful GOAT.", "Potato is the steam part of the potato plant.", "Ice fishing is the better way to obtain food in antartic nations."]

with open("practice_file0.txt", "a") as f:         
    f.writelines(cent)                  #append gareko


