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


dd_gear = {
    'tier': {
      'cleric': [],
      'dwarf': [],
      'elf': [],
      'fighter': [],
      'halfling': [],
      'mu': [],
      'mystic': [],
      'thief': [],
      'fighter': [],
    },
}


def get_tier(avg):
    if avg == 18:
        tier = 'fuckall'
    elif avg >= 16:
        tier = 'shitty'
    elif avg >= 13:
        tier = 'weaksauce'
    elif avg >= 9:
        tier = 'common'
    elif avg >= 6:
        tier = 'decent'
    elif avg >= 4:
        tier = 'whoah'
    else:
        tier = 'holyfuckingshit'
    return tier


def get_gear(classname, prefs, avg):
    # test:
    gear_tier = get_tier(avg)
    gearList = ['this is A TEST', 'this is ONLY A TEST', '']
    gearList = list(filter(None, gearList))
    return sorted(gearList)


if __name__ == "__main__":
    get_gear()
