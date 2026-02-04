from inputvalidation import askforString, checkEmail, validatedPhoneNum
from dataManager import saveUserInFile
import uuid


def userReg():
    print(" User Registration ")
    First_Name = askforString("Enter your First Name: ")
    Last_Name = askforString("Enter your Last Name: ")
    Email = checkEmail("Enter your Email: ")
    Password = input("Enter your Password: ")
    while True:
        confirm_password = input("Confirm your Password: ")
        if confirm_password == Password:
            break
        print("Passwords do not match!")
    Mobile_Phone = validatedPhoneNum("Enter your Mobile phone: ")
    userData = f"{uuid.uuid4()}:{First_Name}:{Last_Name}:{Email}:{Password}:{Mobile_Phone}\n"
    saveUserInFile(userData)
    print(" Registration successful")
    return True
