import AddNewProjects
import inputvalidation


def CreateProject(userMail):
    print(" Create New Project ")
    while True:
        title = input("Project Title: ").strip()
        if title and inputvalidation.checkTitle(title):
            break
        print("Title invalid or already exists.")

    details = input("Project Details: ")
    target = inputvalidation.askforInt("Total Target (numbers only): ")
    start_date = inputvalidation.dateValidated("Start Date (YYYY-MM-DD): ")

    while True:
        end_date = inputvalidation.dateValidated("End Date (YYYY-MM-DD): ")
        if end_date > start_date:
            break
        print("Error: End date must be after start date!")

    projInfo = [userMail, title, details, str(target), start_date, end_date]
    AddNewProjects.addProject(projInfo)
    print("Project saved successfully!")
