import sqlite3
conn = sqlite3.connect("myDB.db")
cursor = conn.cursor()

cursor.execute("""Create table PhoneBook
                   (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT,
                    phone TEXT NOT NULL
                    constraint CK_PhoneBook_phone CHECK (phone LIKE ('[0-9][0-9][0-9])[0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
                    comment TEXT)""")
conn.commit()