#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_9_3():
    N = 1
    while not wall_is_on_the_right():
        N += 1
        move_right()
    move_left(N-1)

    for i in range(N):
        for j in range(N):
            if  not (i== j or i+j == N-1):
                fill_cell()
            if not wall_is_on_the_right():    
                move_right()
        move_left(N-1)    
        if not wall_is_beneath():
             move_down()


if __name__ == '__main__':
    run_tasks()
