'''
    This file will handle deletion of 1 or more projects (even all at once)
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 10:25 PM, August 16, 2022
    Updated: Added len_project variable and change 'int(element) > len_input'
'''

import os
import shutil

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

        len_input   = len(inp_list)
        len_project = len(self.projects)

        if len_input == 1 and inp_list[0] == "all":
            return True
        # if the list is empty -- return False
        elif len_input == 0:
            return False

        for element in inp_list:
            # if each element in the list contains non-digit character or isn't x >= 1
            if not (element.isdigit() and int(element) >= 1):
                return False
            elif int(element) > len_project:
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
        selected = input("\nEnter numbers or \"all\": ")

        return selected.split()


    def _del_all_projects(self):
        '''delete all projects at once'''
        
        for project in self.projects:
            shutil.rmtree(f"contents/{project}")


    def _del_some_projects(self, inp_projects):
        '''delete selected projects'''

        for n in inp_projects:  # each inputed project is actually a number started at 1
            dirname = self.projects[int(n) - 1]
            shutil.rmtree(f"contents/{dirname}")


    def del_projects(self) -> bool:
        '''this method will run deleting projects'''

        # print all projects if they exist
        # otherwise print something else and return False
        if not common.print_projects(self.projects):
            return False

        # input projects to delete (as a list)
        inp_projects = self._get_projects()
        ret_confirm  = self._confirm_input(inp_projects)

        # error handling
        if ret_confirm == 0:
            print("\nERROR: wrong input")
            return False

        # delete projects here
        if inp_projects[0] == "all":
            self._del_all_projects()
        else:
            self._del_some_projects(inp_projects)

        return True


def run():
    '''run delete operations from here'''

    del_projects = DeleteProject()
    ret_del = del_projects.del_projects()

    return ret_del