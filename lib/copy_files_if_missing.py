from shutil import copytree

def copyFilesIfMissing(srcPath, destPath):
    srcPath.mkdir(exist_ok=True)
    destPath.mkdir(exist_ok=True)
    for copyFrom in srcPath.iterdir():
        copyTo = destPath / copyFrom.name
        if copyFrom.is_file():
            with copyFrom.open("rb") as fromf:
                fb = fromf.read()
            if copyTo.exists():
                if not copyTo.is_file():
                    raise Exception(f"Copy from {copyFrom} to {copyTo} failed.")
                with copyTo.open("rb") as tof:
                    tb = tof.read()
                if not fb == tb:
                    raise Exception(f"The files {copyFrom} and {copyTo} exist but are different.")
            with copyTo.open("wb") as tof:
                tof.write(fb)
        elif copyFrom.is_dir():
            if copyTo.exists():
                if not copyTo.is_dir():
                    raise Exception(f"{copyTo} has to be a directory")
                copyFilesIfMissing(copyFrom, copyTo)
            else:
                copytree(copyFrom, copyTo)
