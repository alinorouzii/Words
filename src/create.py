'''
    This file will handle all orders for creating a project
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 7:42 PM, August 16, 2022
    Updated: Added dirname as the CreateFiles class input
             Added "contents/{dirname}" to .json files 
'''

import json
import os
import datetime as dt
import shutil

# import my .py module
import common


class CreateFiles:
    '''this class will create all files for a new project'''

    def __init__(self, dirname):
        self.dirname = dirname

    def _get_interval(self):
        '''get interval from the user to use them into create_settings()'''

        print("\nHow many days should there be a break between each exercise?")
        print("Enter a number equal or greater than 1")

        try:
            interval = int(input("Enter a number: "))
        except ValueError:
            print("\nERROR: You should enter an interger greater than or equal to 1")
            return False

        return interval

    
    def create_settings(self):
        '''
            create settings.json file
            settings.json will contain:
                - the name of the project
                - creation date and time
                - last practiced date and time
                - next practice date and time
                - interval: 'n' next days for practicing
                - limit: maximum days to practice each word
                - total: total practiced days
        '''

        curr_date = dt.datetime.now()
        interval  = self._get_interval()

        # error handling: if interval was wrong and returned False
        if not interval:
            return False

        settings = {
            'projecdt name' : self.dirname,
            'created at'    : str(curr_date),
            'last practice' : str(curr_date),
            'interval'      : interval,  # interval is inter for days
            'next practice' : str(curr_date + dt.timedelta(days=interval))
        }

        try: 
            with open(f"contents/{self.dirname}/settings.json", 'w') as json_file:
                json.dump(settings, json_file)
        except OSError:
            return False                     # if creating was failed

        return True                          # if creating was successful

    def create_words(self):
        '''create words.json to store words inside it'''

        try:
            with open(f"contents/{self.dirname}/words.json", 'w') as json_file:
                json.dump(dict(), json_file)
        except OSError:
            return False                     # if creating was failed

        return True                          # if creating was successful

    def create_wrongs(self):
        '''
            create wrongs.json to store wrong answers
            this file contains:
                - original (wrong answered) word as the key
                - {
                    "iteration" : number of answered wrong,
                    "last wrong": date-time of last answered wrong
                  }
            but for now, this method created an empty dictionary
        '''

        try:
            with open(f"contents/{self.dirname}/wrongs.json", 'w') as json_file:
                json.dump(dict(), json_file)
        except OSError:
            return False                     # if creating was failed

        return True                          # if creating was successful


class CreateProject:
    '''this class will create a new project(directory)'''

    def get_dirname(self):
        '''get the directory name of a new project and return it'''
        
        dirname = input("Choose a name for your project: ")
        return dirname.title()

    def create_project(self, dirname):
        '''create the actual project here (if it doesn't exist)'''

        try:
            # create a directory for the new project
            os.mkdir(f"contents/{dirname}")

            # create 3 .json files
            create_files = CreateFiles(dirname)
            ret_settings = create_files.create_settings()
            ret_words    = create_files.create_words()
            ret_wrongs   = create_files.create_wrongs()

            # error handling: if creating of each of these 3 files failed
            # it must delete the project direcotry before return False
            if not (ret_settings and ret_words and ret_wrongs):
                print(f"ERROR: Creating \"{dirname.title()}\" failed")
                shutil.rmtree(dirname)
                return False

            # print successful creation message
            print(f"\n\"{dirname.title()}\" created successfully")
        except FileExistsError:
            print(f"\nERROR: \"{dirname.title()}\" is already exist")
            return False
        except FileNotFoundError:
            print("\nERROR: \"contents\" direcotry does not exist")
            return False

        return True


def run():
    '''run create.py from here'''

    new_project    = CreateProject()
    dirname        = new_project.get_dirname()
    create_project = new_project.create_project(dirname)

    return create_project       # True if project created successfully