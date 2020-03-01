import sqlite3
conn = sqlite3.connect("myDB.db")
cursor = conn.cursor()

cursor.execute("""Create table Phone_book
                   (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT,
                    phone TEXT NOT NULL,
                    comment TEXT)""")
conn.commit()