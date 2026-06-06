import csv
import json

def read():
    with open("next_practice.txt", "r") as f:
        content=file.read()
        print(content)
        

def write(next_practice):
    with open("next_practice.txt", "w") as f:
        file.write(f"{nex_practice}\n")


def write(next_content):
    with open("next_practice.txt", "a") as f:
        file.write(next_content)

Notes=input("Keep your notes: ")
Additional=input("Additional notes: ")

write(Notes)
append(Additional)
read()

books=[]

def write_jason(element):
    with open("next_practice0.json", "w") as f:
        json.dump(element, f)


def read_jason():
    with open("next_practice0.json", "r") as f:
        data=json.load(f)
        print(data)
for i in range(5):
    book=input("enter the name of {i+1} books: ")
    books.append(book)

write_jason(books)
read_jason()

books=[
            ["name", "price", "author"],
            ["Narnia", "450", "abc"],
            ["Border", "500", "author"],
            ["Law of nature", "price", "author"],
            ["name", "price", "author"],
        ]


def write_csv(Notes):
    with open("")



