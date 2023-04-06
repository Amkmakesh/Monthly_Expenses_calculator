import sqlite3

def table_crete():
    con = sqlite3.Connection("Exp_web.dp")

    cursor = con.cursor()

    Table = """CREATE TABLE if not exists Exp
                (ID INTEGER NOT NULL PRIMARY KEY,
                Date DATE,
                Category VARCHAR(100),
                Amount FLOAT, 
                Remarks VARCHAR(100));"""

    cursor.execute(Table)
    con.close()
