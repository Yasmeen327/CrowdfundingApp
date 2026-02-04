from registration import userReg
from login import userLogin
from CreateProject import CreateProject
from ViewProjects import ViewProjects
from EditProject import EditProject
from DeleteProject import DeleteProject
from SearchProject import SearchProject


def loginMenu(userEmail):
    while True:
        print(f" Project Management (Logged in as: {userEmail}) ")
        print("[1] Create a Project")
        print("[2] View All Projects")
        print("[3] Edit Your Own Projects")
        print("[4] Delete Your Own Project")
        print("[5] Search For a Project")
        print("[6] Logout")

        choice = input("Your Choice: ").strip()

        if choice == "1":
            CreateProject(userEmail)
        elif choice == "2":
            ViewProjects(userEmail)
        elif choice == "3":
            EditProject(userEmail)
        elif choice == "4":
            title = input("Enter Project Title to delete: ")
            DeleteProject(userEmail, title)
        elif choice == "5":
            title = input("Enter Title to search: ")
            SearchProject(userEmail, title)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print(
                f"Invalid Choice '{choice}'. Please enter a number between 1 and 6.")


def main_menu():
    while True:
        print(" Welcome To Crowd-Funding Console Application")
        print("="*50)
        print("1- Registration")
        print("2- Login")
        print("3- Exit")

        choice = input("Your choice: ").strip()

        if choice == '1':
            userReg()
        elif choice == '2':
            userEmail = userLogin()
            if userEmail:
                loginMenu(userEmail)
        elif choice == '3':
            print("GoodBye")
            exit()
        else:
            print(f"Invalid input '{choice}'. Please enter 1 , 2 , or 3.")


if __name__ == "__main__":
    main_menu()
