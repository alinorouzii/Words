'''
    This file will handle deletion of 1 or more projects (even all at once)
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 8:52 PM, August 16, 2022
    Updated: Created DeleteProject class
'''

import os

# import my .py modules


class DeleteProject:
    '''Delete one or more (even all) projects'''

    # get a list of all existing projects
    projects = []
    # get numbers of all projects we want to delete
    # or get "all" to delete all projects at once