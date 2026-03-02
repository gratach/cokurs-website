from .append_contributor import append_contributor
from .append_project import append_project

def appendContributorsAndProjects(oldContributors, oldProjects, newContributors, newProjects):
    newProjectAuthorIndexMappedToCombinedAuthorIndex = {}
    for newContributor in newContributors:
        append_contributor(oldContributors, newContributor, newProjectAuthorIndexMappedToCombinedAuthorIndex)
    for newProject in newProjects:
        append_project(oldProjects, newProject, newProjectAuthorIndexMappedToCombinedAuthorIndex)