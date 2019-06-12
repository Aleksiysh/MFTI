#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    N = 0
    while True:
        if cell_is_filled():
            N+=1
        if N==5:
            break
        else:    
            move_right()  
        
                   

if __name__ == '__main__':
    run_tasks()
