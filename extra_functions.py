# A file which contains functions I didn't where else to put

# Gives the Parent Folder of a Given Path
def give_parent_path(path):
    rev_path = path[::-1]
    separator_index = rev_path.index("\\")
    parent_path = path[: len(path) - separator_index - 1]
    if parent_path.count("\\") == 0:
        return parent_path + "\\"
    return parent_path


# Gives the Last Opened File/Folder in a Given Path
def give_latest_folder_name(path):
    rev_path = path[::-1]
    separator_index = rev_path.index("\\")
    folder_name = rev_path[:separator_index][::-1]
    return folder_name


# Converts size given in bytes to human readable language
def human_readable_size(size_bytes):
    for size_indicator in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {size_indicator}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"
