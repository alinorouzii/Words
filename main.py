'''
    This is the main source code that will execute other 
    .py files. It manages the entire program.

    NOTE: it will create "contents" directory each time this
    file executes, if that directory doesn't exist.
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 7:21 PM, August 16, 2022
    Updated: get_option()
             Added create new project codes to it
'''

import os
import sys

# import my .py modules
sys.path.append("src/")
import common
import create
import delete
import run
import update


def setup_contents():
    '''set up contents directory if it doesn't exist'''

    path = "contents"
    if not os.path.exists(path):
        os.mkdir(path)


def msg_options():
    '''print which options do the program have'''

    print("\t(1) Create a new project")
    print("\t(2) Work with an existing project")
    print("\t(3) Delete projects")

def get_option():
    '''get an option from the use and run the corresponding method'''

    print()
    option = int(input("Enter a number: "))

    try:
        if option == 1:
            ret_create_n = create.run()
            if ret_create_n:
                print("New project created successfully")
            else:
                print("Creating new project failed")
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            print("ERROR: input must be 1, 2, or 3")
            return False
    except:
        print("ERROR: wrong input")
        return False


if __name__ == '__main__':
    setup_contents()
    msg_options()
    get_option()