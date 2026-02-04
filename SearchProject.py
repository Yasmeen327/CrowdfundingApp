PROJECTS_FILE = "projects.txt"


def SearchProject(userEmail, SearchTitle):
    try:
        with open(PROJECTS_FILE, "r") as fileObj:
            for line in fileObj:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")

                if len(parts) >= 6:
                    email, title = parts[0], parts[1]
                    if title == SearchTitle and email == userEmail:
                        print(
                            f"\nProject Found!\nTitle: {parts[1]}\nDetails: {parts[2]}\nTarget: {parts[3]}\nStart: {parts[4]}\nEnd: {parts[5]}")
                        return
            print(f"No project found with title: {SearchTitle}")
    except FileNotFoundError:
        print("Error: projects.txt not found.")
