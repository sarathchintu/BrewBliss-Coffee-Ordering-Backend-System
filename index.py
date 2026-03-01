import login_or_sign
import admin_login
import manager
import user_panal


print('Hello! welcome to Brew Bliss coffee ☕')
print("what's your mood right now")


while True:
    print('please login or sign to order')
    print('1 to login')
    print('2 to signin')
    print('3 to login into admin panal')
    print('enter any key to exit')
    user_login_chooise=input('enter your chooise: ')
    if user_login_chooise=='1':
        logged_user=login_or_sign.login()
        print(f"welcome {logged_user[1]}")
        if logged_user:
            user_panal.menu()            
            user_panal.adding_cart(logged_user)
            break
        else:
            print('please register, chooise 2nd option')
    elif user_login_chooise=='2':
        sigin=login_or_sign.signin()
        print(sigin)
    elif user_login_chooise=='3':
        logged_admin=admin_login.admin()
        if logged_admin:
            print(logged_admin)
            manager.manager_features()
    else:
        print('Remeber the name pride BREWBLISS')

