# Anoushka Saha
# Filesystem Shell Methods
# Python for Data Analysis
# July 11th, 2024

# Importing necessary modules
import os
from os import path
import shutil

# Making a duplicate of an existing file
if path.exists("textfile.txt"):

    # Retreive path info from file
    src = path.realpath("textfile.txt")

    # Making backup copy
    dst = src + ".bak"
    shutil.copy(src, dst)