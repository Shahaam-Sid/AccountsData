
import csv
from userdata import User

data = ["username", "email", "password"]
try:
    with open(User.filePath, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
except FileNotFoundError:
    print("File Does not exist")
except Exception:
    print("An Error Occured")               

username = input("Enter Your Username: ").strip()
x = User(username)

x.getEmail()
x.getPassword()
x.loadData()