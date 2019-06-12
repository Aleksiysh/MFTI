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

@task(delay=0.02)
def task_2_4():
    for j in range(4):
        for i in range(9):
            cross()
            move_right(4)
        cross()
        while not wall_is_on_the_left():
            move_left()
        move_down(4)  

    for i in range(9):
            cross()
            move_right(4)
    cross()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
