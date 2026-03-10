import json
import os
import hashlib


BASE_DIR = os.path.dirname(__file__)
data_file = os.path.join(BASE_DIR, "users.json")
# data_file="users.json"

def load_users():
    if not os.path.exists(data_file):
        return []
    
    with open(data_file,"r") as file:
        storage=json.load(file)
        return storage

def save_users(storage):
    with open(data_file, "w") as file:
        json.dump(storage,file,indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def sign_up(data):
    username=input("Enter your username: ")
    if not username:
        print("enter a valid username")
        return
    for d in data:
        if username == d["name"]:
            print("your username is taken by someone,plz try again")
            return
    password=input("Enter your password: ")
    if len(password)<6:
        print("enter more than 6 characters")
        return
    
    new_data={
        "name":username,
        "password":hash_password(password)
    }
    data.append(new_data)
    save_users(data)

    print("user registered successfully")


def login(data):
    username=input("Enter your username: ")
    password=input("Enter your password: ")
   
    for d in data:
        if username == d["name"] and hash_password(password) == d["password"]:
            print("welcome to the system")
            return username
   
    print("your credentials are not okay")
    return False

def delete_user(data, current_user):

    for i in range(len(data)):
        if data[i]["name"] == current_user:

            data.pop(i)       
            save_users(data)   

            print("account deleted")
            return True

    print("user not found")
    return False

        

def user_dashboard(data, current_user):

    while True:
        print(f"Welcome  {current_user}")
        print("--- User Dashboard ---")
        print("1- View users")
        print("2- Delete my account")
        print("3- Logout")

        choice = input("choose: ")

        if choice == "1":
            for d in data:
                print("->", d["name"])

        elif choice == "2":
            deleted=delete_user(data,current_user)
            if deleted:
                break


        elif choice == "3":
            print("logging out...")
            break
