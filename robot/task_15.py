#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    pass
    if wall_is_on_the_left() and wall_is_above():
        move_to_wall_right()
        move_to_wall_down() 
    elif wall_is_above() and wall_is_on_the_right():
        move_to_wall_down()
        move_to_wall_left()
    elif wall_is_on_the_right() and wall_is_beneath():
        move_to_wall_left()
        move_to_wall_up()
    elif wall_is_beneath() and wall_is_on_the_left():
        move_to_wall_up()
        move_to_wall_right()                         
    else:
        exit(-1)

def move_to_wall_up():
    while not wall_is_above():
        move_up()

def move_to_wall_right():
    while not wall_is_on_the_right():
        move_right()  

def move_to_wall_down():
    while not wall_is_beneath():
        move_down()  

def move_to_wall_left():
    while not wall_is_on_the_left():
        move_left()                    

if __name__ == '__main__':
    run_tasks()
