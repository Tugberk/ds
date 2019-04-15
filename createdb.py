import sqlite3

conn = sqlite3.connect('dertliler.db')
print 'db opened..'
c = conn.cursor()
c.execute('create table data(ID INTEGER PRIMARY KEY AUTOINCREMENT, entry_no TEXT, dert INTEGER, ip TEXT)')	
conn.commit()