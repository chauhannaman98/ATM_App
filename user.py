import hashlib

class User:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.password_hash = ""
        self.account_lock = False
        self.no_of_attempts = 3
        self.hundreds = 0
        self.two_hundreds = 0
        self.five_hundreds = 0
        self.two_thousands = 0
        self.balance = 0

    
    def get_string_hash(self, string):
        b_string = bytes(string,'UTF-8')
        sha256 = hashlib.sha256()
        sha256.update(b_string)
        return sha256.hexdigest()


    def show_menu(self):
        while True:
            self.choice = int(input("\n###################\n\
Menu: (choose item no. like 1 or 2) \n\
1. Create new account\n\
2. Cash Deposit\n\
3. Cash Withdrawl\n\
4. Total Balance\n\
4. Do you want loan?\n\
5. Exit\n\n\
\
Choice: "))
            print("\n----------------\n")

            if self.choice == 1:
                self.create_account()
            elif self.choice == 2:
                self.cash_deposit()
            elif self.choice == 3:
                self.cash_withdrawl()
            elif self.choice == 4:
                print("Thanks you! Exiting . . .")
                break
            else:
                print("\nInvalid choice. Please enter correct choice again.")


    def set_password(self, password):
        self.password_hash = self.get_string_hash(password)


    def create_account(self):
        self.username = input("Enter username: ")
        self.set_password(input("Enter password: "))
        self.name = input("Enter your name: ")
        print("Account created successfully!")

    
    def login(self):
        if self.account_lock==True:
            print("Account has been locked after failed attempts!")
        else:
            userid = input("Enter username: ")
            password = input("Enter password: ")
            password_hash = self.get_string_hash(password)
            if self.username==userid and self.password_hash==password_hash:
                return True
            else:
                self.no_of_attempts -= 1
                print(f"Incorrect ID or Password! Attempt(s) left: {self.no_of_attempts}")
                if self.no_of_attempts == 0:
                    print("You have more than 3 failed attempts. Account has been locked.")
                    self.account_lock = True
        return False

    
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


    # def update_password(self):
    #     curr_pass = input("Enter your current password: ")
    #     curr_pass_hash = self.get_string_hash(curr_pass)
    #     if curr_pass_hash == self.password_hash:
    #         new_pass = input("Enter new password: ")
    #         new_pass_hash = self.get_string_hash(new_pass)
    #         self.password_hash = new_pass_hash
    #         print("Password updated successfully!")
    #     else:
    #         print("Incorrect current password!")