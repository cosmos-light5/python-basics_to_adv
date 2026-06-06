import csv

#writing a csv file
data=[
    ["Name", "age", "City"],                #name, age, city--> header ho vane aaru data
    ["Alice", 25, "New York"],
    ["Bob", 30, "Chicago"],
    ["Charlie", 35, "Los Angles"]
]

with open("people.csv", "w", newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)                      #individual row print garxa


with open("people.csv", "r", newline="") as file:
    csv_reader=csv.reader(file)                     #csv.reader() reads the file line by line; splits each row into a list using commas as separators.
    header=next(csv_reader)                         #next() retrieves the next item from an iterator; Since the iterator is currently at the first row, it returns the header row.
    print(f"Header: {header}")

    for row in csv_reader:                          #for loop starts from the first_data_row because next(csv_reader) has already consumed the header row.
        print(row)



with open("people.csv", "r", newline="") as file:
    csv_reader=csv.DictReader(file)
  
    for row in csv_reader:
        print(row)                          #each row is a dictionary



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
    fieldnames=["Name","age","City"]                            #yaha variable fieldnames le dictionary ma headers dine kam garxa
    writer=csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)