import pyautogui as pt
from time import sleep


def locate_tree():  # ideal fov: 82
    position = pt.locateOnScreen('images/tree.png', confidence=.2)
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
    sleep(.1)


loop_duration = 4

sleep(3)

# ideal fov: 82

while loop_duration != 0:
    sleep(5)

    # logging stuff
    print("MOUSE POS: ", pt.position())

    # no clue why it needs to be done this way
    pt.moveRel(164.5, 0, duration=1)  # in game sensitivity = 50%; raw input OFF; 800dpi

    if locate_tree():

        move('w', 1.5)  # moves forward 5 blocks

        # axe: 1st slot; shears/hoe: 2nd slot; saplings: 3rd slot
        pt.keyDown('2')
        pt.keyUp('2')

        attack(0.15)  # breaks leaves
        attack(0.15)

        pt.keyDown('1')
        pt.keyUp('1')

        move('w', .6)  # moves closer to the tree

        # diamond axe: 0.5s;  hands: 3.2s (approx)
        attack(0.5)
        pt.moveRel(0, 250, duration=.5)
        attack(0.5)
        pt.moveRel(0, -250, duration=.5)
        move('w', 0.1)
        pt.moveRel(0, -1000, duration=.5)
        attack(0.5)
        attack(0.5)
        attack(0.5)
        attack(0.5 + 0.1)  # TODO: DRY lol im going insane
        pt.keyDown('3')
        pt.moveRel(0, 1000, duration=.5)
        pt.click(button='right')
        pt.moveRel(0, -295, duration=.5)
        move('s', 1.39)

    loop_duration -= 1

