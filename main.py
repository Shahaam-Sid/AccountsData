import csv
from userdata import User

data = ["username", "email", "password"]
try:
    username = input("Enter Your Username: ").strip()

    x = User(username)
    x.getEmail()
    x.getPassword()
    x.loadData()
    
    
except FileNotFoundError:
    print("File Does not exist")
except Exception:
    print("An Error Occured")