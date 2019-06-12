#!/usr/bin/python3

from pyrob.api import *
def cross():
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    move_up()

@task
def task_2_2():
    move_down()
    for i in range(5):
        cross()
        for j in range(4):
            if wall_is_on_the_right():
                move_left(2)
                break
            else:    
                move_right()


if __name__ == '__main__':
    run_tasks()
