'''
    All global functions and variables will be stored in this module
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 9:47 PM, August 16, 2022
    Updated: Added print() to print_projects()
'''

import os


def list_projects():
    '''Create a list of all projects and return a list of them'''

    return sorted(os.listdir("contents"))

def print_projects(projects):
        '''print all projects that are existed'''

        print()
        for i, project in enumerate(projects, start=1):
            print(f"({i}) {project}")