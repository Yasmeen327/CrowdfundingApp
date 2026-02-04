def saveUserInFile(userData):
    fileObj = open("users.txt", "a")
    fileObj.write(userData)
    fileObj.close()


def userLoginSearch(email_to_find, password_to_check):
    try:
        with open("users.txt", "r") as fileObj:
            for line in fileObj:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")

                #  id=0, fname=1, lname=2, email=3, password=4
                if len(parts) >= 5:
                    if parts[3] == email_to_find and parts[4] == password_to_check:
                        return parts[3]  # email
        return False
    except FileNotFoundError:
        return False
