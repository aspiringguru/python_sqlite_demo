import sqlite3
import time, datetime, random
import matplotlib
matplotlib.use("Agg")
#added due to error, possibly due to install configuration

import matplotlib.pyplot as plt

print(matplotlib.get_backend())
import matplotlib.dates as mdates

from matplotlib import style
style.use('fivethirtyeight')



conn = sqlite3.connect("part1.db")

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stufftoplot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT into stufftoplot VALUES(123456, '2016-01-01', 'some keywords', 5)")	
    conn.commit()

def data_insert(unix, date, keyword, value):
    c.execute("INSERT into stufftoplot (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?) ", (unix, date, keyword, value))
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
    value = random.randrange(0,10)
    print ("unix:", type(unix), unix, "value:", value)
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    c.execute("INSERT into stufftoplot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    #c.execute('SELECT * FROM stufftoplot')
    #c.execute("SELECT * FROM stufftoplot WHERE value = '5' AND keyword='python' COLLATE NOCASE")
    #c.execute("SELECT * FROM stufftoplot WHERE value = 3 AND keyword='Python'")
    c.execute("SELECT * FROM stufftoplot WHERE unix > 1529020514")
    data = c.fetchall()
    print (type(data))
    print(data)
    for row in data:
        print (row)


def graph_data():
    c.execute('SELECT unix, value FROM stufftoplot')    
    data = c.fetchall()
    print (type(data))
    dates = []
    values = []
    for row in data:
        print (row[0])
        print (datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    #plt.show()
    plt.savefig("charts/output_chart.png")
    print("chart plotted to file")


def del_and_update():
    c.execute("SELECT * FROM stufftoplot")
    temp = c.fetchall()
    [print (row) for row in temp]
    before = len(temp)
    c.execute("SELECT * FROM stufftoplot WHERE value>5")
    temp = c.fetchall()
    num_matches = len(temp)
    
    c.execute("UPDATE stufftoplot SET value=99 WHERE value=8")
    conn.commit() 
    c.execute("SELECT * FROM stufftoplot")
    temp = c.fetchall()
    [print (row) for row in temp] 
    after = len(temp)
    print ("before:", before)
    print ("after:", after)
    print ("num_matches:", num_matches)

def create_n_rows(n):
    for i in range(n):
        dynamic_data_entry()
        time.sleep(1) 

create_table()
#data_entry()
#data_insert(1111, "2016-01-02", "more keywords", 1)
#data_insert(2222, "2016-01-03", "less keywords", 2)

#dynamic_data_entry()

#    time.sleep(1) 

#select_all_tasks(c)
#read_from_db()
#graph_data()
create_n_rows(10)
del_and_update()

c.close()
conn.close()

