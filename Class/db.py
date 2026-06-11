import sqlite3

connection =sqlite3.connect("student.db")
cursor=connection.cursor()

# def create_table():
#     print("You are inside create_table.")
#     create_table_query="""
#             CREATE TABLE IF NOT EXISTS users(
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 age INTEGER,
#                 email TEXT UNIQUE
#                 )
# """
#     try:
#         cursor.execute(create_table_query)
#         print("Table created successfully.")
#     except Exception as e:
#         print("error creating Table: ")
#         print(e)

# def alter_table():
#     print("You are inside alter_table")
#     alter_table_query="""
#         ALTER TABLE users ADD COLUMN phone TEXT;
# """
#     try:
#         cursor.execute(alter_table_query)
#         print("Table created successfully-Added phone_number column.")
#     except Exception as e:
#         print("error altering Table: ")
#         print(e)

# def alter_table():
#     print("You are inside alter_table")
#     alter_table_query="""
#         ALTER TABLE students ADD COLUMN Address TEXT;
# """
#     try:
#         cursor.execute(alter_table_query)
#         print("Table created successfully-Added address column.")
#     except Exception as e:
#         print("error altering Table: ")
#         print(e)

# def rename_table():
#     print("You are inside rename_table")
#     rename_table_query="""
#             ALTER TABLE users RENAME TO students;
# """
#     try:
#         cursor.execute(rename_table_query)
#         print("Table renamed successfully from users to students.")
#     except Exception as e:
#         print("error renaming Table: ")
#         print(e)


# def insert_single_query():
#     print("You are inside insert_single_query.")
#     insert_single_query="""
#         INSERT INTO students (name, age, address, phone) VALUES (?, ?, ?, ?);
#         """
#     try:
#         cursor.execute(insert_single_query,["mahesh", 15,"alok_chwok",5653475])
#         connection.commit()                     #connection.rollback()
#         print("single record inserted successfully.")
#     except Exception as e:
#         print("Error inserting single record..")
#         print(e)




def read_all_data():
    print("You are inside read_data.")
    cursor.execute("SELECT * FROM STUDENTS")
    rows= cursor.fetchall()
    for row in rows:
        print(row)

def read_column_data():
    cursor.execute("SELECT name, email FROM students")
    rows= cursor.fetchall()
    for row in rows:
        print(row)


def read_conditional_data():
    cursor.execute("SELECT * FROM students WHERE age > ?", (10,))
    rows= cursor.fetchall()
    for row in rows:
        print(row)



def update_single_data():
    print("You are inside update_single_data.")
    cursor.execute("UPDATE students SET age = ? WHERE name = ?", (17, "Prak"))
    connection.commit()
    print("data updated successfully")


def update_multiple_data():
    print("You are inside update_multiple_data.")
    cursor.execute("UPDATE students SET age = age + 1")
    connection.commit()
    print("Multiple records updated successfully")


def delete_data():
    print("You are inside delete_data.")
    cursor.execute("DELETE FROM students WHERE name = ?", ("Prak",))
    connection.commit()
    print("Record deleted successfully")



# create_table()
# add_data()
# read_all_data()
# read_column_data()
# read_conditional_data()
# update_single_data()
# update_multiple_data()
delete_data()
# alter_table()
# rename_table()
# insert_single_query()