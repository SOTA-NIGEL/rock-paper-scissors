username = ()
password = ()

username = input("Enter your username: ")   
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("password verified")
else:
    print("password not verified")
if username != "admin" and password == "1234":
    print("username not verified")
    

