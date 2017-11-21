'''
DnD Variant Gear Generator

This is my own custom gear generator built on the premise of tying starting gear choices not to
any random gold rolls, but instead to the average of a character's starting stats. The lower their
stats average, the better gear they will have, and vice-versa.

All weapons are marked with WEAPON: at the beginning
All armours are marked with ARMOUR: at the beginning
I'm considering doing the same for MAGIC: but haven't added it yet
these tags will be used to pull them from the gear dump and separate into their own categories
'''


import random
from random import choice as ch

import dice


def get_gear(classname, prefs, avg):
    return


'''
# how to remove empty items from a list
newtestlist = list(filter(None, testlist))
'''


if __name__ == "__main__":
    get_gear()
