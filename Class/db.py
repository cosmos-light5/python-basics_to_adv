import sqlite3

connection =sqlite3.connect("students.db")

def create_db():
    print("You are inside creat_db.")

def add_data():
    print("You are inside add_data.")

def read_data():
    print("You are inside read_data.")

def update_data():
    print("You are inside update_data.")

def delete_data():
    print("You are inside delete_data.")



create_db()
add_data()
read_data()
update_data()
delete_data()
