from links.login import Authentication, auth

def login():
    username = input("Username: ")
    password = input("Password: ")
    return Authentication(username, password).login()

def LoginView():
    login_response = login()

    if login_response.status_code == 200:
        print("Login successful")
        auth.change_authentication_state(True)
    else:
        login() # Recursive call to try again with different credentials