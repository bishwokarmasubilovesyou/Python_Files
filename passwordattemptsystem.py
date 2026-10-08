correct_username = "admin"
correct_password = "1234"

attempts = 0
login_successful = False

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    attempts += 1

    if username == correct_username and password == correct_password:
        print("Login successful")
        login_successful = True
        break

    else:
        print("Incorrect username or password")
        print("Attempts remaining:", 3 - attempts)

if login_successful == False:
    print("Account locked")