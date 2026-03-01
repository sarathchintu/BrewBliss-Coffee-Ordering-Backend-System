import db_connection

db=db_connection.connection()

cursor=db.cursor()
# cursor.execute("""
#             create table categories(
#             category_id   NUMBER PRIMARY KEY,
#             category_name VARCHAR2(30) UNIQUE NOT NULL)  
# """)

# cursor.execute("""
#             create table products(
#             product_id   NUMBER PRIMARY KEY,
#             category_id  NUMBER,
#             product_name VARCHAR(30) NOT NULL,
#             price NUMBER NOT NULL,
#             is_available CHAR(1) DEFAULT 'Y' CHECK (is_available in ('Y','N')),
#             constraint fk_product_category foreign key(category_id) references categories(category_id))  
# """)

# cursor.execute("""
#             create table customers(
#             cust_id NUMBER PRIMARY KEY,
#             cust_name VARCHAR2(30) unique not null,
#             password VARCHAR2(30) not null,
#             email VARCHAR2(30) unique check(instr(email,'@',1)>0) check(instr(email,'.com',1)>0) not null,
#             mobile_no VARCHAR(16) unique check(length(mobile_no)=10) not null,
#             address VARCHAR(100))
# """)


# cursor.execute("""
#        create table orders(
#                order_id varchar2(20) primary key,
#                cust_id varchar2(20),
#                order_date date default sysdate,
#                total_amount number,
#                status varchar2(30),
#                CONSTRAINT fk_order_user
#                FOREIGN KEY (cust_id)
#                REFERENCES customers(cust_id))
# """)

# cursor.execute("""
#        create table order_items(
#                order_item_id varchar2(20) PRIMARY KEY,
#                order_id varchar2(20),
#                product_id varchar2(30),
#                quantity number,  
#                CONSTRAINT fk_orderitem_order
#                FOREIGN KEY (order_id)
#                REFERENCES orders(order_id),
#                CONSTRAINT fk_orderitem_product
#                FOREIGN KEY (product_id)
#                REFERENCES products(product_id)
#                )
# """)

cursor.execute("""
       create table payments(
               payment_id varchar2(30) PRIMARY KEY,
               order_id varchar2(20),
               payment_method varchar2(30),
               payment_date DATE DEFAULT SYSDATE,
               CONSTRAINT fk_payment_order
               FOREIGN KEY (order_id)
               REFERENCES orders(order_id)
               )
""")


cursor.close()
db.close()




