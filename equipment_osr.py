"""
DnD Variant Gear Generator

This is my own custom gear generator built on the premise of tying starting gear choices not to
any random gold rolls, but instead to the average of a character's starting stats. The lower their
stats average, the better gear they will have, and vice-versa.

All weapons are marked with WEAPON: at the beginning
All armours are marked with ARMOUR: at the beginning
I'm considering doing the same for MAGIC: but haven't added it yet
these tags will be used to pull them from the gear dump and separate into their own categories
"""


import random
from random import choice as ch

import dice
from dice import roll as die


# 22 items
basics = [
    'Backpack', 'Bedroll', 'Belt Purse', 'Chalk (10 pcs)', 'Cloak', 'Crowbar', 'Firewood (3 units)',
    'Flask', 'Lantern (hooded) w/ 2 flasks of oil', 'Mug or Tankard', 'Rain Hat',
    'Rations (7 units iron)', 'Rations (7 units standard)', 'Rope (50 ft)', 'Sack, Small',
    'Sack, Large', 'Sewing Kit', 'Tent', 'Tinder Box', 'Torches x5', 'Waterskin', 'Whetstone',
]

# 38 items
advanced = [
    'Acid (1 flask)', 'Alchemist Fire (1 flask)', 'Antitoxin (1 vial)', 'Bell (tiny)',
    'Belladona', 'Blanket (winter)', 'Block and Tackle', 'Caltrobs (2-pound bag)',
    'Candles x10', 'Case (for map or scroll)', 'Chain (10 ft)', 'Chest', 'Cooking Pot (iron)',
    'Fishing Net (25 sq ft)', 'Fishing Hook, Line, and Pole', 'Garlic', 'Grappling Hook',
    'Hammer (small)', 'Holy Symbol', 'Holy Water (small vial)', 'Ink pot, quill, and paper',
    'Iron Spike', 'Lantern (bullseye) w/ 2 flasks of oil', 'Mallet and Stakes (3)',
    'Manacles', 'Mirror (steel)', 'Notebook (small)', 'Pole (10 ft)', 'Sealing Wax',
    'Signal Whistle', 'Silver cross', 'Silver mirror', 'Soap (1 pound)', 'Spyglass',
    'Steel mirror', 'Wine (1 qt.)', 'Wolvesbane', 'Wooden cross',
]

armour = [
    'ARMOUR: Plate Armour (AC+8)',
    'ARMOUR: Plate Mail (AC+7)',
    'ARMOUR: Splint Mail (AC+6)',
    'ARMOUR: Chain Mail (AC+5)',
    'ARMOUR: Scale Mail (AC+4)',
    'ARMOUR: Studded Leather (AC+3)',
    'ARMOUR: Leather Armour (AC+2)',
    'ARMOUR: Padded Armour (AC+1)',
]

weapons_war = [
    'WEAPON: Axe, Battle (2H, 1d8)',
    'WEAPON: Axe, Hand (1H, 1d6)',
    'WEAPON: Blackjack (1H, 1d2 special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R, special)',
    'WEAPON: Bola (R, 1d2 special)',
    'WEAPON: Bow, Long w/ 20 Arrows (R, 1d6)',
    'WEAPON: Bow, Short w/ 20 Arrows (R, 1d6)',
    'WEAPON: Cestus (1H, 1d3)',
    'WEAPON: Club (1H, 1d4)',
    'WEAPON: Crossbow, Heavy w/ 30 Bolts (R, 2d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R, 1d6)',
    'WEAPON: Dagger (1H, 1d4)',
    'WEAPON: Halberd (2H, 1d10)',
    'WEAPON: Hammer, Throwing (R, 1d4)',
    'WEAPON: Hammer, War (R, 1d6)',
    'WEAPON: Javelin (1H, 1d6)',
    'WEAPON: Lance (1H, 1d10)',
    'WEAPON: Mace (1H, 1d6)',
    'WEAPON: Net (1H, special)',
    'WEAPON: Pike (2H, 1d10)',
    'WEAPON: Poleaxe (2H, 1d10)',
    'WEAPON: Shield, Horned (1H, 1d2)',
    'WEAPON: Shield, Knife (1H, 1d4+1)',
    'WEAPON: Shield, Sword (1H, 1d4+2)',
    'WEAPON: Shield, Tusked (1H, 1d4+1)',
    'WEAPON: Sling w/ 30 Pellets (R, 1d4)',
    'WEAPON: Spear (1H, 1d6)',
    'WEAPON: Staff (2H, 1d6)',
    'WEAPON: Sword, Bastard (1H: 1d6+1, 2H: 1d8+1)',
    'WEAPON: Sword, Normal (1H, 1d8)',
    'WEAPON: Sword, Short (1H, 1d6)',
    'WEAPON: Sword, Two-Handed (2H, 1d10)',
    'WEAPON: Trident (1H, 1d6)',
    'WEAPON: Whip (1H, 1d2 special)',
]

weapons_rog = [
    'WEAPON: Blackjack (1H, 1d2 special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R, special)',
    'WEAPON: Bola (R, 1d2 special)',
    'WEAPON: Bow, Short w/ 20 Arrows (R, 1d6)',
    'WEAPON: Club (1H, 1d4)',
    'WEAPON: Crossbow, Heavy w/ 30 Bolts (R, 2d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R, 1d6)',
    'WEAPON: Dagger (1H, 1d4)',
    'WEAPON: Javelin (1H, 1d6)',
    'WEAPON: Mace (1H, 1d6)',
    'WEAPON: Sling w/ 30 Pellets (R, 1d4)',
    'WEAPON: Spear (1H, 1d6)',
    'WEAPON: Sword, Short (1H, 1d6)',
    'WEAPON: Whip (1H, 1d2 special)',
]

weapons_mag = [
    'WEAPON: Club (1H, 1d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R, 1d6)',
    'WEAPON: Dagger (1H, 1d4)',
    'WEAPON: Sling w/ 30 Pellets (R, 1d4)',
    'WEAPON: Staff (2H, 1d6)',
    'WEAPON: Sword, Short (1H, 1d6)',
]

weapons_clr = [
    'WEAPON: Blackjack (1H, 1d2 special)',
    'WEAPON: Bola (R, 1d2 special)',
    'WEAPON: Cestus (1H, 1d3)',
    'WEAPON: Club (1H, 1d4)',
    'WEAPON: Hammer, Throwing (R, 1d4)',
    'WEAPON: Hammer, War (R, 1d6)',
    'WEAPON: Mace (1H, 1d6)',
    'WEAPON: Net (1H, special)',
    'WEAPON: Sling w/ 30 Pellets (R, 1d4)',
    'WEAPON: Staff (2H, 1d6)',
    'WEAPON: Whip (1H, 1d2 special)',
]

weapons_hlf = [
    'WEAPON: Axe, Hand (1H, 1d6)',
    'WEAPON: Blackjack (1H, 1d2 special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R, special)',
    'WEAPON: Bola (R, 1d2 special)',
    'WEAPON: Bow, Short w/ 20 Arrows (R, 1d6)',
    'WEAPON: Cestus (1H, 1d3)',
    'WEAPON: Club (1H, 1d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R, 1d6)',
    'WEAPON: Dagger (1H, 1d4)',
    'WEAPON: Hammer, Throwing (R, 1d4)',
    'WEAPON: Hammer, War (R, 1d6)',
    'WEAPON: Mace (1H, 1d6)',
    'WEAPON: Net (1H, special)',
    'WEAPON: Shield, Horned (1H, 1d2)',
    'WEAPON: Shield, Knife (1H, 1d4+1)',
    'WEAPON: Shield, Sword (1H, 1d4+2)',
    'WEAPON: Shield, Tusked (1H, 1d4+1)',
    'WEAPON: Sling w/ 30 Pellets (R, 1d4)',
    'WEAPON: Spear (1H, 1d6)',
    'WEAPON: Staff (2H, 1d6)',
    'WEAPON: Sword, Short (1H, 1d6)',
    'WEAPON: Whip (1H, 1d2 special)',
]

miscellany = [
    'Crippling apathy', 'Twitchy eyes', 'a Certain "je ne sais quoi"', 'a love of horrible puns',
    'a feeling of general loathing for everyone around you', 'a case of the wiggles', 'wanderlust in your heart',
    'an independent streak', 'the first love letter anyone every wrote you', 'a sack full of bandit ears',
    'a regrettable haircut', 'chronic silent but deadly gas', 'curious pocket lint', 'inappropriate laughing',
    'a first edition manuscript of "Winter\'s Sullen Cry"', 'all of your nail clippings, ever',
    'an irritable tabby cat', 'a map to an island that doesn\'t exist', 'a pure white badger pelt',
    'pornographic goblin trading cards', 'a single strip of slightly used sandpaper', 'a petrified dragon egg',
    'a lock of hair from your mother or father', 'a fake beard', 'rusted nipple clamps', "two weird puppets",
    str(die(2, 3)) + ' commemorative plates', 'a bottle of freshly-harvested llama milk',
    'a free drink coupon for the Inn, but it expires soon...', 'a tendency to insert yourself into conversations',
    'unsettling memories from last night', 'a strong distrust for the government', 'an unsettlingly sexy facial scar',
]


basic_gear = {
    'fuckall': {
        'weapons': {
            'clr': ['WEAPON: a large brass candlestick, grabbed as you ran disgraced from your temple (Melee: 1d4)'],
            'hlf': ['WEAPON: a large heavy rock, which smells terrible (Melee: 1d4)'],
            'mag': ['WEAPON: Your gnarled fingernails which clawed your master\'s eyes from his skull (Melee: 1d4)'],
            'rog': ['WEAPON: a bone shiv which you used to escape from prison (Melee: 1d4)'],
            'war': ['WEAPON: a recently-detached human leg, usable as a club (Melee: 1d4)'],
        },
        'armour': {
            'mag': ['blood-covered robes'],
            'rog': ['a set of ragged prison clothes'],
            'war': ['ARMOUR: a Shield made from the lid of a rubbish bin (AC+1)'],
        },
        'basics': ['a half-eaten turkey leg from the festival you just left'],
        'advanced': ['the bloody tooth of someone - or something - recently deprived of its favorite tooth'],
        'money': [str(die(1, 6)) + ' copper coins'],
        'misc': [],
    },
    'weaksauce': {
        'weapons': {
            'clr': [],
            'hlf': [],
            'mag': [],
            'rog': [],
            'war': [],
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Leather Armour (AC+2)'],
            'war': [ch(['ARMOUR: Plate Mail (AC+7)', 'ARMOUR: Splint Mail (AC+6)', 'ARMOUR: Chain Mail (AC+5)'])],
        },
        'basics': list(random.sample(basics, 5)),
        'advanced': list(random.sample(advanced, 4)),
        'misc': [],
        'money': [str(die(3, 6)) + ' silver coins'],
    },
    'common': {
        'weapons': {
            'clr': [],
            'hlf': [],
            'mag': [],
            'rog': [],
            'war': [],
        },
        'armour': {
            'mag': [],
            'rog': [ch(['ARMOUR: Studded Leather (AC+3)', 'ARMOUR: Leather Armour (AC+2)'])],
            'war': [ch(['ARMOUR: Splint Mail (AC+6)', 'ARMOUR: Chain Mail (AC+5)', 'ARMOUR: Scale Mail (AC+4)'])],
        },
        'basics': list(random.sample(basics, 10)),
        'advanced': list(random.sample(advanced, 8)),
        'misc': [],
        'money': [str(die(3, 6)) + ' gold coins'],
    },
    'decent': {
        'weapons': {
            'clr': [],
            'hlf': [],
            'mag': [],
            'rog': [],
            'war': [],
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Studded Leather, finely crafted and oiled (AC+3)'],
            'war': [ch(['ARMOUR: Plate Armour (AC+8)', 'ARMOUR: Plate Mail (AC+7)', 'ARMOUR: Splint Mail (AC+6)'])],
        },
        'basics': list(random.sample(basics, 16)),
        'advanced': list(random.sample(advanced, 12)),
        'misc': [],
        'money': [str(die(10, 6)) + ' gold coins'],
    },
    'holyfuckingshit': {
        'weapons': {
            'clr': [],
            'hlf': [],
            'mag': [],
            'rog': [],
            'war': [],
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Studded Leather (AC+3)'],
            'war': [ch(['ARMOUR: Plate Armour (AC+8)', 'ARMOUR: Plate Mail (AC+7)'])],
        },
        'basics': '',
        'advanced': [str(die(3, 4)) + ' 100% Randomly Rolled Magical Items, the Sky is the Limit'],
        'misc': [],
        'money': [str(die(10, 6)) + ' gold coins'],
    },
}


def get_tier(avg):
    if avg >= 16:
        tier = 'fuckall'
    elif avg >= 13:
        tier = 'weaksauce'
    elif avg >= 9:
        tier = 'common'
    elif avg >= 6:
        tier = 'decent'
    else:
        tier = 'holyfuckingshit'
    return tier


# okay I know this is wonky, but I'm expecting the slim possibility for more systems, so just go with it.
def get_gearlist(game):
    if game in ['dd', 'bnt']:
        gearlist = basic_gear
    else:
        gearlist = basic_gear
    return gearlist


def get_gear(data, sysname, avg):
    tier = get_tier(avg)
    base_list = get_gearlist(sysname)
    weapons = list(base_list[tier]['weapons'][data['weapons']])
    armour = list(base_list[tier]['armour'][data['armour']])
    basics = list(base_list[tier]['basics'])
    advanced = list(base_list[tier]['advanced'])
    money = list(base_list[tier]['money'])
    gearList = weapons + armour + basics + advanced + money
    gearList = list(filter(None, gearList))
    return sorted(gearList)


if __name__ == "__main__":
    my_gear = get_gear('war', 'dd', 3)
    for i in my_gear:
        print(i)
    print(len(basics))
    print(len(advanced))
