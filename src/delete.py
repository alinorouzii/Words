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
import common


class DeleteProject:
    '''Delete one or more (even all) projects'''

    def __init__(self):
        self.projects = common.list_projects()

    # get numbers of all projects we want to delete
    # or get "all" to delete all projects at once

    def del_projects(self):
        '''this method will run deleting projects'''

        # when there is no project
        if not self.projects:
            print("\nNo project exists")
            return False

        # print all projects
        common.print_projects(self.projects)

        