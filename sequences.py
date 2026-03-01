import db_connection

db=db_connection.connection()
cursor=db.cursor()
# cursor.execute("""create sequence cust_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

# cursor.execute("""create sequence prod_cat_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

# cursor.execute("""create sequence product_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

# cursor.execute("""create sequence order_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

# cursor.execute("""create sequence order_item_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

cursor.execute("""create sequence payment_id_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE""")

db.commit()
cursor.close()
db.close()

