class Admin:
    def __init__(self):
        self.name = ""
        self.username = "admin"
        self.pwd = "passw0rd"
        self.account_lock = False
        self.no_of_attempts = 3
        self.hundreds = 0
        self.two_hundreds = 0
        self.five_hundreds = 2
        self.two_thousands = 5
        self.balance = 11000

    
    def show_menu(self):
        while True:
            self.choice = int(input("\n###################\n\
Menu: (choose item no. like 1 or 2) \n\
1. Check total balance\n\
2. Cash deposit\n\
3. Notification\n\
4. Exit\n\n\
\
Choice: "))
            print("\n----------------\n")

            if self.choice == 1:
                self.total_balance()
            elif self.choice == 2:
                self.cash_deposit()
            elif self.choice == 3:
                pass
            elif self.choice == 4:
                print("Thanks you! Exiting . . .")
                break
            else:
                print("\nInvalid choice. Please enter correct choice again.")

    
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
            print(f"Total balance = {self.balance}")
            print(f"Denominations:\n\
100 = {self.hundreds}\n\
200 = {self.two_hundreds}\n\
500 = {self.five_hundreds}\n\
2000 = {self.two_thousands}")


    def cash_deposit(self):
        if self.login():
            deposit_amount = int(input("Enter deposit amount: "))
            if deposit_amount <= 300000:
                print("Enter denominations below:")
                self.hundreds += int(input("100: "))
                self.two_hundreds += int(input("200: "))
                self.five_hundreds += int(input("500: "))
                self.two_thousands += int(input("2000: "))
                self.balance += self.hundreds*100 + self.two_hundreds*200 + self.five_hundreds*500 + self.two_thousands*2000
                print("Amount has been added to your account!")
            else:
                print("Maximum deposit limit reached of 3 lakhs.")
    