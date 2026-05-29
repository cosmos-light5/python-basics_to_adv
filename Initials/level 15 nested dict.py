books={"Harry Potter":{"ISBN": 12,
                    "author": "J. K. Rollins",
                    "publish_date": 1990}, 

        "Romeo-Juliet":{"ISBN": 23,
                    "author": "william shakespears",
                    "publish_date": 1890}, 

        "Serve-well":{"ISBN": 34,
                    "author": "Thomas Dritz",
                    "publish_date": 1987},

        "The art of war":{"ISBN": 45,
                    "author": "sun Zhu",
                    "publish_date": 1840},

        "The law of Human Nature":{"ISBN": 56,
                    "author": "Robert Greene",
                    "publish_date": 1976}}

print(books["Harry Potter"]["author"])          #key ko through access


books["The Ulchemist"]={"ISBN": 56,
                    "author": "Paollo Kohello",
                    "publish_date": 1994}
print(books)

print("before update: ", books)
books.update({"ISBN": 56,
                    "author": "Paollo Kohello",
                    "publish_date": 1997})
print("after update: ", books) 

#use '.capitalize() to make the subjct name first letter capital'
students={
    "Ram":{
        "math":85,
        "science":90,
        "english":78
    },
    "Sita":{
        "math":92,
        "science":88,
        "english":81
    }
}

for i,j in students.items():
    print(i, end=" - ")
    for sub, marks in j.items():                #i key ko algi  ani j vitra ko sub key ko lagi
        print(f"{sub.capitalize()}: {marks}", end=", ")
    print()    
    