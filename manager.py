import db_connection

def manager_features():
    print('hello admin')
    print("what's in your mind")
    while True:
        print('1 to modify the menu')
        print('2 to remove a customer account' )
        print('any key exit')
        manager_chooise=input('enter the chooise: ')
        if manager_chooise=='1':
            while True:
                print('you are in menu modifying section')
                print('1 to add item')
                print('2 to remove item')
                print('3 to add catagory')
                print('4 to remove catagory')
                print('any key to exit')
                menu_modification_chooise=input('enter the chooise: ')
                if menu_modification_chooise=='1':
                    try:
                        cat_id=input('enter the catagory ID: ')
                        item_name=input('enter the item name: ')
                        price=int(input('enter the price: '))
                        available=input('enter the availability(y or n): ').upper()
                        db=db_connection.connection()
                        cursor=db.cursor()
                        cursor.execute("""
                            insert into products (product_id,CATEGORY_ID,PRODUCT_NAME,price,IS_AVAILABLE) values ('P'||product_id_seq.nextval,:1,:2,:3,:4)
                        """,(cat_id,item_name,price,available))
                        db.commit()
                        cursor.close()
                        db.close()
                        print(f'{item_name} added')
                    except Exception as e:
                        print(e)
    
                elif menu_modification_chooise=='2':
                    try:
                        while True:
                            prod_id=input('enter the product_id: ')
                            db=db_connection.connection()
                            cursor=db.cursor()
                            cursor.execute("""
                                select * from products where product_id=:1
                            """,(prod_id,))
                            details=cursor.fetchone()
                            if details:
                                print(f"item you want to delete is {details[1]}category's item is {details[2]}")
                                print('1 to conform delete of item')
                                print('any key to exit')
                                item_romove_chooise=input('enter the chooise: ')
                                if item_romove_chooise=='1':
                                    cursor.execute("""
                                        delete from products where product_id=:1
                                    """,(prod_id,))
                                    db.commit()
                                    cursor.close()
                                    db.close()
                                    print(f'{details[2]} is deleted')
                                else:
                                    break
                            else:
                                print('product is not present in menu')
                                print('1 to reenter item details')
                                print('any key to exit')
                                chooise=input('enter the chooise: ')
                                if item_romove_chooise!='1':
                                    print('item deletion process ended')
                                    break
                    except Exception as e:
                        print(e)
                elif menu_modification_chooise=='3':
                    try:
                        cat_name=input('enter the category name: ')
                        db=db_connection.connection()
                        cursor=db.cursor()
                        cursor.execute("""
                            insert into CATEGORIES (CATEGORY_ID,CATEGORY_NAME) values ('CAT'||prod_cat_id_seq.nextval,:1)
                        """,(cat_name,))
                        db.commit()
                        cursor.close()
                        db.close()
                        print(f'{cat_name} added')
                    except Exception as e:
                        print(e)
                elif menu_modification_chooise=='4':
                    try:
                        while True:
                            cat_id=input('enter the category_id: ')
                            db=db_connection.connection()
                            cursor=db.cursor()
                            cursor.execute("""
                                select * from CATEGORIES where category_id=:1
                            """,(cat_id,))
                            details=cursor.fetchone()
                            if details:
                                print(f"category you want to delete is {details[1]}")
                                print('1 to conform delete of catagory')
                                print('any key to exit')
                                cat_romove_chooise=input('enter the chooise: ')
                                if cat_romove_chooise=='1':
                                    cursor.execute("""
                                        delete from CATEGORIES where CATEGORY_ID=:1
                                    """,(cat_id,))
                                    db.commit()
                                    cursor.close()
                                    db.close()
                                    print(f'{details[1]} is deleted')
                                else:
                                    break
                            else:
                                print('catagory is not present in menu')
                                print('1 to reenter catagory details')
                                print('any key to exit')
                                chooise=input('enter the chooise: ')
                                if item_romove_chooise!='1':
                                    print('catagory deletion process ended')
                                    break
                    except Exception as e:
                        print(e)
                else:
                    break

    
        elif manager_chooise=='2':
            print('you are in user removing section')
            print('are you sure')
            print('1 to proceed')
            print('any key to exit')
            chooise=input('enter the chooise: ')
            if item_romove_chooise=='1':
                try:
                    while True:
                        user_id=input('enter the cust_id: ')
                        db=db_connection.connection()
                        cursor=db.cursor()
                        cursor.execute("""
                               select * from customers where cust_id in (:1)
                        """,(user_id,))
                        credentials=cursor.fetchone()
                        if credentials:
                            print(f'conform to delete {credentials[1]}')
                            print('1 to conform')
                            print('any key to exit')
                            chooise=input('enter your chooise: ')
                            if chooise=='1':
                                cursor.execute("""
                                delete from customers where cust_id in (:1)
                                """,(user_id,))
                                db.commit()
                                cursor.close()
                                db.close()
                                print(f'{credentials[1]} is deleted')
                                break
                            else:
                                print('user deletion process ended')
                                break
                        else:
                            print('user not found')
                            print('1 to reneter')
                            print('any key to exit')
                            user_not_found_chooise=input('enter your chooise: ')
                            if user_not_found_chooise!='1':
                                print('exiting customer deleting section')
                                break
                except Exception as e:
                    print(e)
            else:
                print('exiting customer deleting section')
        else:
            print('bye admin')
            return