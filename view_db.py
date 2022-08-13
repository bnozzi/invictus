import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

cn=get_db_connection()
cursor=cn.execute("SELECT * FROM persona")
for fila in cursor:
    print(fila)
cn.commit()
cn.close()