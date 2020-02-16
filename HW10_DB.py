import sqlite3
conn = sqlite3.connect("myDB.db")
cursor = conn.cursor()

cursor.execute("""Create table Employees
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT,
                    address TEXT)""")
cursor.execute("""Create table Salary
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_Employee INTEGER,
                    years_of_experience REAL,
                    salary REAL,
                    FOREIGN KEY (id_Employee) REFERENCES Employees(id))""")
cursor.execute("""Create table Positions
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_Employees INTEGER,
                    department TEXT,
                    position TEXT,
                    FOREIGN KEY (id_Employees) REFERENCES Employees(id))""")
conn.commit()
