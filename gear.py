"""
testing new way to generate gear
"""

from dice import roll as die

armour = {
    'mag': [
        'ARMOUR: Studded Leather (Light, AC+3)',
        'ARMOUR: Leather Armour (Light, AC+2)',
        'ARMOUR: Padded Armour (Light, AC+1)',
        '',
        '',
    ],
    'rog': [
        'ARMOUR: Studded Leather (Light, AC+3)',
        'ARMOUR: Leather Armour (Light, AC+2)',
        'ARMOUR: Padded Armour (Light, AC+1)',
        '',
    ],
    'war': [
        'ARMOUR: Plate Mail (Heavy, AC+7)',
        'ARMOUR: Splint Mail (Heavy, AC+6)',
        'ARMOUR: Chain Mail (Medium, AC+5)',
        'ARMOUR: Scale Mail (Medium, AC+4)',
        'ARMOUR: Studded Leather (Light, AC+3)',
    ],
    'hlf': [
        'ARMOUR: Splint Mail (Heavy, AC+6)',
        'ARMOUR: Chain Mail (Medium, AC+5)',
        'ARMOUR: Scale Mail (Medium, AC+4)',
        'ARMOUR: Studded Leather (Light, AC+3)',
        'ARMOUR: Leather Armour (Light, AC+2)',
        'ARMOUR: Padded Armour (Light, AC+1)',
    ],
    'brb': [
        'ARMOUR: Chain Mail (Medium, AC+5)',
        'ARMOUR: Scale Mail (Medium, AC+4)',
        'ARMOUR: Studded Leather (Light, AC+3)',
        'ARMOUR: Leather Armour (Light, AC+2)',
        'ARMOUR: Padded Armour (Light, AC+1)',
    ],
    'fuckall': [
        'ARMOUR: blood-covered rags',
        'ARMOUR: a set of ragged prison clothes',
        'ARMOUR: a Shield made from the lid of a rubbish bin (AC+1)',
    ],
    'holyfuckingshit': [
        'ARMOUR: A Randomly-Rolled Magical Armour, class-appropriate, which crumbles to dust upon your death.',
    ],
}

weapons = {
    'war': [
        'ARMOUR: a Shield (AC+1)',
        'ARMOUR: a Tower Shield (AC+2)',
        'WEAPON: Axe, Battle (2H, Dmg: 1d8)',
        'WEAPON: Axe, Hand (1H, R: 10/20/30ft, Dmg: 1d6)',
        'WEAPON: Blackjack (1H, special)',
        'WEAPON: Blowgun (Large) w/ 5 Darts (R: 20/25/30ft, special)',
        'WEAPON: Blowgun (Small) w/ 5 Darts (R: 10/20/30ft, special)',
        'WEAPON: Bola (R: 20/40/60ft, special)',
        'WEAPON: Bow, Long w/ 20 Arrows (R: 70/140/210ft, Dmg: 1d6)',
        'WEAPON: Bow, Short w/ 20 Arrows (R: 50/100/150ft, Dmg: 1d6)',
        'WEAPON: Cestus (1H, Dmg: 1d3)',
        'WEAPON: Club (1H, Dmg: 1d4)',
        'WEAPON: Crossbow, Heavy w/ 30 Bolts (R: 80/160/240ft, Dmg: 2d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
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
        'WEAPON: Shield, Horned (1H, Dmg: 1d2)',
        'WEAPON: Shield, Knife (1H, Dmg: 1d4+1)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Shield, Tusked (1H, Dmg: 1d4+1)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
        'WEAPON: Staff (2H, Dmg: 1d6)',
        'WEAPON: Sword, Bastard (1H or 2H, Dmg: 1d6+1)',
        'WEAPON: Sword, Normal (1H, Dmg: 1d8)',
        'WEAPON: Sword, Short (1H, Dmg: 1d6)',
        'WEAPON: Sword, Two-Handed (2H, Dmg: 1d10)',
        'WEAPON: Trident (1H, R: 10/20/30ft, Dmg: 1d6)',
        'WEAPON: Whip (1H, special)',
    ],
    'rog': [
        'ARMOUR: a Shield (AC+1)',
        'WEAPON: Blackjack (1H, special)',
        'WEAPON: Blowgun (Large) w/ 5 Darts (R: 20/25/30ft, special)',
        'WEAPON: Blowgun (Small) w/ 5 Darts (R: 10/20/30ft, special)',
        'WEAPON: Bola (R: 20/40/60ft, special)',
        'WEAPON: Bow, Short w/ 20 Arrows (R: 50/100/150ft, Dmg: 1d6)',
        'WEAPON: Club (1H, Dmg: 1d4)',
        'WEAPON: Crossbow, Heavy w/ 30 Bolts (R: 80/160/240ft, Dmg: 2d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
        'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
        'WEAPON: Javelin (1H, R: 30/60/90ft, Dmg: 1d6)',
        'WEAPON: Mace (1H, Dmg: 1d6)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
        'WEAPON: Sword, Short (1H, Dmg: 1d6)',
        'WEAPON: Whip (1H, special)',
    ],
    'mag': [
        'WEAPON: Club (1H, Dmg: 1d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
        'WEAPON: Dagger (1H, R: 10/20/30ft, Dmg: 1d4)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Staff (2H, Dmg: 1d6)',
        'WEAPON: Sword, Short (1H, Dmg: 1d6)',
    ],
    'clr': [
        'ARMOUR: a Shield (AC+1)',
        'ARMOUR: a Tower Shield (AC+2)',
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
    ],
    'hlf': [
        'ARMOUR: a Shield (AC+1)',
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
        'WEAPON: Shield, Horned (1H, Dmg: 1d2)',
        'WEAPON: Shield, Knife (1H, Dmg: 1d4+1)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Shield, Tusked (1H, Dmg: 1d4+1)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
        'WEAPON: Staff (2H, Dmg: 1d6)',
        'WEAPON: Sword, Short (1H, Dmg: 1d6)',
        'WEAPON: Whip (1H, special)',
    ],
    'fuckall': [
        'WEAPON: a large brass candlestick, grabbed as you ran disgraced from your temple (1H Melee, Dmg: 1d4)',
        'WEAPON: a large heavy rock, stained with blood (1H Melee, Dmg: 1d4)',
        'WEAPON: Your gnarled fingernails which clawed your master\'s eyes from his skull (1H Melee, Dmg: 1d4)',
        'WEAPON: a bone shiv which you used to escape from prison (1H Melee, Dmg: 1d4)',
        'WEAPON: a recently-detached human leg, usable as a club (1H Melee, Dmg: 1d4)',
    ],
    'holyfuckingshit': [
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate, which crumbles to dust upon your death.',
    ]
}

gear = {
    'basic': [
        'Backpack', 'Bedroll', 'Belt Purse', 'Chalk (1d10 pcs)', 'Cloak', 'Crowbar', 'Firewood (1d4 units)',
        'Flask', 'Lantern (hooded) w/ 1d2 flasks of oil', 'Mug or Tankard', 'Rain Hat',
        'Rations (iron, 2d4 units)', 'Rations (standard, 2d4 units)', 'Rope (50 ft)', 'Sack, Small',
        'Sack, Large', 'Sewing Kit', 'Tent', 'Tinder Box', 'Torches (1d6)', 'Waterskin', 'Whetstone',
    ],
    'advanced': [
        'Acid (1d4 flasks)', 'Alchemist Fire (1d4 flasks)', 'Antitoxin (1d4 vials)', 'Bell (tiny)',
        'Belladona', 'Blanket (winter)', 'Block and Tackle', 'Caltrops (2-pound bag)',
        'Candles (1d10)', 'Case (for map or scroll)', 'Chain (10 ft)', 'Chest', 'Cooking Pot (iron)',
        'Fishing Net (25 sq ft)', 'Fishing Hook, Line, and Pole', 'Garlic', 'Grappling Hook',
        'Hammer (small)', 'Holy Symbol', 'Holy Water (small vial)', 'Ink pot, quill, and paper',
        'Iron Spike', 'Lantern (bullseye) w/ 1d2 flasks of oil', 'Mallet and 1d6 Stakes',
        'Manacles', 'Mirror (steel)', 'Notebook (small)', 'Pole (10 ft)', 'Sealing Wax',
        'Signal Whistle', 'Silver cross', 'Silver mirror', 'Soap (1 pound)', 'Spyglass',
        'Steel mirror', 'Wine (1 qt.)', 'Wolvesbane', 'Wooden cross',
    ],
}

miscellany = [
    'crippling apathy', 'twitchy eyes', 'a Certain "je ne sais quoi"', 'a love of horrible puns',
    'a feeling of general loathing for everyone around you', 'a case of the wiggles', 'wanderlust in your heart',
    'an independent streak', 'the first love letter anyone every wrote you', 'a sack full of bandit ears',
    'a regrettable haircut', 'chronic silent but deadly gas', 'curious pocket lint', 'inappropriate laughing',
    'a first edition manuscript of "Winter\'s Sullen Cry"', 'all of your nail clippings, ever',
    'an irritable tabby cat', 'a map to an island that doesn\'t exist', 'a pure white badger pelt',
    'a set of pornographic goblin trading cards', 'a single strip of slightly used sandpaper',
    'a petrified dragon egg', 'a lock of hair from your mother or father', 'a fake beard',
    'rusted nipple clamps', "two weird puppets", '1D6 commemorative plates',
    'a bottle of freshly-harvested llama milk', 'a free drink coupon for the Inn, but it expires soon...',
    'a tendency to insert yourself into conversations', 'unsettling memories from last night',
    'a strong distrust for the government', 'an unsettlingly sexy facial scar',
    'a free spirit that cannot be shackled by despair', 'an obviously fake accent',
    'a feeling like you forgot something very important before heading out...',
    'a case of the wiggles', 'a recently-unlocked chastity belt',
    'a letter of recommendation from someone important', 'a tourist brochure for the dungeon',
    'a signed Maseym\'s Bears Base-Ball', 'an undislodgeable wedgie',
    'a very nice fitted suit', 'a scrap of finely-groomed gnoll hair',
    'a visible tattoo that you deeply regret', 'a massive debt of back rent',
    'an unbreakable padlock that can never be opened once clicked (currently open)',
    'shame, so much shame', 'the constant doting of your parents',
    'the knowledge that you recently betrayed someone in the party', 'a conspicuously dead parrot',
    'a strong craving for pot pies', 'a rock in a sock',
]


def get_weapons(cls):
    weapons_list = list(weapons[cls])
    return weapons_list


def get_armour(cls):
    armour_list = list(armour[cls])
    return armour_list


def get_misc():
    misc = list(miscellany)
    return misc


def get_basic_gear():
    basic_list = list(gear['basic'])
    return basic_list


def get_advanced_gear():
    advanced_list = list(gear['advanced'])
    return advanced_list


def get_gearlist(w_cls, a_cls):
    gearlist = {
        'weapons': get_weapons(w_cls),
        'armour': get_armour(a_cls),
        'basic': get_basic_gear(),
        'advanced': get_advanced_gear(),
        'misc': get_misc(),
    }
    return gearlist


if __name__ == "__main__":
    print(get_gearlist('rog'))
