#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n=N=0
    move_right()

    while True:
        
        if n==N:
            fill_cell()
            n=0
            N+=1
        if wall_is_on_the_right():
            break
        else:    
            move_right()
            n+=1    

if __name__ == '__main__':
    run_tasks()
