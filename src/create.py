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

    def get_name(self):
        '''get the name of a new project and return it'''
        
        name = input("Choose a name for your project: ")
        return name

    def project_exist(self, path):
        '''
            handle an existing project
            print a message and return True if exists
        '''

        if os.path.exists(path):
            print("ERROR: project is already exist")
            return True

        return False

    # create settings.json, wrong.json, words.json