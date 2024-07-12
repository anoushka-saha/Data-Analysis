# Anoushka Saha
# Filesystem Shell Methods
# Python for Data Analysis
# July 11th, 2024

# Importing necessary modules
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

if path.exists("textfile.txt.bak"):

    # Retreive path info from file
    src = path.realpath("textfile.txt")

    # Making backup copy
    # dst = src + ".bak"
    # shutil.copy(src, dst)

    # Renaming original file
    # os.rename("textfile.txt", "newfile.txt")

    # ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)

    # More detailed control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")