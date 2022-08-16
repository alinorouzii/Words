'''
    This file will handle all orders for creating a project
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 5:05 PM, August 16, 2022
    changes: ?
'''

import json
import os

# import my .py module
import common


class CreateFiles:
    '''this class will create all files for a new project'''
    pass


class CreateProject:
    '''this class will create a new project(directory)'''

    def get_dirname(self):
        '''get the directory name of a new project and return it'''
        
        dirname = input("Choose a name for your project: ")
        return dirname.title()

    def create_project(self, dirname, name):
        '''create the actual project here (if it doesn't exist)'''

        try:
            os.mkdir(dirname)
            # before print, create 3 .json files here
            print(f"\"{name.title()}\" created successfully")
        except FileExistsError:
            print(f"ERROR: \"{name.title()}\" is already exist")
        except FileNotFoundError:
            print("ERROR: \"contents\" direcotry does not exist")