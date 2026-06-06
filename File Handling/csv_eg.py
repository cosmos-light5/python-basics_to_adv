import csv

#writing a csv file
data=[
    ["Name", "age", "City"],                #name, age, city--> header ho vane aaru values
    ["Alice", 25, "New York"],
    ["Bob", 30, "Chicago"],
    ["Charlie", 35, "Los Angles"]
]

with open("people.csv", "w", newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)                      #individual row print garxa


with open("people.csv", "r", newline="") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)                         #Reads the header row; next le one line print garxa
    print(f"Header: {header}")

    for row in csv_reader:
        print(row)



with open("people.csv", "r", newline="") as file:
    csv_reader=csv.DictReader(file)
  
    for row in csv_reader:
        print(row)



students=[]

with open("people.csv", "r", newline="") as file:
    csv_writer=csv.DictReader(file)
  
    for row in csv_writer:
        print(row)
        students.append(row)

print(students) 
students.append({"Name": "Prakash", "age": 25, "City":"kathmandu"})

print(students)


with open("people-output.csv", mode="w", newline="") as file:
    fieldnames=["Name","age","City"]
    writer=csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)