__author__ = 'ylwoi'

import sys


class ArgumentReader():
    def __init__(self):
        self.args = sys.argv
        if len(self.args) == 1:
            print("Python Todo application \n======================= \n \nCommand line arguments: \n-l   Lists all the tasks \n-a   Adds a new task \n-r   Removes an task \n-c   Completes an task ")
        else:
            command = self.args[1:]
            if command[0] == '-l':
                print("-l")
            if command[0] == '-a':
                print('-a')
            if command[0] == '-r':
                print('-r')
            if command[0] == '-c':
                print('-c')

example = ArgumentReader()





