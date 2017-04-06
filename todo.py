__author__ = 'ylwoi'

import sys


class ArgumentReader():
    def __init__(self):
        self.args = sys.argv
        if len(self.args) == 1:
            self.print_info()

    def print_info(self):
        print("Python Todo application \n======================= \n \nCommand line arguments: \n-l   Lists all the tasks \n-a   Adds a new task \n-r   Removes an task \n-c   Completes an task ")

example = ArgumentReader()





