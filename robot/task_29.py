#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    N = 0
    while not wall_is_on_the_right() and N!=2:
        if cell_is_filled():
            N+=1
        move_right()
        if not cell_is_filled():
            N=0    


    


if __name__ == '__main__':
    run_tasks()
