from userdata import User
            

username = input("Enter Your Username: ").strip()
x = User(username)

x.getEmail()
x.getPassword()
x.loadData()