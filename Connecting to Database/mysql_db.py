import MySQLdb

#5 Stepts to interact with Database
#Connect to Database
#Create a cursor object
#Write a sql query
#Commit changes
#Close database connection


def create_table():
    conn = MySQLdb.connect(database='database1',user='root',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = MySQLdb.connect(database='database1',user='root',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = MySQLdb.connect(database='database1',user='root',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = MySQLdb.connect(database='database1',user='root',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item =%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = MySQLdb.connect(database='database1',user='root',password='root',host='localhost')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item =%s",(quantity,price,item))
    conn.commit()
    conn.close()

update(11,6, "coffee cup")
#delete('tea cup')
#insert('tea cup',10,5)
print(view())