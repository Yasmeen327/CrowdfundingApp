import re
import datetime


def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print(" invalid number please enter it again")


def askforString(message):
    while True:
        val = input(message)
        if val.isalpha():
            return val
        print(" invalid string please enter it again ")


def checkEmail(message):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        email = input(message)
        if (re.fullmatch(regex, email)):
            return email
        print(" invalid email please enter it again ")


def ConfirmPasswordFun(password, message):
    while True:
        Confirm = input(message)
        if password == Confirm:
            return True
        print(" passwords do not match ")


def validatedPhoneNum(message):
    while True:
        phone = input(message)
        if phone.isdigit() and len(phone) == 11:
            # Egypt mobile prefixes
            prefixes = ['010', '011', '012', '014', '015']
            if phone[:3] in prefixes:
                return phone
        print(" invalid phone number please enter it again ")


def dateValidated(message):
    date_format = '%Y-%m-%d'
    while True:
        date_string = input(message)
        try:
            datetime.datetime.strptime(date_string, date_format)
            return date_string
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")


def checkTitle(projectTitle):
    try:
        fileObj = open("projects.txt", "r")
        for line in fileObj:
            parts = line.strip().split(":")
            if len(parts) > 1:
                if parts[1] == projectTitle:
                    fileObj.close()
                    return False
        fileObj.close()
    except FileNotFoundError:
        return True

    return True
