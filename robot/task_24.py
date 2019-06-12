#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    
    pass
    move_down(2)
    move_right()
    cross()

def cross():
    
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


if __name__ == '__main__':
    run_tasks()
