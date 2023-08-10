#4.
MAX_ATTEMPTS = 3

def login():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Username: ")
        password = input("Password: ")
        retype_password = input("Re-Type Password: ")

        if password == retype_password:
            print("Login successful!")
            return

        print("Passwords do not match. Please try again.")
        attempts += 1

    print("Too many failed attempts. Login failed.")

login()
