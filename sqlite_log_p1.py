import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE loads (date datetime, Wh real, P real)''')

Wh=12
P=110
# Insert a row of data
c.execute("INSERT INTO loads VALUES (datetime(),"+str(Wh)+","+str(P)+")")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
