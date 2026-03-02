def append_project(old_projects_list, new_project):
    new_project = new_project.copy()
    indexlesslist = old_projects_list.copy()
    for indexlessproject in indexlesslist:
        if "id" in indexlessproject:
            del indexlessproject["id"]
    if "id" in new_project:
        del new_project["id"]
    if new_project in old_projects_list:
        return old_projects_list
    new_project["id"] = len(old_projects_list)
    old_projects_list.append(new_project)
