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
    'WEAPON: Axe, Battle (2H, Dmg: 1d8)',
    'WEAPON: Axe, Hand (1H, R: 10/20/30ft, Dmg: 1d6)',
    'WEAPON: Blackjack (1H, special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R: 20/25/30ft, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R: 10/20/30ft, special)',
    'WEAPON: Bola (R: 20/40/60ft, special)',
    ch(['WEAPON: Bow, Long w/ 20 Arrows (R: 70/140/210ft, Dmg: 1d6)',
        'WEAPON: Bow, Short w/ 20 Arrows (R: 50/100/150ft, Dmg: 1d6)']),
    'WEAPON: Cestus (1H, Dmg: 1d3)',
    'WEAPON: Club (1H, Dmg: 1d4)',
    ch(['WEAPON: Crossbow, Heavy w/ 30 Bolts (R: 80/160/240ft, Dmg: 2d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)']),
    'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Halberd (2H, Dmg: 1d10)',
    'WEAPON: Hammer, Throwing (R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Hammer, War (1H, Dmg: 1d6)',
    'WEAPON: Javelin (1H, R: 30/60/90ft, Dmg: 1d6)',
    'WEAPON: Lance (1H, Dmg: 1d10)',
    'WEAPON: Mace (1H, Dmg: 1d6)',
    'WEAPON: Net (1H, R: 10/20/30ft, special)',
    'WEAPON: Pike (2H, Dmg: 1d10)',
    'WEAPON: Poleaxe (2H, Dmg: 1d10)',
    ch(['WEAPON: Shield, Horned (1H, Dmg: 1d2)',
        'WEAPON: Shield, Knife (1H, Dmg: 1d4+1)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Shield, Tusked (1H, Dmg: 1d4+1)']),
    'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
    'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
    'WEAPON: Staff (2H, Dmg: 1d6)',
    'WEAPON: Sword, Bastard (1H or 2H, Dmg: 1d6+1)',
    'WEAPON: Sword, Normal (1H, Dmg: 1d8)',
    'WEAPON: Sword, Short (1H, Dmg: 1d6)',
    'WEAPON: Sword, Two-Handed (2H, Dmg: 1d10)',
    'WEAPON: Trident (1H, R: 10/20/30ft, Dmg: 1d6)',
    'WEAPON: Whip (1H, special)',
]

weapons_rog = [
    'WEAPON: Blackjack (1H, special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R: 20/25/30ft, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R: 10/20/30ft, special)',
    'WEAPON: Bola (R: 20/40/60ft, special)',
    'WEAPON: Bow, Short w/ 20 Arrows (R: 50/100/150ft, Dmg: 1d6)',
    'WEAPON: Club (1H, Dmg: 1d4)',
    ch(['WEAPON: Crossbow, Heavy w/ 30 Bolts (R: 80/160/240ft, Dmg: 2d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)']),
    'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Javelin (1H, R: 30/60/90ft, Dmg: 1d6)',
    'WEAPON: Mace (1H, Dmg: 1d6)',
    'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
    'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
    'WEAPON: Sword, Short (1H, Dmg: 1d6)',
    'WEAPON: Whip (1H, special)',
]

weapons_mag = [
    'WEAPON: Club (1H, Dmg: 1d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
    'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
    'WEAPON: Staff (2H, Dmg: 1d6)',
    'WEAPON: Sword, Short (1H, Dmg: 1d6)',
]

weapons_clr = [
    'WEAPON: Blackjack (1H, special)',
    'WEAPON: Bola (R: 20/40/60ft, special)',
    'WEAPON: Cestus (1H, Dmg: 1d3)',
    'WEAPON: Club (1H, Dmg: 1d4)',
    'WEAPON: Hammer, Throwing (R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Hammer, War (1H, Dmg: 1d6)',
    'WEAPON: Mace (1H, Dmg: 1d6)',
    'WEAPON: Net (1H, R: 10/20/30ft, special)',
    'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
    'WEAPON: Staff (2H, Dmg: 1d6)',
    'WEAPON: Whip (1H, special)',
]

weapons_hlf = [
    'WEAPON: Axe, Hand (1H, R: 10/20/30ft, Dmg: 1d6)',
    'WEAPON: Blackjack (1H, special)',
    'WEAPON: Blowgun (Large) w/ 5 Darts (R: 20/25/30ft, special)',
    'WEAPON: Blowgun (Small) w/ 5 Darts (R: 10/20/30ft, special)',
    'WEAPON: Bola (R: 20/40/60ft, special)',
    'WEAPON: Bow, Short w/ 20 Arrows (R: 50/100/150ft, Dmg: 1d6)',
    'WEAPON: Cestus (1H, Dmg: 1d3)',
    'WEAPON: Club (1H, Dmg: 1d4)',
    'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
    'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Hammer, Throwing (R: 10/20/30ft, Dmg: 1d4)',
    'WEAPON: Hammer, War (1H, Dmg: 1d6)',
    'WEAPON: Mace (1H, Dmg: 1d6)',
    'WEAPON: Net (1H, R: 10/20/30ft, special)',
    ch(['WEAPON: Shield, Horned (1H, Dmg: 1d2)',
        'WEAPON: Shield, Knife (1H, Dmg: 1d4+1)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Shield, Tusked (1H, Dmg: 1d4+1)']),
    'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
    'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
    'WEAPON: Staff (2H, Dmg: 1d6)',
    'WEAPON: Sword, Short (1H, Dmg: 1d6)',
    'WEAPON: Whip (1H, special)',
]

miscellany = [
    'crippling apathy', 'twitchy eyes', 'a Certain "je ne sais quoi"', 'a love of horrible puns',
    'a feeling of general loathing for everyone around you', 'a case of the wiggles', 'wanderlust in your heart',
    'an independent streak', 'the first love letter anyone every wrote you', 'a sack full of bandit ears',
    'a regrettable haircut', 'chronic silent but deadly gas', 'curious pocket lint', 'inappropriate laughing',
    'a first edition manuscript of "Winter\'s Sullen Cry"', 'all of your nail clippings, ever',
    'an irritable tabby cat', 'a map to an island that doesn\'t exist', 'a pure white badger pelt',
    'a set of pornographic goblin trading cards', 'a single strip of slightly used sandpaper',
    'a petrified dragon egg', 'a lock of hair from your mother or father', 'a fake beard',
    'rusted nipple clamps', "two weird puppets", str(die(2, 3)) + ' commemorative plates',
    'a bottle of freshly-harvested llama milk', 'a free drink coupon for the Inn, but it expires soon...',
    'a tendency to insert yourself into conversations', 'unsettling memories from last night',
    'a strong distrust for the government', 'an unsettlingly sexy facial scar',
    'a free spirit that cannot be shackled by despair', 'an obviously fake accent',
]


basic_gear = {
    'fuckall': {
        'weapons': {
            'clr': ['WEAPON: a large brass candlestick, grabbed as you ran disgraced from your temple'],
            'hlf': ['WEAPON: a large heavy rock, stained with blood'],
            'mag': ['WEAPON: Your gnarled fingernails which clawed your master\'s eyes from his skull'],
            'rog': ['WEAPON: a bone shiv which you used to escape from prison'],
            'war': ['WEAPON: a recently-detached human leg, usable as a club'],
        },
        'armour': {
            'mag': ['blood-covered robes'],
            'rog': ['a set of ragged prison clothes'],
            'war': ['ARMOUR: a Shield made from the lid of a rubbish bin (AC+1)'],
        },
        'basics': ['a half-eaten turkey leg from the festival you just left'],
        'advanced': ['the bloody tooth of someone - or something - recently deprived of its favorite tooth'],
        'money': [str(die(1, 6)) + ' copper coins'],
        'misc': [str(ch(list(miscellany)))],
    },
    'weaksauce': {
        'weapons': {
            'clr': [str(ch(list(weapons_clr)))],
            'hlf': list(random.sample(weapons_hlf, 2)),
            'mag': [str(ch(list(weapons_mag)))],
            'rog': [str(ch(list(weapons_rog)))],
            'war': list(random.sample(weapons_war, 2)),
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Leather Armour (AC+2)'],
            'war': [ch(['ARMOUR: Plate Mail (AC+7)', 'ARMOUR: Splint Mail (AC+6)', 'ARMOUR: Chain Mail (AC+5)'])],
        },
        'basics': list(random.sample(basics, 6)),
        'advanced': list(random.sample(advanced, 4)),
        'misc': [str(ch(list(miscellany)))],
        'money': [str(die(3, 6)) + ' silver coins'],
    },
    'common': {
        'weapons': {
            'clr': list(random.sample(weapons_clr, 3)),
            'hlf': list(random.sample(weapons_hlf, 4)),
            'mag': list(random.sample(weapons_mag, 2)),
            'rog': list(random.sample(weapons_rog, 3)),
            'war': list(random.sample(weapons_war, 4)),
        },
        'armour': {
            'mag': [],
            'rog': [ch(['ARMOUR: Studded Leather (AC+3)', 'ARMOUR: Leather Armour (AC+2)'])],
            'war': [
                ch(['ARMOUR: Splint Mail (AC+6)', 'ARMOUR: Chain Mail (AC+5)', 'ARMOUR: Scale Mail (AC+4)']),
                ch(['', 'ARMOUR: a Shield (AC+1)'])
            ],
        },
        'basics': list(random.sample(basics, 8)),
        'advanced': list(random.sample(advanced, 6)),
        'misc': [str(ch(list(miscellany)))],
        'money': [str(die(3, 6)) + ' gold coins'],
    },
    'decent': {
        'weapons': {
            'clr': list(random.sample(weapons_clr, 4)),
            'hlf': list(random.sample(weapons_hlf, 5)),
            'mag': list(random.sample(weapons_mag, 3)),
            'rog': list(random.sample(weapons_rog, 4)),
            'war': list(random.sample(weapons_war, 5)),
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Studded Leather, finely crafted and oiled (AC+3)'],
            'war': [
                ch(['ARMOUR: Plate Armour (AC+8)', 'ARMOUR: Plate Mail (AC+7)', 'ARMOUR: Splint Mail (AC+6)']),
                ch(['', 'ARMOUR: a Shield (AC+1)', 'ARMOUR: a Tower Shield (AC+2)'])
            ],
        },
        'basics': list(random.sample(basics, 10)),
        'advanced': list(random.sample(advanced, 8)),
        'misc': [str(ch(list(miscellany)))],
        'money': [str(die(10, 6)) + ' gold coins'],
    },
    'holyfuckingshit': {
        'weapons': {
            'clr': ['Two 100% Randomly Rolled Magical Weapons, class-appropriate, which vanish upon your death.'],
            'hlf': ['Two 100% Randomly Rolled Magical Weapons, class-appropriate, which vanish upon your death.'],
            'mag': ['Two 100% Randomly Rolled Magical Weapons, class-appropriate, which vanish upon your death.'],
            'rog': ['Two 100% Randomly Rolled Magical Weapons, class-appropriate, which vanish upon your death.'],
            'war': ['Four 100% Randomly Rolled Magical Weapons, class-appropriate, which vanish upon your death.'],
        },
        'armour': {
            'mag': [],
            'rog': ['ARMOUR: Studded Leather (AC+3)'],
            'war': [ch(['ARMOUR: Plate Armour (AC+8)', 'ARMOUR: Plate Mail (AC+7)'])],
        },
        'basics': list(random.sample(basics, 12)),
        'advanced': list(random.sample(advanced, 12)),
        'misc': [str(ch(list(miscellany))), 'Four 100% Randomly Rolled Magical Trinkets, which vanish upon your death'],
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
    wep_list = list(base_list[tier]['weapons'][data['weapons']])
    arm_list = list(base_list[tier]['armour'][data['armour']])
    bas_list = list(base_list[tier]['basics'])
    adv_list = list(base_list[tier]['advanced'])
    msc_list = list(base_list[tier]['misc'])
    mny_list = list(base_list[tier]['money'])
    # just some free stuff for everyone
    bonus = ['Satchel']
    my_gearlist = wep_list + arm_list + bas_list + adv_list + msc_list + mny_list + bonus
    my_gearlist = list(filter(None, my_gearlist))
    return sorted(my_gearlist)


if __name__ == "__main__":
    my_gear = get_gear('war', 'dd', 3)
    for i in my_gear:
        print(i)
    print(len(basics))
    print(len(advanced))
