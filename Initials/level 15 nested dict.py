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

#new nested book add gareko
books["The Ulchemist"]={"ISBN": 56,                     
                    "author": "Paollo Kohello",
                    "publish_date": 1994}
print(books)


#modifying nested values
books["The Ulchemist"]["publish_date"]=1995             #small changes inside the ulchemist dict...
print(books["The Ulchemist"])



#update() method modifies a dictionary in-place by adding new key-value pairs or overwriting the values of existing keys.
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

new_books = {"The art of war":{"ISBN": 45,
                    "author": "sun Zhu",
                    "publish_date": 1845},
             "Summer love":{"ISBN": 45,
                    "author": "Subin Bhattarai",
                    "publish_date": 2020}}

books.update(new_books)         #When you pass another dictionary, existing keys get overwritten, and new keys are appended
print(books)
#Or  for quick, pass direct key-value assignments inside the function
books.update({"The Ulchemist":{"ISBN": 56,                  
                    "author": "Paollo Kohelo",
                    "publish_date": 1997}})
print(books) 


#jaha key vetidaina tya ha error nadiyi comment print garna .get() ko use gare ko..
print(books.get("Serve-well", "doesnot exists").get("price", "Invalid input.."))
print(books.get("Serve-well", {}).get("price", "Invalid input.."))              #{} --> vaneko None vaneko ho

# Adding a key to a nested dictionary
books["Summer love"]["price"] = 550         #yaha summer love vitra euta "price" key add garera tesko value diyeko ho...
print(books)

#major keys dinxa .title() le
for book_name, details in books.items():
    print(f"{book_name.title()}")
""" Output: Harry Potter
            Romeo-Juliet    
            Serve-Well
            The Art Of War
            The Law Of Human Nature
            Summer Love
            The Ulchemist """


#books vitra ko book details matra dinako lagi..
book_details=list(books.values())           #yaha values nested vayeko le nested values nai print hunxa..
print(book_details)



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
    
""" Output:
            Ram - Math: 85, Science: 90, English: 78, 
            Sita - Math: 92, Science: 88, English: 81, 
    """

a=[85,90,78,32]
highest=0

a.sort()              #increasing order ma sort garxa
#print(a.sort())      #yo gare none aauxa
print(a[-1])          #Output: 90
