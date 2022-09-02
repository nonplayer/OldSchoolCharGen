"""
Starting Gear Generator for "Dark Dungeons HAMMERED"

All weapons are marked with WEAPON: at the beginning
All armours are marked with ARMOUR: at the beginning
I'm considering doing the same for MAGIC: but haven't added it yet
these tags will be used to pull them from the gear dump and separate into their own categories
"""

# from dice import roll as die

armour = {
    'mag': [
        'ARMOUR: Leather Armour (Light, AC 7, SpellFail 10%)',
        'ARMOUR: Padded Armour (Light, AC 8, SpellFail 5%)',
        '',
        '',
        '',
        '',
        '',
    ],
    'rog': [
        'ARMOUR: Leather Armour (Light, AC 7, SpellFail 10%)',
        'ARMOUR: Padded Armour (Light, AC 8, SpellFail 5%)',
        '',
    ],
    'war': [
        'ARMOUR: Plate Mail (Heavy, AC 2, SpellFail 90%)',
        'ARMOUR: Banded Mail (Heavy, AC 3, SpellFail 70%)',
        'ARMOUR: Chain Mail (Medium, AC 4, SpellFail 50%)',
        'ARMOUR: Scale Mail (Medium, AC 5, SpellFail 30%)',
        'ARMOUR: Studded Leather (Light, AC 6, SpellFail 20%)',
    ],
    'hlf': [
        'ARMOUR: Banded Mail (Heavy, AC 3, SpellFail 70%)',
        'ARMOUR: Chain Mail (Medium, AC 4, SpellFail 50%)',
        'ARMOUR: Scale Mail (Medium, AC 5, SpellFail 30%)',
        'ARMOUR: Studded Leather (Light, AC 6, SpellFail 20%)',
        'ARMOUR: Leather Armour (Light, AC 7, SpellFail 10%)',
        'ARMOUR: Padded Armour (Light, AC 8, SpellFail 5%)',
    ],
    'brb': [
        'ARMOUR: Chain Mail (Medium, AC 4, SpellFail 50%)',
        'ARMOUR: Scale Mail (Medium, AC 5, SpellFail 30%)',
        'ARMOUR: Studded Leather (Light, AC 6, SpellFail 20%)',
        'ARMOUR: Leather Armour (Light, AC 7, SpellFail 10%)',
        'ARMOUR: Padded Armour (Light, AC 8, SpellFail 5%)',
    ],
    'fuckall': [
        'ARMOUR: blood-covered rags',
        'ARMOUR: a set of ragged prison clothes',
        'ARMOUR: a Shield made from the lid of a rubbish bin (AC-1)',
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
        'WEAPON: Dart (1H, R: 15/25/35ft, Dmg: 1d3)',
        'WEAPON: Halberd (2H, Dmg: 1d10)',
        'WEAPON: Hammer, Throwing (R: 10/20/30ft, Dmg: 1d4)',
        'WEAPON: Hammer, War (1H, Dmg: 1d6)',
        'WEAPON: Harpoon (1H, R: 20/40/60ft, Dmg: 2d4)',
        'WEAPON: Javelin (1H, R: 30/60/90ft, Dmg: 1d6)',
        'WEAPON: Lance (1H, Dmg: 1d10)',
        'WEAPON: Mace (1H, Dmg: 1d6)',
        'WEAPON: Mancatcher (2H, Dmg: 1d2, special)',
        'WEAPON: Morningstar (1H, Dmg: 1d6)',
        'WEAPON: Net (1H, R: 10/20/30ft, special)',
        'WEAPON: Pick, Light (1H, Dmg: 1d6)',
        'WEAPON: Pick, War (2H, Dmg: 1d8)',
        'WEAPON: Pike (2H, Dmg: 1d10)',
        'WEAPON: Pistol w/ 15 Charges (R: 50/100/150ft, Dmg: 1d6)',
        'WEAPON: Poleaxe (2H, Dmg: 1d10)',
        'WEAPON: Scourge (1H, special)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Smoothbore w/ 15 Charges (R: 60/160/240ft, Dmg: 2d4)',
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
        'WEAPON: Dart (1H, R: 15/25/35ft, Dmg: 1d3)',
        'WEAPON: Javelin (1H, R: 30/60/90ft, Dmg: 1d6)',
        'WEAPON: Mace (1H, Dmg: 1d6)',
        'WEAPON: Pick, Light (1H, Dmg: 1d6)',
        'WEAPON: Pistol w/ 15 Charges (R: 50/100/150ft, Dmg: 1d6)',
        'WEAPON: Scourge (1H, special)',
        'WEAPON: Sling w/ 30 Pellets (R: 40/80/160ft, Dmg: 1d4)',
        'WEAPON: Spear (1H, R: 20/40/60ft, Dmg: 1d6)',
        'WEAPON: Sword, Short (1H, Dmg: 1d6)',
        'WEAPON: Whip (1H, special)',
    ],
    'mag': [
        'WEAPON: Club (1H, Dmg: 1d4)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (R: 60/120/180ft, Dmg: 1d6)',
        'WEAPON: Dart (1H, R: 15/25/35ft, Dmg: 1d3)',
        'WEAPON: Scourge (1H, special)',
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
        'WEAPON: Mancatcher (2H, Dmg: 1d2, special)',
        'WEAPON: Morningstar (1H, Dmg: 1d6)',
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
        'WEAPON: Dart (1H, R: 15/25/35ft, Dmg: 1d3)',
        'WEAPON: Hammer, Throwing (R: 10/20/30ft, Dmg: 1d4)',
        'WEAPON: Hammer, War (1H, Dmg: 1d6)',
        'WEAPON: Mace (1H, Dmg: 1d6)',
        'WEAPON: Net (1H, R: 10/20/30ft, special)',
        'WEAPON: Pick, Light (1H, Dmg: 1d6)',
        'WEAPON: Pistol w/ 15 Charges (R: 50/100/150ft, Dmg: 1d6)',
        'WEAPON: Scourge (1H, special)',
        'WEAPON: Shield, Sword (1H, Dmg: 1d4+2)',
        'WEAPON: Sickle (1H, Dmg: 1d4)',
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
        'Backpack', 'Bedroll', 'Belt Purse', 'Chalk (1d10 pcs)', 'Cloak', 'Crowbar', 'Firewood (1d4)',
        'Flask', 'Lantern (hooded) w/ 1d2 flasks of oil', 'Mug or Tankard', 'Rain Hat',
        'Rations (preserved, 2d4)', 'Rations (fresh, 2d4)', 'Rope (50 ft)', 'Sack, Small',
        'Sack, Large', 'Sewing Kit', 'Tent', 'Tinder Box', 'Torches (1d6)', 'Waterskin', 'Whetstone',
    ],
    'advanced': [
        'Acid (1d4 flasks)', 'Alchemist Fire (1d4 flasks)', 'Antitoxin (1d4 vials)', 'Bell (tiny)',
        'Belladona', 'Blanket (winter)', 'Block and Tackle', 'Caltrops (2-pound bag)',
        'Candles (1d10)', 'Case (for map or scroll)', 'Chain (10 ft)', 'Chest', 'Cooking Pot (iron)',
        'Fishing Net (25 sq ft)', 'Fishing Hook, Line, and Pole', 'Garlic', 'Grappling Hook',
        'Healing Potions (1d4 vials, each heals for 1d6+1 HP)',
        'Hammer (small)', 'Holy Symbol', 'Holy Water (1d4 vials)', 'Ink pot, quill, and paper',
        'Iron Spike', 'Lantern (bullseye) w/ 1d2 flasks of oil', 'Mallet and 1d6 Stakes',
        'Manacles', 'Mirror (steel)', 'Notebook (small)', 'Pole (10 ft)', 'Sealing Wax',
        'Signal Whistle', 'Silver cross', 'Silver mirror', 'Soap (1 pound)', 'Spyglass',
        'Steel mirror', 'Wine (1 qt.)', 'Wolvesbane', 'Wooden cross',
    ],
    'free': [
        'Satchel/Shoulderbag', 'Torches (1d4)', 'Rations (fresh, 1d6)',
    ]
}


def get_weapons(cls):
    weapons_list = list(weapons[cls])
    return weapons_list


def get_armour(cls):
    armour_list = list(armour[cls])
    return armour_list


def get_basic_gear():
    basic_list = list(gear['basic'])
    return basic_list


def get_advanced_gear():
    advanced_list = list(gear['advanced'])
    return advanced_list


def get_free_gear():
    free_list = list(gear['free'])
    return free_list


def get_gearlist(w_cls, a_cls):
    gearlist = {
        'weapons': get_weapons(w_cls),
        'armour': get_armour(a_cls),
        'basic': get_basic_gear(),
        'advanced': get_advanced_gear(),
        'free': get_free_gear(),
    }
    return gearlist


if __name__ == "__main__":
    print(get_gearlist('rog', 'rog'))
