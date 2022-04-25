
import passwords

class Run:

    print('Welcome to the password locker app, created with love by devJamesNjoroge')

    print(
        """
        Choose one option:
        1. Login
        2. Create new account
        """ 
    )

    option_selected = str(input("[1] or [2]: "))

    while option_selected != '1' and option_selected != '2':
        print("Try again, options available are 1 or 2")
        option_selected = str(input())


    if option_selected == "1":
        print('Welcome back user, Please enter your username')
        username = str(input())
        print('Enter your account password')
        password = str(input())
        print("User does not seem to exist please create a new account")

    elif option_selected == "2":
        print("Create a new account")
        print("Enter username you want")
        username = str(input("Username: "))
        print(
            """
            [1] Generate password or
            [2] Create your own password
            """
            )
        password_option = str(input("[1] or [2]: "))

        while password_option != '1' and password_option != '2':
            print("Try again, options available are 1 or 2")
            password_option = str(input("[1] or [2]: "))

        if password_option == "1":
            password = passwords.Credentials.generatePassword(12)
            print(f"your password is {password} please copy it")

        elif password_option == "2":
            print("Enter your password")
            password = str(input("Password: "))
        passwords.User.user_list = username, password
        
            
        # LOGIN FUNCTION TO VERIFY IF A USER ALREADY EXISTS


        print('Welcome back user, Please enter your username')
        username = str(input())
        print('Enter your account password')
        password = str(input())
        if passwords.User.user_list[0] == username and passwords.User.user_list[1] == password:
            print("login successful")

            print("What do you want our app to do for you?")
            print(
                """
                [1] Store your existing accounts credentials.
                [2] Create new account credentials.
                [3] View your stored account credentials.
                """
            )

            credentials_option = str(input("[1], [2] or [3] :"))

            while credentials_option == '' and credentials_option != '1' and credentials_option != '2' and credentials_option != 3:
                print("Try again, options available are 1 or 2 or 3")
                credentials_option = str(input("[1] or [2] or [3]: "))

            if credentials_option == '1':
                print("Enter the website address to your account.")
                website = str(input("Website : "))
                print("Enter username or login email used.")
                username = str(input("Username : "))
                print("Enter the password used.")
                password = str(input("Password : "))

                add_credentials = passwords.Credentials(website, username, password)
                add_credentials.save_credentials()
                print(passwords.Credentials.credentials_dict)
            
            elif credentials_option == '2':
                print("Enter the website address to your account.")
                website = str(input("Website : "))
                print("Enter username or login email used.")
                username = str(input("Username : "))
                print(
                    """
                    [1] Generate password or
                    [2] Create your own password
                    """
                    )
                password_option = str(input("[1] or [2]: "))
                while password_option == '' and password_option != '1' and password_option != '2':
                    print("Try again, options available are 1 or 2")
                    password_option = str(input("[1] or [2]: "))

                if password_option == "1":
                    print("What length do you want your password to have?")
                    length = str(input("value between 6 and 12 : "))
                    while length == "" :
                        print("invalid input")
                        length = str(input("value between 6 and 12 : "))

                    password = passwords.Credentials.generatePassword(length)
                    print(f"your password is {password} please copy it")

                elif password_option == "2":
                    print("Enter your password")
                    password = str(input("Password: "))

                add_credentials = passwords.Credentials(website, username, password)
                add_credentials.save_credentials()
                print(passwords.Credentials.credentials_dict)
                
            elif credentials_option == '3':
                print(passwords.Credentials.credentials_dict)


        else:
            print("Invalid credentials")

       


