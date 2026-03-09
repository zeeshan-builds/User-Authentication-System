# Python User Authentication System

A simple command-line authentication system written in Python.
Users can sign up, log in, view registered users, and delete their account.
Passwords are hashed using SHA-256 and stored in a JSON file.

This project demonstrates basic concepts of:
- User authentication
- Password hashing
- JSON data storage
- CLI based interaction

# Features

- User registration (Sign Up)

- Login authentication

- Password hashing with SHA-256

- View registered users
- Delete current user account

Data persistence using JSON

# How It Works

The program loads user data from users.json.

The user selects an option from the main menu:

Sign Up

Login

Exit

After a successful login, the user enters a dashboard where they can:

View all users

Delete their account

Logout

Passwords are hashed before storage, so the actual password is never saved in plain text.

# file Structure
user-authentication-system/
│
├── main.py
├── storage.py
├── users.json
└── README.md

main.py

Controls the main program flow and menu system.

storage.py

Contains the main logic of the system such as:

user registration

login validation

password hashing

loading and saving users

users.json

Stores user data in JSON format.

Example structure:
[
    {
        "name": "zeeshan",
        "password": "hashed_password_here"
    }
]
# Installation:


Clone the repository:

git clone https://github.com/zeeshan-builds/user-authentication-system.git

Move into the project folder:

cd user-authentication-system

Run the program:

python main.py

# Known Bugs / Limitations

The exit option prints a message but does not stop the program loop.

No protection against invalid menu input (non-numeric values may crash the program).

Password hashing does not include salting.

Any logged-in user can see all usernames.

Unlimited login attempts are allowed.

# Future Improvements

Possible improvements for the project:

Use bcrypt instead of SHA-256

Add password salting

Hide password input using getpass

Add proper input validation

Store data in SQLite instead of JSON

Add login attempt limits

Implement user roles (admin / normal user)

# Author

Zeeshan
Software Engineering Student
