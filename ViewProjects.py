PROJECTS_FILE = "projects.txt"


def ViewProjects(userEmail):
    print(" Searching for your projects..")
    found_any = False
    try:
        with open(PROJECTS_FILE, "r") as fileObj:
            for line in fileObj:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(":")
                if len(parts) >= 6:
                    email = parts[0]
                    title = parts[1]
                    details = parts[2]
                    target = parts[3]

                    if email == userEmail:
                        found_any = True
                        print("-" * 20)
                        print(f"Title:   {title}")
                        print(f"Details: {details}")
                        print(f"Target:  {target}")

        if not found_any:
            print(" No projects found for your account")

    except FileNotFoundError:
        print(" Error: The projects.txt file does not exist.")

    input("\nPress Enter to return to the menu...")
