"""
Treasure Tables Data for random treasure generator.
This generator DOES NOT generate everything. Instead, it simply checks all of the percentages
on the initial treasure table. I always loved rolling up everything else, but hated checking
against all the base percentages. So this takes care of all of that, letting me do all the fun
deeper rolls myself.

In "Treasure as XP" systems, I simply tracks "gems" as a basic number, with each one being
worth 1d20 x 1d10 x 1d10 GP and XP at the end of a dungeon run.

Currently based on Dark Dungeons, compatible with BECMI.

"""

from random import randint as ri

import dice

dd_treasure = {
    'a': {
        'CP': {'chance': 25, 'val': ri(1000, 6000)},
        'SP': {'chance': 30, 'val': ri(1000, 6000)},
        'EP': {'chance': 20, 'val': ri(1000, 4000)},
        'GP': {'chance': 35, 'val': ri(1000, 6000) + ri(1000, 6000)},
        'PP': {'chance': 25, 'val': ri(1000, 2000)},
        'Gems': {'chance': 50, 'val': dice.roll(6, 6)},
        'Jewl': {'chance': 50, 'val': dice.roll(6, 6)},
        'Spec': {'chance': 10, 'val': ri(1, 2)},
        'Mag': {'chance': 30, 'val': 'any 3 magic items'},
    },
    'b': {
        'CP': {'chance': 50, 'val': ri(1000, 8000)},
        'SP': {'chance': 25, 'val': ri(1000, 6000)},
        'EP': {'chance': 25, 'val': ri(1000, 4000)},
        'GP': {'chance': 35, 'val': ri(1000, 3000)},
        'Gems': {'chance': 25, 'val': ri(1, 6)},
        'Jewl': {'chance': 25, 'val': ri(1, 6)},
        'Mag': {'chance': 10, 'val': '1 sword, weapon, or armor'},
    },
    'c': {
        'CP': {'chance': 20, 'val': ri(1000, 12000)},
        'SP': {'chance': 30, 'val': ri(1000, 4000)},
        'EP': {'chance': 10, 'val': ri(1000, 4000)},
        'Gems': {'chance': 25, 'val': ri(1, 4)},
        'Jewl': {'chance': 25, 'val': ri(1, 4)},
        'Spec': {'chance': 5, 'val': ri(1, 2)},
        'Mag': {'chance': 10, 'val': 'any 2 magic items'},
    },
    'd': {
        'CP': {'chance': 10, 'val': ri(1000, 8000)},
        'SP': {'chance': 15, 'val': ri(1000, 12000)},
        'GP': {'chance': 60, 'val': ri(1000, 6000)},
        'Gems': {'chance': 30, 'val': ri(1, 8)},
        'Jewl': {'chance': 30, 'val': ri(1, 8)},
        'Spec': {'chance': 10, 'val': ri(1, 2)},
        'Mag': {'chance': 15, 'val': 'any 2 magic items, 1 potion'},
    },
    'e': {
        'CP': {'chance': 5, 'val': ri(1000, 10000)},
        'SP': {'chance': 30, 'val': ri(1000, 12000)},
        'EP': {'chance': 25, 'val': ri(1000, 4000)},
        'GP': {'chance': 25, 'val': ri(1000, 8000)},
        'Gems': {'chance': 10, 'val': ri(1, 10)},
        'Jewl': {'chance': 10, 'val': ri(1, 10)},
        'Spec': {'chance': 15, 'val': ri(1, 2)},
        'Mag': {'chance': 25, 'val': 'any 3 magic items, 1 scroll'},
    },
    'f': {
        'SP': {'chance': 10, 'val': ri(1000, 10000) + ri(1000, 10000)},
        'EP': {'chance': 20, 'val': ri(1000, 8000)},
        'GP': {'chance': 45, 'val': ri(1000, 12000)},
        'PP': {'chance': 30, 'val': ri(1000, 3000)},
        'Gems': {'chance': 20, 'val': dice.roll(2, 6)},
        'Jewl': {'chance': 10, 'val': ri(1, 12)},
        'Spec': {'chance': 20, 'val': ri(1, 3)},
        'Mag': {'chance': 30, 'val': 'any 3 magic items but weapons, 1 scroll, 1 potion'},
    },
    'g': {
        'GP': {'chance': 50, 'val': ri(1000, 4000)},
        'PP': {'chance': 50, 'val': ri(1000, 6000)},
        'Gems': {'chance': 25, 'val': dice.roll(3, 6)},
        'Jewl': {'chance': 25, 'val': ri(1, 10)},
        'Spec': {'chance': 30, 'val': ri(1, 3)},
        'Mag': {'chance': 35, 'val': 'any 4 magic items, 1 scroll'},
    },
    'h': {
        'CP': {'chance': 25, 'val': dice.roll(3, 8) * 1000},
        'SP': {'chance': 50, 'val': ri(1000, 100000)},
        'EP': {'chance': 50, 'val': ri(1000, 4000)},
        'GP': {'chance': 50, 'val': ri(10000, 60000)},
        'PP': {'chance': 25, 'val': dice.roll(5, 4) * 1000},
        'Gems': {'chance': 50, 'val': ri(1, 100)},
        'Jewl': {'chance': 50, 'val': ri(10, 40)},
        'Spec': {'chance': 10, 'val': ri(1, 2)},
        'Mag': {'chance': 15, 'val': 'any 4 magic items, 1 potion, 1 scroll'},
    },
    'i': {
        'PP': {'chance': 30, 'val': ri(1000, 8000)},
        'Gems': {'chance': 50, 'val': dice.roll(2, 6)},
        'Jewl': {'chance': 5, 'val': dice.roll(2, 6)},
        'Spec': {'chance': 5, 'val': ri(1, 2)},
        'Mag': {'chance': 15, 'val': 'any 1 magic item'},
    },
    'j': {
        'CP': {'chance': 25, 'val': ri(1000, 4000)},
        'SP': {'chance': 10, 'val': ri(1000, 3000)},
    },
    'k': {
        'SP': {'chance': 30, 'val': ri(1000, 6000)},
        'EP': {'chance': 10, 'val': ri(1000, 2000)},
    },
    'l': {
        'GP': {'chance': 40, 'val': ri(1000, 4000) + ri(1000, 4000)},
        'PP': {'chance': 50, 'val': ri(1000, 10000) + ri(1000, 10000) + ri(1000, 10000)},
        'Gems': {'chance': 50, 'val': ri(1, 4)},
    },
    'm': {
        'Gems': {'chance': 55, 'val': dice.roll(5, 4)},
        'Jewl': {'chance': 45, 'val': dice.roll(2, 6)},
    },
    'n': {
        'Spec': {'chance': 10, 'val': ri(1, 2)},
        'Mag': {'chance': 40, 'val': str(dice.roll(2, 4)) + ' potions'},
    },
    'o': {
        'Spec': {'chance': 10, 'val': ri(1, 3)},
        'Mag': {'chance': 50, 'val': str(ri(1, 4)) + ' scrolls'},
    },
    'p': {
        'CP': {'chance': 100, 'val': dice.roll(3, 8)}
    },
    'q': {
        'SP': {'chance': 100, 'val': dice.roll(3, 6)},
    },
    'r': {
        'EP': {'chance': 100, 'val': dice.roll(2, 6)},
    },
    's': {
        'GP': {'chance': 100, 'val': dice.roll(2, 4)},
        'Gems': {'chance': 5, 'val': 1},
    },
    't': {
        'PP': {'chance': 100, 'val': ri(1, 6)},
        'Gems': {'chance': 5, 'val': 1},
    },
    'u': {
        'CP': {'chance': 10, 'val': ri(1, 100)},
        'SP': {'chance': 10, 'val': ri(1, 100)},
        'GP': {'chance': 5, 'val': ri(1, 100)},
        'Gems': {'chance': 5, 'val': ri(1, 2)},
        'Jewl': {'chance': 5, 'val': ri(1, 4)},
        'Spec': {'chance': 2, 'val': 1},
        'Mag': {'chance': 2, 'val': 'any 1 magic item'}
    },
    'v': {
        'SP': {'chance': 10, 'val': ri(1, 100)},
        'EP': {'chance': 5, 'val': ri(1, 100)},
        'GP': {'chance': 19, 'val': ri(1, 100)},
        'PP': {'chance': 5, 'val': ri(1, 100)},
        'Gems': {'chance': 10, 'val': ri(1, 2)},
        'Jewl': {'chance': 10, 'val': ri(1, 2)},
        'Spec': {'chance': 5, 'val': 1},
        'Mag': {'chance': 5, 'val': 'any 1 magic item'}
    }
}

# lair values, ascending based on DD listed avg values
lairs = ['j', 'l', 'k', 'c', 'b', 'e', 'd', 'i', 'f', 'a', 'g', 'm', 'h']

# individual values, ascending based on chances of magic loot
indiv = ['p', 'q', 'r', 's', 't', 'n', 'o', 'u', 'v']

# only tables with magic chances:
monly = ['n', 'o', 'u', 'v', 'c', 'b', 'e', 'd', 'i', 'f', 'a', 'g', 'm', 'h']


'''
SYSTEMS KEY:
dd      = "Dark Dungeons"
add1e   = "AD&D 1st Edition" 

Only current system implemented is Dark Dungeons. 1E is on the far back burner,
and since the Donjon already has a good one I may skip it entirely. Not sure if any
other systems have this kind of random treasure generation, but I'm leaving the
code in place just in case.

Also, I kinda sorta REALLY want to incorporate rolls against the entire combined
AD&D 2E Encyclopedia Magica... 
'''

systems = {
    'dd': dd_treasure,
}


# needs alpha category, game system, and number of rolls against the table
def get_treasure(category, system='dd', quantity=1):
    loot_set = systems[system]
    check_set = loot_set[category]
    # let's go down the line now...
    my_treasure = []
    if 'CP' in check_set:
        my_cps = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['CP']['chance']:
                my_cps += check_set['CP']['val']
        if my_cps > 0:
            my_treasure.append('Copper Pieces: ' + str(my_cps))
    if 'SP' in check_set:
        my_sps = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['SP']['chance']:
                my_sps += check_set['SP']['val']
        if my_sps > 0:
            my_treasure.append('Silver Pieces: ' + str(my_sps))
    if 'EP' in check_set:
        my_eps = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['EP']['chance']:
                my_eps += check_set['EP']['val']
        if my_eps > 0:
            my_treasure.append('Electrum Pieces: ' + str(my_eps))
    if 'GP' in check_set:
        my_gps = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['GP']['chance']:
                my_gps += check_set['GP']['val']
        if my_gps > 0:
            my_treasure.append('Gold Pieces: ' + str(my_gps))
    if 'PP' in check_set:
        my_pps = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['PP']['chance']:
                my_pps += check_set['PP']['val']
        if my_pps > 0:
            my_treasure.append('Platinum Pieces: ' + str(my_pps))
    if 'Gems' in check_set:
        my_gems = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['Gems']['chance']:
                my_gems += check_set['Gems']['val']
        if my_gems > 0:
            my_treasure.append('Gems: ' + str(my_gems))
    if 'Jewl' in check_set:
        my_jewls = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['Jewl']['chance']:
                my_jewls += check_set['Jewl']['val']
        if my_jewls > 0:
            my_treasure.append('Pieces of Jewellery: ' + str(my_jewls))
    if 'Spec' in check_set:
        my_specs = 0
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['Spec']['chance']:
                my_specs += check_set['Spec']['val']
        if my_specs > 0:
            my_treasure.append('Platinum Pieces: ' + str(my_specs))
    if 'Mag' in check_set:
        # my_mags = []
        for x in range(0, quantity):
            check_val = ri(1, 100)
            if check_val <= check_set['Mag']['chance']:
                my_treasure.append(str('Magic Items: ' + str(check_set['Mag']['val'])))
    return my_treasure


if __name__ == "__main__":
    sys = 'dd'  # will convert to input later
    table = input("Which sub-table are you rolling against? Valid input is single-letter A-V: ")
    rolls = int(input("How many rolls against that table do you need to make? Enter a number 1 or greater: "))
    treasure = get_treasure(table, sys, rolls)
    for item in treasure:
        print(item)
