import db_connection
import otp_generator


def menu():
    print('welcome! want some BLISSES?')
    print("what's your mood right now")
    
    db=db_connection.connection()
    cursor=db.cursor()
    cursor.execute("""
        select category_name from categories order by category_id asc
    """)
    category_details=cursor.fetchall()
    for blisses in category_details:
        cursor.execute("""
        select p.product_id,p.product_name,p.price,p.is_available from products p where category_id in (select category_id from categories where category_name=:1)
        """,(blisses))
        menu_details=cursor.fetchall()
        print(blisses[0])
        print(f'{"ID".ljust(4)}{"Name".ljust(20)}{"Price".ljust(8)}{"Available"}')
        print("-" * 45)
        for j in menu_details:
            print(f'{j[0].ljust(4,' ')}{j[1].ljust(20,' ')}₹{str(j[2]).ljust(8,' ')}{j[-1]}')
        print(' ')
    cursor.close()
    db.close()

cart={}

def adding_cart(user):
    total_cart_val=0
    products=[]
    print('chooise the bliss you want')
    while True:
        item=input('enter the product_id you want: ')
        db=db_connection.connection()
        cursor=db.cursor()
        cursor.execute("""
            select * from products where product_id in (:1) 
        """,(item,))
        details=cursor.fetchone()
        cursor.close()
        db.close()
        if details:
            if details[4]=='N':
                print('item not available at this moment')
            else:
                quna=int(input('enter the quantity: '))
                products.append([item,quna])
                cart.update({details[2]:{quna:details[3]}})
                print('want to add more...')
                print('1 to add')
                print('any key to checkout page')
                chooise=input('enter the chooise: ')
                if chooise!='1':
                    break
        else:
            print('entered wrong product_id please try again')
    for item,details in cart.items():
        print(item,end=' ')
        for quan,price in details.items():
            print(f'× {quan} ₹ {price} total {quan*price}')
            total_cart_val+=quan*price
    print(f'Total {total_cart_val}')
    checkout(user,total_cart_val,products)

def checkout(user,amount,products):
    print(f'ready to checkout')
    print(f'yup your order is almost placed')
    print(f'just conform the payment method')
    print('1 to upi')
    print('any to cash on delivery')
    payment_method=''
    chooise=input('enter the chooise: ')
    if chooise=='1':
        payment_method='UPI'
    else:
        payment_method='COD'
    
    try:
        db=db_connection.connection()
        cursor=db.cursor()
        cursor.execute
    
        print('every thing set to go!')
        print('just conform your address')
        
        cursor.execute("""
              select address from customers where cust_id in (:1)
        """,(user[0],))
    
        address=cursor.fetchone()
    
        print(address[0])
        print('1 to change address')
        print('any key to confor and place order')
        addConform_chooise=input('enter the chooise: ')
        if addConform_chooise=='1':
            new_address=input('enter the new address')
            conformed_address=new_address
            print("is this is a premenent address or for this time?")
            print('1 to save as home')
            print('any key for only this time')
            address_change=input('enter the chooise: ')
            if address_change=='1':
                cursor.execute("""
                    update customers set address = :1 where cust_id = :2
                """,(new_address,user[0]))
            else:
                print('this address only used for this time')
        else:
            conformed_address=address[0]
    except Exception as e:
        print(e)
        return

    # order_id_var = cursor.var(str)
    # RETURNING order_id INTO :order_id
    # "order_id":order_id_var
    try: 
        cursor.execute("""select 'O'||order_id_seq.nextval from dual""")
        order_id=cursor.fetchone()[0]
        cursor.execute("""
            insert into orders(order_id,cust_id,order_date,total_amount,status) values (:1,:2,sysdate,:3,:4)
        """,(order_id,user[0],amount,'delivered'))
    
        for i in products:
            cursor.execute("""
                insert into order_items(order_item_id,order_id,product_id,quantity) values ('OI'||order_item_id_seq.nextval,:1,:2,:3)
            """,(order_id,i[0],i[1]))
    
        cursor.execute("""
            insert into payments(payment_id,order_id,payment_method) values ('PAY'||payment_id_seq.nextval,:1,:2)
        """,(order_id,payment_method))
    
    
    
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(e)

    print(f'yaaa!!! your BLISS is on the way')
    print(f'Thankyou Visit Again')
    print(f'delivering to {conformed_address}')
    print(f'Our deliviry Partner will reach you on time')
    try:
        otp=otp_generator.otp_generator()
    except Exception as e:
        print(e)
    print(f'share this otp in the time of deliviry: {otp}')
    print(f'Have a great BLISS - BREWBLISS')




