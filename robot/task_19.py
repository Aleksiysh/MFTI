#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    pass
    while not wall_is_on_the_left():
        move_left()
    while True:
        if not wall_is_above():
            go_to_end()
            break
        
        elif not wall_is_on_the_right():    
            move_right()
        elif wall_is_on_the_right():
            break  

def  go_to_end():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()  


if __name__ == '__main__':
    run_tasks()
