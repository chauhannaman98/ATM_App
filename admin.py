class Admin:
    def __init__(self):
        self.username = "admin"
        self.pwd = "passw0rd"
        self.account_lock = False
        self.no_of_attempts = 3
        self.hundreds = 0
        self.two_hundreds = 0
        self.five_hundreds = 2
        self.two_thousands = 5

    
    def login(self):
        if self.account_lock==True:
            print("Account has been locked after failed attempts!")
        else:
            userid = input("Enter username: ")
            password = input("Enter password: ")
            if self.username==userid and self.pwd==password:
                return True
            else:
                self.no_of_attempts -= 1
                print(f"Incorrect ID or Password! Attempt(s) left: {self.no_of_attempts}")
                if self.no_of_attempts == 0:
                    print("You have more than 3 failed attempts. Account has been locked.")
                    self.account_lock = True
        return False
        

    def total_balance(self):
        if self.login():
            print(f"Total balance = {self.hundreds*100 + self.two_hundreds*200 + self.five_hundreds*500 + self.two_thousands*2000}")
            print(f"Denominations:\n\
100 = {self.hundreds}\n\
200 = {self.two_hundreds}\n\
500 = {self.five_hundreds}\n\
2000 = {self.two_thousands}")
        
    
admin = Admin()

while True:
    choice = int(input("\n###################\n\
Menu: (choose item no. like 1 or 2) \n\
1. Check total balance\n\
2. Cash deposit\n\
3. Notification\n\
4. Exit\n\n\
\
Choice: "))
    print("\n----------------\n")


    if choice == 1:
        admin.total_balance()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Thanks you! Exiting . . .")
    else:
        print("\nInvalid choice. Please enter correct choice again.")

    