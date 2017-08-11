import sqlite3
conn = sqlite3.connect('p1database.db')
c = conn.cursor()

conn2 = sqlite3.connect('example.db')
c2 = conn2.cursor()

#load data from c

# Insert a row of data
c2.execute("INSERT INTO loads VALUES (datetime(),"+str(P)+")")

# Save (commit) the changes
conn2.commit()



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn2.close()
