import storage
data=storage.load_users()

while True:
    print("Welcome to the authentication system built by zeeshan")
    print("1-Sign up")
    print("2-Login")
    print("3-Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        storage.sign_up(data)
    elif choice == 2:
        value=storage.login(data)
        if value:
            storage.user_dashboard(data,value)
    elif choice == 3:
        print("exiting the system")
        storage.save_users(data)
    else:
        print("enter valid option")