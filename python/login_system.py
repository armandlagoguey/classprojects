correct_username="admin"
correct_password="password123"
username=input("Enter your username here: ")
password=input("Enter your password: ")
username=username.lower()
if username==correct_username and password==correct_password:
    print("Login successful")
else:
    print("Wrong credentials")
