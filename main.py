from admin import Admin
from user import User


if __name__ == "__main__":
    while True:
        choice = int(input("Are you a user or admin? (1 for user; 2 for Admin): "))
        
        if choice == 1:
            # user
            user = User()
            user.show_menu()
            
        elif choice == 2:
            #admin
            admin = Admin()
            admin.show_menu()

        else:
            print("Undefined input. Exiting!")
            break
