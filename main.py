from userdata import User

data = ["username", "email", "password"]
try:
    
    print(f"""
Sign up -- 1
Log in -- 2
Exit -- 3
""")
    
    while True:
    
        choice = input("Enter your choice(1, 2, or 3) > ")
        
        match choice:
            case "1":
                username = input("Enter Your Username: ").strip()

                x = User(username)
                x.getEmail()
                x.getPassword()
                x.loadData()
            
            case "2":
                User.login()
                break
            
            case "3":
                print("Program Ended")
                break
        
    
except FileNotFoundError:
    print("File Does not exist")
except Exception:
    print("An Error Occured")