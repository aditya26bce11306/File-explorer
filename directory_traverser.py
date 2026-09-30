# My Modules
from extra_functions import *

# Built-In Modules
import os


# Function which uses recursion to call itself until given command to stop traversing the File System
# Could have used for loop, but wanted to understand recursion using this function
def traverse(path, stop=False):
    print("-----Traversing-----")
    print("Current Path: ", path)
    os.system("clear")
    # Printing the Current Path this Function is currently inspecting
    # Setting the "stop" condition for the recursion
    # That being, if the "stop" parameter is True, stop the recursion and return the accumulated value
    if stop == True:
        return path
    # Listing the files and folders inside the current folder
    root, dirs, files = next(os.walk(path))
    folder_objs = dirs + files
    for i in range(len(folder_objs)):
        print(f"{i + 1}: {folder_objs[i]}")
    # Asking the user to select a folder object to select
    folder_index = int(
        input("Enter the number you want to access(0 to end/-1 to parent folder): ")
    )
    # If user enters '0', then the function stops there, and returns the current path
    if folder_index == 0:
        return traverse(path, True)
    elif folder_index == -1:
        parent_path = give_parent_path(path)
        return traverse(parent_path, False)
    else:
        # The path after adding the folder object into the current path
        extended_path = os.path.join(path, folder_objs[folder_index - 1])
        # If the folder object is a "directory", call the function again with the new path
        if os.path.isdir(extended_path):
            return traverse(extended_path, False)
        else:
            # If the folder object is a "file", call the function with 'stop' parameter being True, effectively stopping the recursion
            return traverse(extended_path, True)
