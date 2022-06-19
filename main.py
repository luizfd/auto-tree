import pyautogui as pt
from time import sleep


def locate_tree():  # ideal fov: 82
    position = pt.locateCenterOnScreen('images/tree.png', confidence=.5)

    if position is None:
        print("tree no found :(")
        return False
    else:
        print("tree found!!!")
        return True


def move(key, duration):
    pt.keyDown(key)

    sleep(duration)
    pt.keyUp(key)


def attack(duration):
    pt.mouseDown()
    sleep(duration)
    pt.mouseUp()


loop_duration = 2

sleep(3)

# ideal fov: 82

while loop_duration != 0:
    sleep(5)

    # logging stuff
    print("MOUSE POS: ", pt.position())

    # no clue why it needs to be done this way
    # pt.moveRel(164.5, 0, duration=1)  # in game sensitivity = 50%; raw input OFF; 800dpi


    if locate_tree():

        move('w', 3.5)  # moves forward 5 blocks

        # axe: 1st slot; shears/hoe: 2nd slot
        pt.keyDown('2')
        pt.keyUp('2')

        attack(0.11)  # breaks leaves
        attack(0.11)

        pt.keyDown('1')
        pt.keyUp('1')

        move('w', 1.5)  # moves closer to the tree

        # diamond axe: 0.41s; iron axe: 0.51s; stone axe: 0.76s; hands: 3.1s (approx)
        attack(0.41)
        pt.moveRel(0, 250, duration=.5)
        attack(0.41)
        pt.moveRel(0, -250, duration=.5)
        move('w', 0.1)
        pt.moveRel(0, -1000, duration=.5)



    loop_duration -= 1

