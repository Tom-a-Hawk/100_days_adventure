from time import sleep
import itertools
import random

colors = 'Red Green Yellow'.split()
rotation = itertools.cycle(colors)


def rg_time():
    return random.randint(3,7)


def light_rotation(rotation):
    for color in rotation:
        if color == 'Yellow':
            print('Caution! The light is %s' %color)
            sleep(3) #seconds
        elif color == 'Red':
            print('Stop! The light is %s' %color)
            sleep(rg_time()) #seconds
        else:
            print('Go! The light is %s' %color)
            sleep(rg_time())



if __name__ ==  '__main__':
    light_rotation(rotation)
