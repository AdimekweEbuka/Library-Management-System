import time
import sqlite3

class LibManagementSystem:
    """
    This class is for the library management system, it contains the login  function and 
    also the authenticate function

    """
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
                print(tableList)


    def main(self):
        """
        This function is the main function that starts everything and it is called first when the system is launched
        from this function the Login function and the registeration function are called
    
        """
        while True:
            print("-"*60)
            user_input = input("Welcome to the Adimekwe Ebuka Library.\n1. Login\n2. Register\n3. Exit\n")
            print("-"*60)
            if user_input == "1":
                LibManagementSystem.loginAuthentication(self)
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("A bientot!!")
                exit()
            else:
                print("Invalid Input. Please enter a valid input.")
                time.sleep(1.5)


#Here we create an instance of the class and then call the main function to start the process
rr = LibManagementSystem()
rr.main()
