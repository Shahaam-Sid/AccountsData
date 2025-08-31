import csv
import hashlib

class User:
    """
    User Management Class

    This class handles user registration, password management, and login using
    a CSV file as the data store. Passwords are securely hashed using SHA-256.

    Attributes:
    -----------
    filePath : str
        Class attribute representing the path to the CSV file storing user accounts.
    username : str
        The username of the user.
    email : str
        The user's email address.
    password : str
        The user's hashed password.
    """    
    
    filePath = "AccountsData/data.csv"
    
    def __init__(self, username):
        """
        Initialize a User instance.

        Parameters:
        -----------
        username : str
            The username for the new user.
        
        Initializes:
        ------------
        email : str
            Empty string initially, to be set using getEmail().
        password : str
            Empty string initially, to be set using getPassword().
        """
        
        self.username = username
        self.email = ""
        self.password = ""
        
    def getEmail(self):
        """
        Prompt the user to enter a valid and unique email address.

        The method repeatedly asks for input until the email is:
            1. Properly formatted.
            2. Not already used in the CSV file.

        Sets:
        -----
        self.email : str
            The validated and unique email for the user.
        """
        
        while True:
            self.email = self.emailFormating()
            emailExists = False

            try:
                with open(self.__class__.filePath, "r", newline="") as file:
                    content = csv.DictReader(file)
                    for row in content:
                        if row["email"] == self.email:
                            print("Email Occupied, Enter Again")
                            emailExists = True
                            break  # No need to check further

            except FileNotFoundError:
                print("File Not Found")

            if not emailExists:
                break

    def emailFormating(self):
        """
        Prompt the user to enter a properly formatted email address.

        The method ensures:
            - The email contains '@'.
            - '@' is not at the start or end.
            - The domain contains '.' (like .com, .net).

        Returns:
        --------
        str
            The validated email address entered by the user.
        """        
        
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
        """
        Prompt the user to enter a password that meets length requirements,
        is unique, and is confirmed by entering twice.

        The method repeatedly asks until:
            1. Password length is between 8-15 characters.
            2. Password is not already used in the CSV file.
            3. Password matches the confirmation entry.

        Sets:
        -----
        self.password : str
            The validated and hashed password.
        """
        
        passMatch = False

        while not passMatch:
            passUnique = False

            while not passUnique:
                passOnce = self.__class__.encoder(self.passFormating())
                passwordExists = False

                try:
                    with open(self.__class__.filePath, "r", newline="") as file:
                        content = csv.DictReader(file)
                        for row in content:
                            if row["password"] == passOnce:
                                print("Password Occupied, Enter Again")
                                passwordExists = True
                                break

                except FileNotFoundError:
                    print("File Not Found")

                except Exception as e:
                    print("An Error Occurred:", e)

                if not passwordExists:
                    passUnique = True

            passTwice = self.__class__.encoder(input("Enter Password Again: "))
            if passOnce == passTwice:
                self.password = passOnce
                passMatch = True
            else:
                print("Passwords do not match, try again.")

    def passFormating(self):
        """
        Prompt the user to enter a password that meets length requirements.

        Requirements:
            - Minimum 8 characters.
            - Maximum 15 characters.

        Returns:
        --------
        str
            The validated raw password entered by the user.
        """
        
        passAcceptable = False
        while not passAcceptable:
            rawPass = input("Enter Password: ")
            if len(rawPass) < 8 or len(rawPass) > 15:
                print("Password must contain atleast 8 and at most 15 characters")
            else:
                passAcceptable = True
            
        return rawPass
    
    def loadData(self):
        """
        Append the user's username, email, and hashed password to the CSV file.

        Handles:
            - FileNotFoundError if the CSV file does not exist.
            - General exceptions during file writing.

        Prints:
            Success or error messages based on the outcome.
        """
        
        data = [self.username, self.email, self.password]
        try:
            with open(self.__class__.filePath, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
                print("Signed up Succesfully")
        except FileNotFoundError:
            print("File Does not exist")
        except Exception:
            print("An Error Occured")   
            
    @classmethod
    def login(cls):
        """
        Authenticate a user by email and password.

        Prompts the user for email and password, hashes the input password,
        and checks against stored data in the CSV file.

        Prints:
            - Login success message if credentials match.
            - Error message if email or password is incorrect.
        """
        
        email_logging = input("Enter your E-mail: ")
        emailMatched = False
        
        try:
            with open(cls.filePath, "r", newline="") as file:
                content = csv.DictReader(file)
                for row in content:
                    if row["email"] == email_logging:
                        emailMatched = True
                        break
                    
            if emailMatched:
                pass_logging = cls.encoder(input("Enter your Password: "))
                passMathched = False
                
                with open(cls.filePath, "r", newline="") as file:
                    content = csv.DictReader(file)
                    for row in content:
                        if (row["email"] == email_logging) and (row["password"] == pass_logging):
                            passMathched = True
                            break
                        
                if passMathched:
                    print("You Haved Logged in")
                    
                else:
                    print("Wrong Password | Try again")
                
                
                
            else:
                print("Wrong Email | Try Again")
            
        except FileNotFoundError:
            print
        
        
    @staticmethod
    def encoder(base):
        """
        Hash a password using SHA-256.

        Parameters:
        -----------
        base : str
            The plain text password to hash.

        Returns:
        --------
        str
            The SHA-256 hexadecimal digest of the input password.
        """
        
        h = hashlib.new("SHA256")
        
        correct_password = base
        h.update(correct_password.encode())
        
        hash_password  = h.hexdigest()
        return hash_password