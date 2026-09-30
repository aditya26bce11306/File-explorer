# Aditya Halkara
# 26BCE11306
# My Modules
from folder import Folder
from file import File
from extra_functions import *
from directory_traverser import traverse

# Built-In Modules
import os
import time


# Function To Clear Up the Screen
def refresh(path):
    os.system("clear")
    print("---------- FILE EXPLORER -----------")
    print("Current Path: ", path)


# Function to show given arguments in a nice menu way
def show_options(*args):
    for i in range(len(args)):
        print(f"({i + 1}) {args[i]}")
    return args


# The Main Menu of the Explorer
def menulist():
    print("What do you want to do?")
    show_options(
        "Traverse the Filesystem",
        "Add File/Folder in Current Path",
        "Remove File/Folder inside Current Folder",
        "Rename File/Folder inside Current Folder",
        "Rename Current Folder",
        "Delete Current Folder",
        "Get Info About File/Folder inside Current Folder",
        "Get Info About Current Folder",
        "Quit",
    )
    choice = int(input("Enter your choice: "))
    return choice


def main():
    # The Explorer will run until this is False
    quit_explorer = False

    # This will get the Home Folder of the User(Default Path for Explorer to Open in)
    path = os.environ["USERPROFILE"]

    # Variable to keep track of the current folder this program will be inspecting
    current_folder = Folder(give_latest_folder_name(path), path)

    while quit_explorer != True:
        refresh(current_folder.path)
        choice = menulist()

        if choice == 1:
            os.system("clear")
            traversed_path = traverse(current_folder.path)
            if os.path.isdir(traversed_path):
                current_folder = Folder(
                    give_latest_folder_name(traversed_path), traversed_path
                )
            else:
                current_file = File(
                    give_latest_folder_name(traversed_path), traversed_path
                )
                current_folder = Folder(
                    give_latest_folder_name(current_file.parent_path),
                    current_file.parent_path,
                )

        elif choice == 2:
            refresh(current_folder.path)
            print("-----Adding a New File/Folder-----")
            show_options("Folder", "File")
            object_choice = int(input("Enter your choice: "))
            operation_result = None
            if object_choice == 1:
                new_folder_name = input("Enter New Folder Name: ")
                operation_result = current_folder.addObject(new_folder_name, "F")
            elif object_choice == 2:
                new_file_name = input("Enter New File Name: ")
                operation_result = current_folder.addObject(new_file_name, "f")
            if operation_result == -1:
                print("Already Exists! No Need to Create!")
            elif operation_result == 0:
                print("Folder Creation Succesfull!")
            elif operation_result == 1:
                print("File Creation Succesfull!")
            time.sleep(3)

        elif choice == 3:
            refresh(current_folder.path)
            print("-----Removing a File/Folder-----")
            print("What do you want to remove?")
            sub_objects = current_folder.listObjects()
            removal_choice = int(input("Enter your choice: "))
            current_folder.removeObject(sub_objects[removal_choice - 1])

        elif choice == 4:
            refresh(current_folder.path)
            print("-----Renaming a File/Folder-----")
            print("Choose which File/Folder you want To Rename?")
            sub_objects = current_folder.listObjects()
            renaming_choice = int(input("Enter your choice: "))
            new_name = input("Enter New Name: ")
            current_folder.renameObject(sub_objects[renaming_choice - 1], new_name)

        elif choice == 5:
            refresh(current_folder.path)
            print("-----Renaming Current Folder-----")
            new_name = input("Enter New Name: ")
            current_folder.rename(new_name)

        elif choice == 6:
            refresh(current_folder.path)
            path = current_folder.delete()
            current_folder = Folder(give_latest_folder_name(path), path)

        elif choice == 7:
            refresh(current_folder.path)
            print("-----Info About A File/Folder-----")
            print("Select the File/Folder You Want To See Of:")
            sub_objects = current_folder.listObjects()
            object_info_choice = int(input("Enter your choice: "))
            chosen_object = sub_objects[object_info_choice - 1]
            if os.path.isdir(current_folder.path + "\\" + chosen_object):
                object_path = current_folder.path + "\\" + chosen_object
                chosen_folder = Folder(
                    give_latest_folder_name(object_path), object_path
                )
                print("What Info Do You Want To See?")
                show_options(
                    "Date Created", "Date Modified", "Date Last Accessed", "Size"
                )
                info_choice = int(input("Enter your choice: "))
                if info_choice == 1:
                    print(
                        "This Folder was Created on ", chosen_folder.getCreationTime()
                    )
                    time.sleep(5)
                elif info_choice == 2:
                    print(
                        "This Folder was Last Modified on ",
                        chosen_folder.getModifiedTime(),
                    )
                    time.sleep(5)
                elif info_choice == 3:
                    print(
                        "This Folder was Last Accessed on ",
                        chosen_folder.getLastAccessedTime(),
                    )
                    time.sleep(5)
                elif info_choice == 4:
                    print("The Size of this Folder is ", chosen_folder.getSize())
                    time.sleep(5)
            else:
                object_path = current_folder.path + "\\" + chosen_object
                chosen_file = File(give_latest_folder_name(object_path), object_path)
                print("What Info Do You Want To See?")
                show_options("Date Created", "Date Modified", "Date Last Accessed")
                info_choice = int(input("Enter your choice: "))
                if info_choice == 1:
                    print("This Folder was Created on ", chosen_file.getCreationTime())
                    time.sleep(5)
                elif info_choice == 2:
                    print(
                        "This Folder was Last Modified on ",
                        chosen_file.getModifiedTime(),
                    )
                    time.sleep(5)
                elif info_choice == 3:
                    print(
                        "This Folder was Last Accessed on ",
                        chosen_file.getLastAccessedTime(),
                    )
                    time.sleep(5)
                elif info_choice == 4:
                    print("The Size of this Folder is ", chosen_file.getSize())
                    time.sleep(5)

        elif choice == 8:
            refresh(current_folder.path)
            print("-----Info About Current Folder-----")
            print("What Info Do You Want To See?")
            show_options("Date Created", "Date Modified", "Date Last Accessed")
            info_choice = int(input("Enter your choice: "))
            if info_choice == 1:
                print("This Folder was Created on ", current_folder.getCreationTime())
                time.sleep(5)
            elif info_choice == 2:
                print(
                    "This Folder was Last Modified on ",
                    current_folder.getModifiedTime(),
                )
                time.sleep(5)
            elif info_choice == 3:
                print(
                    "This Folder was Last Accessed on ",
                    current_folder.getLastAccessedTime(),
                )
                time.sleep(5)
            elif info_choice == 4:
                print("The Size of this Folder is ", current_folder.getSize())
                time.sleep(5)

        elif choice == 9:
            quit_explorer = True


# Running the Main Function this way so the code in other files won't run
if __name__ == "__main__":
    main()
