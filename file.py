# My Modules
from extra_functions import *

# In-Built Modules
import os
from datetime import datetime


# A Class which somewhat represents a File in a File System
class File:
    def __init__(self, file_name, file_path):
        self.name = file_name
        self.type = "f"
        self.path = file_path
        self.parent_path = give_parent_path(file_path)
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

    def rename(self, new_name):
        self.name = new_name
        os.rename(self.path, self.parent_path + "\\" + self.name)

    def delete(self):
        os.remove(self.path)
        return self.parent_path
