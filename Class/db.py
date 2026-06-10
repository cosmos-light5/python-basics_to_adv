import sqlite3

connection =sqlite3.connect("student.db")
cursor=connection.cursor()

def create_table():
    print("You are inside create_table.")
    create_table_query="""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT UNIQUE
                )
"""
    try:
        cursor.execute(create_table_query)
        print("Table created successfully.")
    except Exception as e:
        print("error creating Table: ")
        print(e)

def alter_table():
    print("You are inside alter_table")
    alter_table_query="""
        ALTER TABLE users ADD COLUMN phone TEXT;
"""
    try:
        cursor.execute(alter_table_query)
        print("Table created successfully-Added phone_number column.")
    except Exception as e:
        print("error altering Table: ")
        print(e)

def rename_table():
    print("You are inside rename_table")
    rename_table_query="""
            ALTER TABLE users RENAME TO students;
"""
    try:
        cursor.execute(rename_table_query)
        print("Table renamed successfully from users to students.")
    except Exception as e:
        print("error renaming Table: ")
        print(e)


def add_data():
    print("You are inside add_data.")

def read_data():
    print("You are inside read_data.")

def update_data():
    print("You are inside update_data.")

def delete_data():
    print("You are inside delete_data.")



create_table()
add_data()
read_data()
update_data()
delete_data()
alter_table()
rename_table()