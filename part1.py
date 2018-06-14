import sqlite3
import time, datetime, random

conn = sqlite3.connect("part1.db")

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stufftoplot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT into stufftoplot VALUES(123456, '2016-01-01', 'some keywords', 5)")	
    conn.commit()

def data_insert(unix, datestamp, keyword, value):
    sql = "INSERT into stufftoplot VALUES("+str(unix)+", "+datestamp+", "+keyword+", "+str(value)+")"
    print ("sql:", sql)
    c.execute(sql)
    conn.commit()

def select_all_tasks(c):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    c.execute("SELECT * FROM stufftoplot")
 
    rows = c.fetchall()
 
    for row in rows:
        print(row)


def dynamic_data_entry():
    unix = time.time()
    print ("unix:", type(unix), unix)
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT into stufftoplot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()
    

create_table()
data_entry()
#data_insert(1111, "2016-01-02", "more keywords", 1)
#data_insert(2222, "2016-01-03", "less keywords", 2)
dynamic_data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1) 

select_all_tasks(c)
c.close()
conn.close()

