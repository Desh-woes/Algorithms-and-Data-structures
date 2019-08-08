import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    outer_arr = []
    _helper_func(suffix, path, outer_arr)
    print(outer_arr)


def _helper_func(suffix, current_path, outer_arr):
    # Define a base case
    if os.path.isfile(current_path):
        if current_path.endswith(".h"):
            outer_arr.append(current_path)
        return

    # Get a list of the directories in the current path
    dir_list = os.listdir(current_path)
    # Loop through all the results and create a new path
    for path in dir_list:
        new_path = current_path+"/"+path
        _helper_func(suffix, new_path, outer_arr)


find_files("c", "./testdir")