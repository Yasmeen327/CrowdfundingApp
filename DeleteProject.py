PROJECTS_FILE = "projects.txt"


def DeleteProject(userEmail, searchTitle):
    try:
        with open(PROJECTS_FILE, "r") as fileObj:
            all_lines = fileObj.readlines()

        keep_list = []
        deleted = False

        for line in all_lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")

            if len(parts) >= 6:
                if parts[0] == userEmail and parts[1] == searchTitle:
                    deleted = True
                    continue  # skip this line to delete it
            keep_list.append(line + "\n")

        with open(PROJECTS_FILE, "w") as fileObj:
            fileObj.writelines(keep_list)

        if deleted:
            print("Project successfully deleted.")
        else:
            print("Project not found or access denied.")
    except FileNotFoundError:
        print("Error: projects.txt not found.")
