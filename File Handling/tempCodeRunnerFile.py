sentences=["I have a car.","He owns a manison.", "Bradly is a blues lyricist.", "Taro is a turtle specialiest.", "kelensky is a mad scientist.","New content appears here..","Hello, I'm mr. happy."]

with open("file.txt", "w") as f:  
    for i in sentences:
        f.write(f"{i}\n")
#    print()