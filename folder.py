# My Modules
from extra_functions import *

# In-Built Modules
import os
from datetime import datetime


# A Class which somewhat represents a Folder in a File System
class Folder:
    def __init__(self, folder_name, folder_path):
        self.name = folder_name
        self.type = "F"
        self.path = folder_path
        self.parent_path = give_parent_path(folder_path)
        self.stats = os.stat(self.path)

    def getCreationTime(self):
        created_timestamp = self.stats.st_birthtime
        readable_creation_time = datetime.fromtimestamp(created_timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return readable_creation_time

    def getModifiedTime(self):
        modified_timestamp = self.stats.st_mtime
        readable_modified_time = datetime.fromtimestamp(modified_timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return readable_modified_time

    def getLastAccessedTime(self):
        lastaccess_timestamp = self.stats.st_atime
        readable_lastaccess_time = datetime.fromtimestamp(
            lastaccess_timestamp
        ).strftime("%Y-%m-%d %H:%M:%S")
        return readable_lastaccess_time

    def getSize(self):
        return human_readable_size(self.stats.st_size)

    def listObjects(self):
        objects = os.listdir(self.path)
        for i in range(len(objects)):
            print(i + 1, ": ", objects[i])

        return objects

    def rename(self, new_name):
        self.name = new_name
        os.rename(self.path, self.parent_path + "\\" + self.name)
        self.path = self.parent_path + "\\" + self.name

    def renameObject(self, object_old_name, object_new_name):
        os.rename(
            self.path + "\\" + object_old_name, self.path + "\\" + object_new_name
        )

    def addObject(self, new_object_name, new_object_type):
        if os.path.exists(self.path + "\\" + new_object_name):
            return -1
        elif new_object_type == "F":
            os.mkdir(self.path + "\\" + new_object_name)
            return 0
        elif new_object_type == "f":
            open(self.path + "\\" + new_object_name, "w").close()
            return 1

    def removeObject(self, object_name):
        object_path = self.path + "\\" + object_name
        if os.path.isdir(object_path):
            os.rmdir(object_path)
        else:
            os.remove(object_path)

    def delete(self):
        os.rmdir(self.path)
        return self.parent_path
