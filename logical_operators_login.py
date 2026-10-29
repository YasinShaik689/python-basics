username = input("enter the user name: ")
password = input("enter the password: ")
if username == "keerthana" and password == "keerthana.python":
    print("login successful")
else:
    print("login failed")
if username == "janu" or password == "keerthana.java":
    print("login successful")
else:
    print("login failed")
print(not username)
