import sqlite3 as sql

qiymat = sql.connect("odam.db")
malumot = qiymat.cursor()
malumot.execute('''
CREATE TABLE IF NOT EXISTS Odamlar(
    ism TEXT
    familiya TEXT
    yosh INTEGER
)
 ''')