def updateIDInScratchProjects(projects, oldScratchProjectsnamesMappedToNewScratchProjectNames):
    return [
        project if not project["typ"] == "scratch" else {
            k: v if not k == "inh" else {
                "project-id" : oldScratchProjectsnamesMappedToNewScratchProjectNames[v["project-id"]]
            } for k, v in project.items()
        } for project in projects
    ]