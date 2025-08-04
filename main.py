from userdata import User
            

username = input("Enter Your Username: ")

x = User(username)

x.getEmail()
x.getPassword()

print(x)

x.loadData()