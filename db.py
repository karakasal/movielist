import sqlite3

conn = sqlite3.connect("movielist.db") 

conn.execute('''    CREATE TABLE IF NOT EXISTS movies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    director TEXT,
                    released INTEGER
                   )''')
conn.commit()
conn.close()
