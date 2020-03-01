import sqlite3
conn = sqlite3.connect("DB.db")
cursor = conn.cursor()

cursor.execute("""Create table Telephone_Book
                   (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT,
                    phone TEXT NOT NULL
                    constraint CK_Telephone_Book_phone CHECK (phone LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
                    comment TEXT)""")
conn.commit()