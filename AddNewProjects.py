def addProject(projInfo):
    # join elements in the list with a colon
    data = ":".join(projInfo) + "\n"
    fileObj = open("projects.txt", "a")
    fileObj.write(data)
    fileObj.close()
