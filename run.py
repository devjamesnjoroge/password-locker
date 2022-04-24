import passwords

print('Welcome to the password locker app, created with love by devJamesNjoroge')

print(
    """
    Choose one option:
    1. Login
    2. Create new account
    """ 
)

option_selected = str(input())

while option_selected != '1' and option_selected != '2':
    print("Try again, options available are 1 or 2")
    option_selected = str(input())


if option_selected == "1":
    print('Welcome back user, Please enter your username')
    username = str(input())
    print('Enter your account password')
    password = str(input())

elif option_selected == "2":
    print("Create a new account")
    print("Enter username you want")
    username = str(input())
    print(
        """
        [1] Generate password or
        [2] Create your own password
        """
        )
    password_option = str(input())

    while password_option == '' or password_option != '1' and password_option != '2':
        print("Try again, options available are 1 or 2")
        password_option = str(input())

    if password_option == "1":
        password = passwords.Credentials.generatePassword(12)
        print(f"your password is {password} please copy it")

    elif password_option == "2":
        print("Enter your password")
        password = str(input())
    passwords.User.user_list = username, password
    
        
    # LOGIN FUNCTION TO VERIFY IF A USER ALREADY EXISTS


    print('Welcome back user, Please enter your username')
    username = str(input())
    print('Enter your account password')
    password = str(input())
    if passwords.User.user_list[0] == username and passwords.User.user_list[1] == password:
        print("login successful")
    else:
        print("Invalid credentials")


