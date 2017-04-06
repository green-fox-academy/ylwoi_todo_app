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
                task_list = ListTasks()
            if command[0] == '-a':
                print('-a')
            if command[0] == '-r':
                print('-r')
            if command[0] == '-c':
                print('-c')

    def reader(self):
        self.db_file = open('DB.txt', 'r')
        db_list = self.db_file.readlines()
        db_list = [i.replace('\n', '') for i in db_list]
        db_list = [i.split('\t')for i in db_list]
        return db_list


class ListTasks(ArgumentReader):
    def __init__(self):
        self.db_list = self.reader()
        if len(self.db_list) == 0:
            print('No todos for today! :)')
        else:
            for i in range(len(self.db_list)):
                if self.db_list[i][0] == '0':
                    self.db_list[i][0] = '[ ]'
                if self.db_list[i][0] == '1':
                    self.db_list[i][0] = '[x]'
                print(i+1, ' - ', self.db_list[i][0], self.db_list[i][1])
example = ArgumentReader()





