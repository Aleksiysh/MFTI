#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    pass
    move_right()
    while True:
        if not wall_is_above():
            colored_return()
        if wall_is_on_the_right():
            break
        else:
            move_right()
    while wall_is_beneath():
        move_left()        

def colored_return():
    while True:
        move_up()
        fill_cell()
        if wall_is_above():
            break
          
    while not wall_is_beneath():
        move_down()                      


if __name__ == '__main__':
    run_tasks()
