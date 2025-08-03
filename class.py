import csv

class User:
    
    filePath = "AccountsData/data.csv"
    
    def __init__(self, username):
        self.username = username
        self.email = ""
        self.password = ""
        
    def getEmail(self):
        emailUnique = False
        
        while not emailUnique:
            self.email = input(f"{self.username} Enter your E-mail: ")
            try:
                with open(User.filePath, "r", newline="") as file:
                    content = csv.DictReader(file)
                    
                    for row in content:
                        if row["email"] == self.email:
                            print("Email Already Exists, Enter Again")
                        
                        else:
                            emailUnique = True
                            
                
            except FileNotFoundError:
                print("Data File not found")
            except Exception as e:
                print("An Error has occured")
    
    
    
    def getPassword(self):
        passMatch = False
        
        while passMatch == False:
            passOnce = input(f"Enter Password: ")
            passTwice = input(f"Enter Password Again: ")
            if passOnce == passTwice:
                self.password = passOnce
                passMatch = True
            else:
                print("Password not match, Try again")
            
    def __str__(self):
        return f"Username: {self.username}, E-mail: {self.email}, Password: {self.password}"
    
    def loadData(self):
        data = [self.username, self.email, self.password]
        try:
            with open(User.filePath, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
                print("Data Saved")
        except FileNotFoundError:
            print("File Does not exist")
        except Exception:
            print("An Error Occured")   
            
            
            


#testing

username = input("Enter Your Username: ")

x = User(username)

x.getEmail()
x.getPassword()

print(x)

x.loadData()
