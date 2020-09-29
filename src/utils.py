from pathlib import Path
from sys import platform

""" This scripts contain utility functions to aide in the development of the wrapper, server and requests """


# get the project root dynamically
def get_project_root() -> Path:
    return Path(__file__).parent.parent

# get the absolute path of a subdirectory
def get_path(path):
    # if platform == "linux" or platform == "linux2" or platform == "darwin":
    #     continue
    return str(get_project_root()) + path