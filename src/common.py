'''
    All global functions and variables will be stored in this module
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 9:57 PM, August 16, 2022
    Updated: Added a title to print() for listing projects
'''

import os


def list_projects():
    '''Create a list of all projects and return a list of them'''

    return sorted(os.listdir("contents"))

def print_projects(projects):
        '''print all projects that are existed'''

        print("\n--- LIST OF ALL EXISTING PROJECTS ---\n")
        for i, project in enumerate(projects, start=1):
            print(f"\t({i}) {project}")