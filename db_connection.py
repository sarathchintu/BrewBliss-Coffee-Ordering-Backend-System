import oracledb

oracledb.init_oracle_client(lib_dir=r"c:\oracle\instantclient_19_30")

def connection():
    conn=oracledb.connect(
        user='brewbliss',
        password='tiger',
        dsn='localhost:1521/orcl123'
    )
    return conn

#     cursor=conn.cursor()
#     cursor.execute("select 'hi' from dual")
#     op=cursor.fetchone()
#     print(op)
#     print('connection established')
#     cursor.close()
#     conn.close()

# connection()