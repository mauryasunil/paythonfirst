import sqlite3

conn = sqlite3.connect("erp.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM itemsmaster ")
print(cursor.fetchall())

conn.close()
