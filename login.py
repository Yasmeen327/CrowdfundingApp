from inputvalidation import checkEmail
from dataManager import userLoginSearch


def userLogin():
    while True:
        print(" User Login ")
        print("(Type 'back' to return to main menu)")

        email_input = input("Enter your Email (or 'back'): ").strip()

        # allow user to cancel and go back
        if email_input.lower() == 'back':
            print("Returning to main menu...")
            return None
        password_input = input("Enter your Password: ").strip()
        if password_input.lower() == 'back':
            print("Returning to main menu...")
            return None

        user_email = userLoginSearch(email_input, password_input)

        if user_email:
            print(f"\n Login success! Welcome {user_email}")
            return user_email
        else:
            print("\n Invalid Email or Password.")
            retry = input("Try again? (y/n): ").strip().lower()
            if retry != 'y':
                print("Returning to main menu...")
                return None
