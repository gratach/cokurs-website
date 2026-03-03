def append_project(old_projects_list, new_project, newProjectAuthorIndexMappedToCombinedAuthorIndex):
    old_projects_list_modified = [{k:v for k, v in p.items() if not k in {"id", "von"}} for p in old_projects_list]
    new_project_modified = {k:v for k, v in new_project.items() if not k in {"id", "von"}}
    if not new_project_modified in old_projects_list_modified:
        new_project_modified["id"] = len(old_projects_list)
        if "von" in new_project:
            new_project_modified["von"] = newProjectAuthorIndexMappedToCombinedAuthorIndex[new_project["von"]]
        old_projects_list.append(new_project_modified)
