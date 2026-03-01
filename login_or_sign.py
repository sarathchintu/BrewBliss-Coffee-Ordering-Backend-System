import db_connection
import otp_generator

def login():
    print('you are in login section')
    while True:
        user_name=input('enter the user name: ')
        db=db_connection.connection()
        cursor=db.cursor()
        cursor.execute("""select cust_id,cust_name,password from customers where cust_name=:1""",(user_name,))
        credentials=cursor.fetchone()
        db.commit()
        cursor.close()
        db.close()
        if credentials:
            while True:
                passcode=input("enter your password: ")
                if credentials[2]==passcode:
                    print('login success')
                    return [credentials[0],user_name]
                else:
                    print('wrong password')
                    print('forgot password?')
                    print('1 to reset password')
                    print('any key to re-enter credentials')
                    user_chooise=input('enter your chooise: ')
                    if user_chooise=='1':
                        forgot_password(user_name)
                        return
        else:
            print('user not found')
            print('new coustmer?')
            print('1 to register')
            print('any key to re-enter credentials')
            user_chooise=input('enter your chooise: ')
            if user_chooise=='1':
                # user=signin()
                # return user
                return
            
def signin():
    print('you are in signin section')
    while True:
        user_name=input('please select your prefered name: ')
        db=db_connection.connection()
        cursor=db.cursor()
        cursor.execute("""select cust_name from customers where cust_name=:1""",(user_name,))
        credentials=cursor.fetchone()
        if credentials:
            print('user name already taken')
            print('re enter the user name')
        else:
            try:
                passcode=input('enter the password: ')
                email=input('enter the email: ')
                mobile=input('enter the mobile: ')
                add=input('enter the address (will be used in delivery time): ')
                cursor.execute("""insert into customers (cust_id,cust_name,password,email,mobile_no,address) values ('c'||CUST_ID_SEQ.nextval,:1,:2,:3,:4,:5)""",(user_name,passcode,email,mobile,add))
                db.commit()
                cursor.close()
                db.close()
                print(f"{user_name} created please login again")
                return f"{user_name}"
            except Exception as e:
                print(e)
    
def forgot_password(user_name):
    print('you are in password change sectuon')
    print(f'password change for {user_name}')
    print('Are you sure to change the password?')
    print('1 to exit the process')
    print('any key to continue')
    user_chooise=input('enter your chooise: ')
    if user_chooise=='1':
        login()
        return
    else:
        while True:
            new_passcode=input('enter the new password: ')
            re_enter=input('re-enter the new password: ')
            if new_passcode==re_enter:
                while True:
                    try:
                        otp=otp_generator.otp_generator()
                        print(otp)
                        enter_otp=int(input('enter the above👆 otp:'))
                        if otp==enter_otp:
                            db=db_connection.connection()
                            cursor=db.cursor()
                            cursor.execute("""
                                update customers set password=:1 where cust_name=:2
                            """,(new_passcode,user_name))
                            db.commit()
                            cursor.close()
                            db.close()
                            print('password changed, please login')
                            login()
                            return
                        else:
                            print('otp is wrong re-enter the otp')
                    except Exception as e:
                        print(e)
            else:    
                print('both should passwords should be same')