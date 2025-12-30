import sqlite3

conn = sqlite3.connect("erp.db")
cursor = conn.cursor()

# CHANGE table name here
cursor.execute("DROP TABLE IF EXISTS items")

conn.commit()
conn.close()

print("Table dropped successfully")
