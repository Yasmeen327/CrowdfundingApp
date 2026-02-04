PROJECTS_FILE = "projects.txt"


def EditProject(userEmail):
    search_title = input(
        "Enter the Title of the project you want to edit: ").strip()

    try:
        file_obj = open(PROJECTS_FILE, "r")
        all_projects = file_obj.readlines()
        file_obj.close()
    except FileNotFoundError:
        print("Error: projects.txt not found.")
        return

    updated_list = []
    found = False

    for line in all_projects:
        line = line.strip()
        if not line:
            continue

        parts = line.split(":")
        if len(parts) >= 6:
            email = parts[0]
            title = parts[1]
            details = parts[2]
            target = parts[3]
            start_date = parts[4]
            end_date = parts[5]

            if title == search_title and email == userEmail:
                found = True
                print(
                    "\nProject Found! Enter new details :")

                new_title = input(f"New Title [{title}]: ").strip() or title
                new_details = input(
                    f"New Details [{details}]: ").strip() or details
                new_target = input(
                    f"New Target [{target}]: ").strip() or target

                updated_line = f"{email}:{new_title}:{new_details}:{new_target}:{start_date}:{end_date}\n"
                updated_list.append(updated_line)
                print("Project updated locally.")
            else:
                # keep the original line if it doesn't match
                updated_list.append(line + "\n")
        else:
            # Keep lines that don't match the format (to avoid losing data)
            updated_list.append(line + "\n")

    if found:
        file_obj = open(PROJECTS_FILE, "w")
        file_obj.writelines(updated_list)
        file_obj.close()
        print("Changes saved successfully to file.")
    else:
        print("Project not found or you do not have permission to edit it.")
