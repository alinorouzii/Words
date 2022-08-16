'''
    This file will handle deletion of 1 or more projects (even all at once)
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 9:30 PM, August 16, 2022
    Updated: Created _del_all_projects()
             Created _del_some_projects()
'''

import os

# import my .py modules
import common


class DeleteProject:
    '''Delete one or more (even all) projects'''


    def __init__(self) -> None:
        self.projects = common.list_projects()

    # get numbers of all projects we want to delete
    # or get "all" to delete all projects at once


    def _confirm_input(self, inp_list) -> bool:
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


    def _get_projects(self) -> list:
        '''
            get a list of projects (as string) from the user
            return a list of splitted the string
        '''

        print("\nEnter numbers for each project (such as: 2 8 12),")
        print("Or enter \"all\" to delete all projects at once")
        print("NOTE: deleted projects cannot be reversed")
        selected = input("Enter numbers or \"all\": ")

        return selected.split()


    def _del_all_projects(self):
        '''delete all projects at once'''
        
        pass


    def _del_some_projects(self):
        '''delete selected projects'''

        pass


    def del_projects(self) -> bool:
        '''this method will run deleting projects'''

        # when there is no project
        if not self.projects:
            print("\nNo project exists")
            return False

        # print all projects
        common.print_projects(self.projects)

        # input projects to delete (as a list)
        inp_projects = self._get_projects()
        ret_confirm  = self._confirm_input(inp_projects)

        # error handling
        if ret_confirm == 0:
            print("ERROR: wrong input")
            return False