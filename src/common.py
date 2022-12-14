'''
    All global functions and variables will be stored in this module
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 10:46 PM, August 16, 2022
    Updated: Changed 'while' loop to 'if' to remove '.DS_Store' from returned list
'''

import os


def list_projects() -> list:
    '''Create a list of all projects and return a list of them'''

    projects = os.listdir("contents")

    if ".DS_Store" in projects:
        projects.remove(".DS_Store")
    
    return sorted(projects)

def print_projects(projects) -> bool:
        '''print all projects that are existed'''

        if not projects:
            print("\nNo project exists")
            return False

        print("\n--- LIST OF ALL EXISTING PROJECTS ---\n")
        for i, project in enumerate(projects, start=1):
            print(f"\t({i}) {project}")

        return True