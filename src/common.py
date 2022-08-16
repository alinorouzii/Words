'''
    All global functions and variables will be stored in this module
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 8:55 PM, August 16, 2022
    Updated: Created list_projects()
'''

import os


def list_projects():
    '''Create a list of all projects and return a list of them'''

    return os.listdir("contents")