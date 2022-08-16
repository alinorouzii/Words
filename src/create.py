'''
    This file will handle all orders for creating a project
'''

'''
    Creator: Ali Norouzi
    Last modified: Tue 6:30 PM, August 16, 2022
    Updated: removed an unwanted import
'''

import json
import os
import datetime as dt

# import my .py module
import common


class CreateFiles:
    '''this class will create all files for a new project'''

    def get_interval(self):
        '''get interval from the user to use them into create_settings()'''

        print("\nHow many days should there be a break between each exercise?")
        print("Enter a number equal or greater than 1")

        try:
            interval = int(input("Enter a number: "))
        except ValueError:
            print("\nERROR: You should enter an interger greater than or equal to 1")
            return False

        return interval

    
    def create_settings(self, dirname, interval=1):
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

        settings = {
            'name'          : self.dirname,
            'created at'    : curr_date,
            'last practice' : curr_date,
            'interval'      : interval,       # interval is in day(s)
            'next practice' : curr_date + dt.timedelta(days=interval)
        }

        try: 
            with open("settings.json", 'w') as json_file:
                json.dump(settings, json_file)
        except OSError:
            return False                     # if creating was failed

        return True                          # if creating was successful

    def create_words(self):
        '''create words.json to store words inside it'''

        try:
            with open("words.json", 'w') as json_file:
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
            with open("wrongs.json", 'w') as json_file:
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

    def create_project(self, dirname, name):
        '''create the actual project here (if it doesn't exist)'''

        try:
            os.mkdir(dirname)
            # before print, create 3 .json files here
            # delete this directory if creating .json files fail
            print(f"\n\"{name.title()}\" created successfully")
        except FileExistsError:
            print(f"\nERROR: \"{name.title()}\" is already exist")
        except FileNotFoundError:
            print("\nERROR: \"contents\" direcotry does not exist")