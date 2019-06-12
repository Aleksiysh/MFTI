#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    n=0
    
    while not wall_is_on_the_right():
        if wall_is_above():
            if cell_is_filled():
                n+=1
            fill_cell()
        else:
            n+=colored_return() 
        move_right()   
    

    mov(ax,n) 
    print (n)       



def colored_return():
    m = 0
    while True:
        move_up()
        if cell_is_filled():
            m+=1
        fill_cell()
        if wall_is_above():
            break
          
    while not wall_is_beneath():
        move_down()

    return m           


if __name__ == '__main__':
    run_tasks()
