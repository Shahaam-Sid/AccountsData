import csv

class User:
    
    filePath = "AccountsData/data.csv"
    
    def __init__(self, username):
        self.username = username
        self.email = ""
        self.password = ""
        
    def getEmail(self):
        while True:
            self.email = self.emailFormating()
            emailExists = False

            try:
                with open(User.filePath, "r", newline="") as file:
                    content = csv.DictReader(file)
                    for row in content:
                        if row["email"] == self.email:
                            print("Email Occupied, Enter Again")
                            emailExists = True
                            break  # No need to check further

            except FileNotFoundError:
                pass

            if not emailExists:
                break

    def emailFormating(self):
        mailAcceptable = False
        while not mailAcceptable:
            rawmail = input(f"{self.username}, Enter your E-mail: ").strip()

            if "@" not in rawmail:
                print("Email must contain '@'")
            elif rawmail.startswith("@") or rawmail.endswith("@"):
                print("'@' cannot be in the start or in the end")
            elif "." not in rawmail.split("@")[-1]:
                print("E-mail must contain .com/.net etc.")
            else:
                mailAcceptable = True
        
        return rawmail     
    
    def getPassword(self):
        passMatch = False

        while not passMatch:
            passUnique = False

            while not passUnique:
                passOnce = input("Enter Password: ")
                passwordExists = False

                try:
                    with open(User.filePath, "r", newline="") as file:
                        content = csv.DictReader(file)
                        for row in content:
                            if row["password"] == passOnce:
                                print("Password Occupied, Enter Again")
                                passwordExists = True
                                break

                except FileNotFoundError:
                    pass
                except Exception as e:
                    print("An Error Occurred:", e)

                if not passwordExists:
                    passUnique = True

            passTwice = input("Enter Password Again: ")
            if passOnce == passTwice:
                self.password = passOnce
                passMatch = True
            else:
                print("Passwords do not match, try again.")

            
    def __str__(self):
        return f"Username: {self.username}, E-mail: {self.email}, Password: {self.password}"
    
    def loadData(self):
        data = [self.username, self.email, self.password]
        try:
            with open(User.filePath, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
                print("Signed up Succesfully")
        except FileNotFoundError:
            print("File Does not exist")
        except Exception:
            print("An Error Occured")   
            
