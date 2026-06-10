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