#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while True:
        if not wall_is_above():
            # or wall_is_beneath():
            fill_up()
        if not wall_is_beneath():
            fill_down()    
        if wall_is_on_the_right():
            return
        else:
             move_right()

def fill_up():
    move_up()
    fill_cell()
    move_down()

def fill_down():
    move_down()
    fill_cell()
    move_up()

if __name__ == '__main__':
    run_tasks()
