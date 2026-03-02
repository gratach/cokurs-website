from .html_building_blocks import *

def createProjectHTMLTile(filestream, projectJSON):
    if projectJSON["typ"] == "gif":
        filestream.write(gifbox%(projectJSON["inh"]["thumbpfad"][1:], projectJSON["titel"], projectJSON["inh"]["gifpfad"][1:]))
    elif projectJSON["typ"] == "svg":
        filestream.write(svgbox%(projectJSON["inh"]["svgpfad"][1:], projectJSON["inh"]["svgpfad"][1:], projectJSON["titel"]))
    elif projectJSON["typ"] == "audio":
        filestream.write(audiobox%(projectJSON["titel"], projectJSON["inh"]["audiopfad"][1:]))
    elif projectJSON["typ"] == "bitmap":
        filestream.write(bitmapbox%(projectJSON["inh"]["bitmappfad"][1:], projectJSON["inh"]["thumbpfad"][1:], projectJSON["titel"]))
    elif projectJSON["typ"] == "schrift":
        filestream.write(schriftbox%(projectJSON["inh"]["schriftpfad"][1:], projectJSON["inh"]["thumbpfad"][1:], projectJSON["titel"]))
    elif projectJSON["typ"] == "html":
        filestream.write(htmlbox%(projectJSON["inh"]["pfad"][1:], projectJSON["titel"], projectJSON["titel"]))
    elif projectJSON["typ"] == "scratch":
        filestream.write(scratchbox%(projectJSON["inh"]["pfad"], projectJSON["titel"], projectJSON["titel"]))
    elif projectJSON["typ"] == "dreid":
        filestream.write(dreidbox%(projectJSON["inh"]["progpfad"][1:], projectJSON["inh"]["thumbpfad"][1:], projectJSON["titel"]))