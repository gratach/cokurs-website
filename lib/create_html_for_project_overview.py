from .html_building_blocks import *
from .create_project_html_tile import createProjectHTMLTile

def createHTMLForProjectOverview(fileStream, projectJSONsList):
    fileStream.write(kopf)
    for projectJSON in projectJSONsList:
        createProjectHTMLTile(fileStream, projectJSON)