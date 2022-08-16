'''
    This file will handle deletion of 1 or more projects (even all at once)
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 8:52 PM, August 16, 2022
    Updated: Created confirm_input()
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

    def confirm_input(self, inp_list) -> Boolean:
        '''confirm if list of numbers is all numbers or just "all"'''

        len_input = len(inp_list)

        if len_input == 1 and inp_list[0] == "all":
            return True
        # if the list is empty -- return False
        elif len_input == 0:
            return False

        for element in inp_list:
            # if each element in the list contains non-digit character -- return False
            if not element.isdigit():
                return False

        return True


    def del_projects(self):
        '''this method will run deleting projects'''

        # when there is no project
        if not self.projects:
            print("\nNo project exists")
            return False

        # print all projects
        common.print_projects(self.projects)

        # input projects to delete (as a list)
        print("\nEnter numbers for each project (such as: 2 8 12),")
        print("Or enter \"all\" to delete all projects at once")
        print("NOTE: deleted projects cannot be reversed")
        selected = input("Enter numbers or \"all\": ")