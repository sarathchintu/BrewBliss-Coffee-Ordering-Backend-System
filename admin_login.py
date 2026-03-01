import db_connection

def admin():
    print('hello admin enter your credentials')
    while True:
        admin_id=input('enter the admin_id: ')
        db=db_connection.connection()
        cursor=db.cursor()
        cursor.execute("""select admin_name,admin_password from admins where admin_id=:1""",(admin_id,))
        credentials=cursor.fetchone()
        cursor.close()  
        db.close()
        if credentials:
            while True:
                passcode=input("enter your password: ")
                if credentials[1]==passcode:
                    print('login success')
                    return credentials[0]
                else:
                    print('wrong password')
                    print('forgot password?')
                    print('1 to reset password')
                    print('any key to re-enter credentials')
                    user_chooise=input('enter your chooise: ')
                    if user_chooise=='1':
                        print('please contact db administer to change password')
                        return
        else:
            print('user not found')
            print('new admin?')
            print('not an admin?')
            print('1 to register')
            print('2 to re-enter credentials')
            print('any key exit admin login section')
            user_chooise=input('enter your chooise: ')
            if user_chooise=='1':
                print('please contact db administer to register')
                return
            elif user_chooise=='2':
                continue
            else:
                print('please re start the app')
                return