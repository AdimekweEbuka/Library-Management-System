import time
import sqlite3
import random
from User import *

class LibManagementSystem:
    """
    This class is for the library management system, it contains the login  function and 
    also the authenticate function

    """

    def generateRandomNumber():
        random.seed(time.time())

        return random.randint(100, 990)


    def loginAuthentication(self):
        """
            This is the login function, it makes use of sqlite3 to get user information from our database 
            and compares it to user input to validate new users that want to log in to the system.
        """
        user_ID = input("Please input your user ID number:\nEnter 'exit' to cancel\n")
        
        if user_ID == "exit":
            print("Goodbye!")
            exit()
            
        #This try and except block checks for wrong value errors. If a user inputs letters instead of a number value. 
        #or a combination of both, this catches that.
        try:
            user_ID = int(user_ID)
        except ValueError:
            print("Invalid Input. Please ensure your input is a valid.")
            LibManagementSystem.loginAuthentication(self)


        self.conn = sqlite3.connect("NewLibraryDatabase.db")
        self.c = self.conn.cursor()

        with self.conn:
            command = f'SELECT * FROM Users WHERE UserID = :uID'
            self.c.execute(command, {'uID' :user_ID})
            tableList = self.c.fetchone()
            if tableList == None:
                print("This user does not exist")
                LibManagementSystem.main(self)
            else:
                user_password = input("Please input your user password:\n")
                if user_password == tableList[3]:
                    print("Welcome " + tableList[1])
                    Librarian.menu(self)
                else:
                    print("Username or password is incorrect")
                    LibManagementSystem.loginAuthentication(self)


    def registeration(self):
        """
        This method is used to register new users for approval from the resident librarian
        """
        user_name = input("Please enter your name:\n")
        while True:
            user_input = input("Are you a staff or a student?\nPress 1 for student\nPress 2 for staff\n")
            if user_input == "1":
                user_role = "Student"
                break
            elif user_input == "2":
                user_role = "Staff"
                break
            else:
                print("Invalid value, Please enter the correct value.")

        while True:
            user_password1 = input("Please enter your new password\n")
            user_password2 = input("Please re-enter your password\n")
            if user_password1 != user_password2:
                print("Passwords do not match, please re-enter password")
            else:
                user_password = user_password1
                break
        user_ID = LibManagementSystem.generateRandomNumber()

        self.conn = sqlite3.connect("NewLibraryDatabase.db")
        self.c = self.conn.cursor()

        with self.conn:
            self.c.execute("INSERT INTO New_Users VALUES(:UserID, :Username, :UserRole, :UserPassword)", {"UserID": user_ID, "Username": user_name, "UserRole": user_role, "UserPassword": user_password } )
            self.conn.commit()


        print("-"*60)
        print(f"Registeration complete!\nPlease find all your details below.\nUserName: {user_name}\nUser ID: {user_ID}\nUser role: {user_role}\nPLEASE TAKE NOT OF YOUR USER ID. GOODBYE")
        exit()



    def main(self):
        """
        This method is the main function that starts everything and it is called first when the system is launched
        from this function the Login function and the registeration function are called
    
        """
        while True:
            print("-"*60)
            user_input = input("Welcome to the Adimekwe Ebuka Library.\n1. Login\n2. Register\n3. Exit\n")
            print("-"*60)
            if user_input == "1":
                LibManagementSystem.loginAuthentication(self)
            elif user_input == "2":
                LibManagementSystem.registeration(self)
            elif user_input == "3":
                print("A bientot!!")
                exit()
            else:
                print("Invalid Input. Please enter a valid input.")
                time.sleep(1.5)


#Here we create an instance of the class and then call the main function to start the process
rr = LibManagementSystem()
rr.main()
