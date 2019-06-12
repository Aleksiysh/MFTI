#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_8_30():
    while True:
        while not wall_is_on_the_right():
            move_right()
        while wall_is_beneath():
            if not wall_is_on_the_left():
                move_left()
            else:
                return    

        while not wall_is_beneath():
            move_down()
          



if __name__ == '__main__':
    run_tasks()
