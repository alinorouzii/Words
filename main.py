'''
    This is the main source code that will execute other 
    .py files. It manages the entire program.

    NOTE: it will create "contents" directory each time this
    file executes, if that directory doesn't exist.
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 4:26 PM, August 16, 2022
    Added: import modules
           __name__ condition
'''

import os
import sys

# import my .py modules
sys.path.append("/src")
import common
import create
import delete
import run
import update


if __name__ == '__main__':
    pass