#!/usr/bin/python3

from pyrob.api import *
#from move_to_wall import *

@task
def task_8_22():
    move_to_wall_up()
    if not wall_is_on_the_left():
        move_to_wall_left()
    else:
         move_to_wall_right()  

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
