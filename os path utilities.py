# Anoushka Saha
# OS Path Utilities
# Python for Data Analysis
# July 10th, 2024

# Importing necessary modules
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print name of operating system
    print(os.name)

    # Checking for item existence and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file: ", path.isfile("textfile.txt"))
    print("item is a directory: ", path.isdir("textfile.txt"))

    # Working with file paths
    print("Item's path: ", path.realpath("textfile.txt"))
    print("Item's path and name: ", path.split(path.realpath("textfile.txt")))

    # Get modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been ", td, " since the file was modified.")
    print ("Or, ", td.total_seconds(), " seconds.")



if __name__ == "__main__":
    main()