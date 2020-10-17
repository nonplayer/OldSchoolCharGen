"""
HAMMERCRAWL! Variant Gear Generator

Derived from the DnD Variant Gear Generator
"""

# from dice import roll as die

armour = {
    'mag': [
        'ARMOUR: Studded Leather (Light, Size M, DEF+3)',
        'ARMOUR: Leather Armour (Light, Size M, DEF+2)',
        'ARMOUR: Padded Armour (Light, Size M, DEF+1)',
        '',
        '',
    ],
    'rog': [
        'ARMOUR: Studded Leather (Light, Size M, DEF+3)',
        'ARMOUR: Leather Armour (Light, Size M, DEF+2)',
        'ARMOUR: Padded Armour (Light, Size M, DEF+1)',
        '',
    ],
    'war': [
        'ARMOUR: Splint Mail (Heavy, Size L, DEF+6)',
        'ARMOUR: Chain Mail (Heavy, Size L, DEF+5)',
        'ARMOUR: Scale Mail (Heavy, Size L, DEF+4)',
        'ARMOUR: Studded Leather (Light, Size M, DEF+3)',
    ],
    'hlf': [
        'ARMOUR: Splint Mail (Heavy, Size L, DEF+6)',
        'ARMOUR: Chain Mail (Heavy, Size L, DEF+5)',
        'ARMOUR: Scale Mail (Heavy, Size L, DEF+4)',
        'ARMOUR: Studded Leather (Light, Size M, DEF+3)',
        'ARMOUR: Leather Armour (Light, Size M, DEF+2)',
        'ARMOUR: Padded Armour (Light, Size M, DEF+1)',
    ],
    'brb': [
        'ARMOUR: Chain Mail (Heavy, Size L, DEF+5)',
        'ARMOUR: Scale Mail (Heavy, Size L, DEF+4)',
        'ARMOUR: Studded Leather (Light, Size M, DEF+3)',
        'ARMOUR: Leather Armour (Light, Size M, DEF+2)',
        'ARMOUR: Padded Armour (Light, Size M, DEF+1)',
    ],
    'fuckall': [
        'ARMOUR: blood-covered rags',
        'ARMOUR: a set of ragged prison clothes',
        'ARMOUR: a Shield made from the lid of a rubbish bin (1H, Size M, DEF+1)',
    ],
    'holyfuckingshit': [
        'ARMOUR: A Randomly-Rolled Magical Armour, class-appropriate.',
    ],
}

weapons = {
    'war': [
        'ARMOUR: a Small Shield (1H, Size M, DEF+2)',
        'ARMOUR: a Tower Shield (1H, Size L, DEF+3)',
        'WEAPON: Axe, Battle (1H, Size M, Dmg M+2)',
        'WEAPON: Axe, Throwing (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Blackjack (1H, Size M, Dmg M+1, Tactical)',
        'WEAPON: Blowgun w/ 5 Darts (1H, Size S, R: 10/30ft, Tactical)',
        'WEAPON: Bola (1H, Size M, R: 20/60ft, Tactical)',
        'WEAPON: Bow, Long w/ 20 Arrows (2H, Size L, R: 55/220ft)',
        'WEAPON: Bow, Short w/ 20 Arrows (2H, Size M, R: 75/150ft)',
        'WEAPON: Cestus (1H, Size M, Dmg: M+1)',
        'WEAPON: Club (1H, Size M, Dmg: M+2)',
        'WEAPON: Crossbow, Heavy w/ 30 Bolts (2H, Size L, R: 80/240ft, Awesome 2, Reload 2)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (2H, Size M, R: 60/180ft, Awesome 1, Reload 1)',
        'WEAPON: Dagger (1H, Size S, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Dagger, Punching (1H, Size S, Dmg: M+1)',
        'WEAPON: Greataxe (2H, Size L, Dmg: M+3)',
        'WEAPON: Greatclub (2H, Size L, Dmg: M+3)',
        'WEAPON: Greatmace (2H, Size L, Dmg: M+3)',
        'WEAPON: Greatsword (2H, Size L, Dmg: M+3)',
        'WEAPON: Hammer, Light (1H, Size M, R: 10/30ft, Dmg: M+1)',
        'WEAPON: Hammer, War (1H, Size M, Dmg: M+2)',
        'WEAPON: Javelin (1H, Size M, R: 20/60ft, Dmg: M+1, Thrown)',
        'WEAPON: Lance (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Mace, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Military Fork (2H, Size L, Dmg: M+3)',
        'WEAPON: Net (1H, Tactical)',
        'WEAPON: Pick, Heavy (2H, Size L, Dmg: M+3)',
        'WEAPON: Pick, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Polearm, Glaive (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Guisarme (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Halberd (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Lucerne Hammer (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Pike (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Pole Axe (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Polearm, Ranseur (2H, Size L, Dmg: M+3, Reach)',
        'WEAPON: Scimitar (1H, Size M, Dmg: M+2)',
        'WEAPON: Rapier (1H, Size M, Dmg: M+2)',
        'WEAPON: Scythe (2H, Size L, Dmg: M+3)',
        'WEAPON: Shield, Horned (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Knife (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Sword (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Tusked (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Sling w/ 30 Pellets (1H, Size S, R: 60/180ft)',
        'WEAPON: Spear, Short (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Staff (1H, Size M, Dmg: M+1)',
        'WEAPON: Sword, Bastard (1H or 2H, Size L, Dmg: M+2 or M+3)',
        'WEAPON: Sword, Broad (1H, Size M, Dmg: M+2)',
        'WEAPON: Sword, Long (1H, Size M, Dmg: M+2)',
        'WEAPON: Sword, Short (1H, Size M, Dmg: M+1)',
        'WEAPON: Trident (1H, Size M, Dmg: M+2)',
        'WEAPON: Whip (1H, Size M, Tactical)',
    ],
    'rog': [
        'ARMOUR: a Buckler Shield (1H, Size M, DEF+1, Special)',
        'WEAPON: Blackjack (1H, Size M, Dmg M+1, Tactical)',
        'WEAPON: Blowgun w/ 5 Darts (1H, Size S, R: 10/30ft, Tactical)',
        'WEAPON: Bola (1H, Size M, R: 20/60ft, Tactical)',
        'WEAPON: Bow, Short w/ 20 Arrows (2H, Size M, R: 75/150ft)',
        'WEAPON: Club (1H, Size M, Dmg: M+2)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (2H, Size M, R: 60/180ft, Awesome 1, Reload 1)',
        'WEAPON: Dagger (1H, Size S, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Dagger, Punching (1H, Size S, Dmg: M+1)',
        'WEAPON: Javelin (1H, Size M, R: 20/60ft, Dmg: M+1, Thrown)',
        'WEAPON: Mace, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Pick, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Rapier (1H, Size M, Dmg: M+2)',
        'WEAPON: Scimitar (1H, Size M, Dmg: M+2)',
        'WEAPON: Sling w/ 30 Pellets (1H, Size S, R: 60/180ft)',
        'WEAPON: Spear, Short (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Sword, Short (1H, Size M, Dmg: M+1)',
        'WEAPON: Whip (1H, Size M, Tactical)',
    ],
    'mag': [
        'WEAPON: Blackjack (1H, Size M, Dmg M+1, Tactical)',
        'WEAPON: Blowgun w/ 5 Darts (1H, Size S, R: 10/30ft, Tactical)',
        'WEAPON: Bola (1H, Size M, R: 20/60ft, Tactical)',
        'WEAPON: Cestus (1H, Size M, Dmg: M+1)',
        'WEAPON: Club (1H, Size M, Dmg: M+2)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (2H, Size M, R: 60/180ft, Awesome 1, Reload 1)',
        'WEAPON: Dagger (1H, Size S, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Dagger, Punching (1H, Size S, Dmg: M+1)',
        'WEAPON: Hammer, Light (1H, Size M, R: 10/30ft, Dmg: M+1)',
        'WEAPON: Javelin (1H, Size M, R: 20/60ft, Dmg: M+1, Thrown)',
        'WEAPON: Mace, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Net (1H, Tactical)',
        'WEAPON: Pick, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Rapier (1H, Size M, Dmg: M+2)',
        'WEAPON: Sling w/ 30 Pellets (1H, Size S, R: 60/180ft)',
        'WEAPON: Spear, Short (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Staff (1H, Size M, Dmg: M+1)',
        'WEAPON: Sword, Long (1H, Size M, Dmg: M+2)',
        'WEAPON: Sword, Short (1H, Size M, Dmg: M+1)',
    ],
    'clr': [
        'ARMOUR: a Small Shield (1H, Size M, DEF+2)',
        'ARMOUR: a Tower Shield (1H, Size L, DEF+3)',
        'WEAPON: Blackjack (1H, Size M, Dmg M+1, Tactical)',
        'WEAPON: Bola (1H, Size M, R: 20/60ft, Tactical)',
        'WEAPON: Cestus (1H, Size M, Dmg: M+1)',
        'WEAPON: Club (1H, Size M, Dmg: M+2)',
        'WEAPON: Greatclub (2H, Size L, Dmg: M+3)',
        'WEAPON: Greatmace (2H, Size L, Dmg: M+3)',
        'WEAPON: Hammer, Light (1H, Size M, R: 10/30ft, Dmg: M+1)',
        'WEAPON: Hammer, War (1H, Size M, Dmg: M+2)',
        'WEAPON: Mace, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Net (1H, Tactical)',
        'WEAPON: Sling w/ 30 Pellets (1H, Size S, R: 60/180ft)',
        'WEAPON: Staff (1H, Size M, Dmg: M+1)',
        'WEAPON: Whip (1H, Size M, Tactical)',
    ],
    'hlf': [
        'ARMOUR: a Buckler Shield (1H, Size M, DEF+1, Special)',
        'ARMOUR: a Small Shield (1H, Size M, DEF+2)',
        'WEAPON: Axe, Throwing (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Blackjack (1H, Size M, Dmg M+1, Tactical)',
        'WEAPON: Blowgun w/ 5 Darts (1H, Size S, R: 10/30ft, Tactical)',
        'WEAPON: Bola (1H, Size M, R: 20/60ft, Tactical)',
        'WEAPON: Bow, Short w/ 20 Arrows (2H, Size M, R: 75/150ft)',
        'WEAPON: Cestus (1H, Size M, Dmg: M+1)',
        'WEAPON: Club (1H, Size M, Dmg: M+2)',
        'WEAPON: Crossbow, Light w/ 30 Bolts (2H, Size M, R: 60/180ft, Awesome 1, Reload 1)',
        'WEAPON: Dagger (1H, Size S, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Dagger, Punching (1H, Size S, Dmg: M+1)',
        'WEAPON: Hammer, Light (1H, Size M, R: 10/30ft, Dmg: M+1)',
        'WEAPON: Hammer, War (1H, Size M, Dmg: M+2)',
        'WEAPON: Mace, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Net (1H, Tactical)',
        'WEAPON: Pick, Light (1H, Size M, Dmg: M+2)',
        'WEAPON: Rapier (1H, Size M, Dmg: M+2)',
        'WEAPON: Shield, Horned (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Knife (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Sword (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Shield, Tusked (1H, Size M, Dmg: M+1, Shield Weapon)',
        'WEAPON: Sling w/ 30 Pellets (1H, Size S, R: 60/180ft)',
        'WEAPON: Spear, Short (1H, Size M, R: 10/30ft, Dmg: M+1, Thrown)',
        'WEAPON: Staff (1H, Size M, Dmg: M+1)',
        'WEAPON: Sword, Short (1H, Size M, Dmg: M+1)',
        'WEAPON: Whip (1H, Size M, Tactical)',
    ],
    'fuckall': [
        'WEAPON: a large brass candlestick, grabbed as you ran disgraced from your temple (1H, Size M, Dmg: M+1)',
        'WEAPON: a large heavy rock, stained with blood (1H, Size S, Dmg: M+1)',
        'WEAPON: Your gnarled fingernails which clawed your master\'s eyes from his skull (1H, Dmg: M+1)',
        'WEAPON: a bone shiv which you used to escape from prison (1H, Size S, R: 10/30, Dmg: M+1, Thrown)',
        'WEAPON: a recently-detached human leg, usable as a club (1H, Size M, Dmg: M+1)',
    ],
    'holyfuckingshit': [
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
        'WEAPON: A Randomly-Rolled Magical Weapon, class-appropriate.',
    ]
}

gear = {
    'free': [
        'Satchel (S; Bag 5M, Fragile, Wearable)', 'Rations (fresh, 1d4 units, S)', 'Torch, 1 (S)',
        '1 set of clothes to match your rolled attire',
    ],
    'basic': [
        'Backpack (M, Bag 10L, Wearable)', 'Bedroll (M)', 'Bell, Tiny (S)', 'Belt Purse (S, Bag 1S, Wearable)',
        'Blanket (M))', 'Candles (1d10, S)', 'Chalk (1d10 pcs, S)', 'Cloak (M)', 'Cooking Pot, Iron (L)',
        'Firewood (1d4 units, M)', 'Flask (S)', 'Garlic (1d4 cloves, S)', 'Hammer, Small (S)',
        'Holy Symbol, Wooden (S)', 'Iron Spike (S)', 'Mug or Tankard (S)', 'Pole (10 ft, L)', 'Rain Hat (M)',
        'Rations (fresh, 2d4 units, S)', 'Rope (50 ft, M)', 'Sack (M[S], Bag 5M, Fragile)', 'Soap (1 puck, S)',
        'Tinder Box (M)', 'Torches (1d6, S)', 'Waterskin, Gallon (M)', 'Whetstone (S)', 'Wine Bottle (M)',
    ],
    'advanced': [
        'Acid (1d4 flasks, S)', 'Alchemist Fire (1d4 flasks, S)', 'Antitoxin (1d4 vials, S)',
        'Bandoliers (M, Bag 3S, Wearable)', 'Belladona (1d4 sprigs, S)', 'Block and Tackle (M)',
        'Caltrops (2-pound bag, M)', 'Case, Scroll (S, Bag 1*, Durable)', 'Chain (10 ft, M)',
        'Chest, Small (M, Bag 5S, Durable)', 'Chest, Medium (L, Bag 10M, Durable)', 'Crowbar (M)',
        'Fishing Net (25 sq ft, M)', 'Fishing Hook, Line, and Pole (M)', 'Grappling Hook (M)',
        'Healing Potions (1d4 vials, each heals for 1d6+1 HP; S)', 'Holy Symbol, Wooden (S)',
        'Holy Water (1d4 vials, S)', 'Holy Symbol, Silver (S)', 'Ink pot, quill, and paper (S)',
        'Lantern (M) w/ 1d2 flasks of oil (S)', 'Mallet and 1d6 Stakes (S)', 'Manacles (M)', 'Mirror, Steel (M)',
        'Mirror, Silver (M)', 'Notebook (M)', 'Rations (preserved, 2d4 units, S)', 'Sealing Wax (S)',
        'Sewing Kit (S)', 'Signal Whistle (S)', 'Spyglass (M)', 'Tent (L)', 'Wolvesbane (1d4 sprigs, S)',
    ],
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
