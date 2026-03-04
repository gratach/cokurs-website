from .html_building_blocks import *

def createProjectHTMLTile(filestream, projectJSON, scratchURLPrefix):
    if projectJSON["typ"] == "gif":
        filestream.write(gifbox%(projectJSON["inh"]["thumbpfad"], projectJSON["titel"], projectJSON["inh"]["gifpfad"]))
    elif projectJSON["typ"] == "svg":
        filestream.write(svgbox%(projectJSON["inh"]["svgpfad"], projectJSON["inh"]["svgpfad"], projectJSON["titel"]))
    elif projectJSON["typ"] == "audio":
        filestream.write(audiobox%(projectJSON["titel"], projectJSON["inh"]["audiopfad"]))
    elif projectJSON["typ"] == "bitmap":
        filestream.write(bitmapbox%(projectJSON["inh"]["bitmappfad"], projectJSON["inh"]["thumbpfad"], projectJSON["titel"]))
    elif projectJSON["typ"] == "schrift":
        filestream.write(schriftbox%(projectJSON["inh"]["schriftpfad"], projectJSON["inh"]["thumbpfad"], projectJSON["titel"]))
    elif projectJSON["typ"] == "html":
        filestream.write(htmlbox%(projectJSON["inh"]["pfad"], projectJSON["titel"], projectJSON["titel"]))
    elif projectJSON["typ"] == "scratch":
        filestream.write(scratchbox%(scratchURLPrefix, projectJSON["inh"]["project-id"], projectJSON["titel"], projectJSON["titel"]))
    elif projectJSON["typ"] == "dreid":
        filestream.write(dreidbox%(projectJSON["inh"]["progpfad"], projectJSON["inh"]["thumbpfad"], projectJSON["titel"]))