"""
This file will be where I eventually expand the program to accommodate different games.
Right now, I'm just focusing on The Nightmares Underneath.
I'm sure there's got to be a better way to do this in a "pythonic" way, but I'm new, so this is my solution.

Systems Represented:
bnt = Blood & Treasure
dd = Dark Dungeons (my first planned expansion, further down the road)
tnu = The Nightmares Underneath
plt = Microlite Platinum

Valid Types:
dnd = this game follows most basic D&D expectations
plt = this game derives from microlite platinum
tnu = the nightmares underneath (it really is pretty unique here...)
"""

statArrays = {
    'dnd': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    'tnu': ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL'],
    'pla': ['ICQ', 'MEE', 'MAF', 'PST', 'PRW', 'PND', 'PBT', 'RUN'],
}

statMods = {
    'bnt': {
        'STR': 'Melee Attack rolls, Damage with Melee and Thrown',
        'INT': 'Known Languages, Mage Spells per day',
        'WIS': 'Will Saves, Cleric Spells per day',
        'DEX': 'Ranged Attacks, AC, Reflex Saves',
        'CON': 'Hit Point rolls, Fortitude Saves',
        'CHA': 'Leadership, Reaction rolls, Bard/Sorc Spells per day'
    },
    'dd': {
        'STR': 'Melee Attack rolls, Damage with Melee and Thrown',
        'INT': '',
        'WIS': 'Saves vs Spells',
        'DEX': 'Ranged Attacks, AC, Initiative',
        'CON': 'Hit Point rolls',
        'CHA': 'Leadership, Reaction rolls'
    },
    'tnu': {
        'CHA': 'Social rolls',
        'DEX': 'Evasion, Initiative, Ranged Attacks, Special Maneuvers',
        'FER': 'Melee Attack and Damage rolls, Open Doors/Chests, Saves vs Confinement',
        'HEA': 'Recovery Rolls, Saves vs Disease and Poison',
        'INT': 'Surprise, Spells Memorized, Saves vs Falsehood',
        'WIL': 'Spells Mastered, Abjure Spirits, Saves vs Mental Effects'
    },
    'pla': {
        'ICQ': 'Mental Skills',
        'MEE': 'Mind Saves',
        'MAF': 'Social Skills, Invoke Trust or Intimidate',
        'PST': 'Damage with Melee, Thrown, and Bow Weapons',
        'PRW': 'Physical Skills; Combat Rolls other than Initiative/Saves/Damage',
        'PND': 'Body Saves',
        'PBT': 'Social Skills, Invoke Charm or Impress',
        'MOV': 'Initiative, Running Speed = stat * .68 mph'
    },
}

'''
I'm sure the above two could be merged, but I added the second dict late in the game,
after already writing code that used the statArrays lists to generate character spreads.
Converting that code to use a dict would be more of a pain in the ass than I feel like
dealing with currently.
'''


saves = {
    'one': ['Saving Throw'],
    'three': ['Fortitude', 'Reflex', 'Willpower'],
    'five': ['Death Ray & Poison', 'Magic Wands', 'Paralysis & Petrification', 'Breath Weapon', 'Rod, Staff, & Spell'],
    'six': statArrays['dnd'],
    'pla': ['Mind', 'Body', 'Reflex', 'Horror Factor (HF)'],
}


dnd_races = {
    'bnt': {
        'human': {
            'label': "Human",
            'traits': ['(Racial) Medium size with a base speed of 30 feet.',
                       '(Racial) 10% bonus to all earned experience.',
                       '(Racial) +1 bonus to all saving throws.',
                       '(Racial) Speak Common and can learn any other language.'],
        },
        'dwarf': {
            'label': "Dwarf",
            'traits': [
                '(Racial) Medium size with a base speed of 20.',
                '(Racial) See in the dark up to 60 feet via black and white "darkvision".',
                '(Racial) +3 bonus on Fortitude saving throws vs poison.',
                '(Racial) +3 bonus on Will saves against magic (Dwarf spellcasters lose this bonus).',
                '(Racial) knack for noticing unusual stonework and intuiting depth.',
                '(Racial) Speak Common and Dwarven. They might also speak Gnome, Goblin, '
                'Kobold, Orc, Ogre, Hill Giant and Earth Elemental.',
                '(Racial) +1 attack vs goblins, hobgoblins and orcs.',
                '(Racial) +4 AC vs large humanoids like giants.'
            ],
        },
        'elf': {
            'label': "Elf",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to a range of 60 feet.',
                '(Racial) Chance to find secret doors by passing within 5 feet.',
                '(Racial)  +1 bonus to hit with long and short bows, and long and short swords.',
                '(Racial) 90% magic resistance to sleep spells and enchantment spells.',
                '(Racial) Immunity to ghoul paralysis.',
                '(Racial) Speak Common and Elven. They might also speak Gnoll, Gnome, Goblin, Orc, Sylvan and Dragon.'
            ],
        },
        'gnome': {
            'label': "Gnome",
            'traits': [
                '(Racial) Small size with a base speed of 20 feet.',
                '(Racial) Darkvision to a range of 60 feet.',
                '(Racial) Knack for listening at doors.',
                '(Racial) If CHA is 10 or higher can cast the following spells, 1x/day each: '
                'Audible glamer, dancing lights and prestidigitation.',
                '(Racial) +2 bonus on Will saving throws against illusions.',
                '(Racial) Speak Common and Gnome. They might also speak Dwarf, Elf, Goblin, '
                'Hill Giant, Orc, Sylvan and the language of burrowing mammals.'
            ],
        },
        'halfelf': {
            'label': "Half-Elf",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to a range of 60 feet.',
                '(Racial) 30% magic resistance to sleep and enchantment spells.',
                '(Racial) Knack for trickery.',
                '(Racial) Speak Common and Elven and can learn virtually any other language.'
            ],
        },
        'halforc': {
            'label': "Half-Orc",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to 60 feet.',
                '(Racial) Speak Common and Orc. They might also speak Gnoll, Goblin, Hill Giant, Ogre or Dragon.'
            ],
        },
        'halfling': {
            'label': "Halfling",
            'traits': [
                '(Racial) Small size with a base speed of 20 feet.',
                '(Racial) Darkvision to a range of 30 feet.',
                '(Racial) +1 bonus when attacking with slings and thrown weapons.',
                '(Racial) Knack for hiding, moving silently and getting into trouble.',
                '(Racial) Speak Common and Halfling. They might also speak '
                'Dwarven, Elven, Gnome, Goblin, Kobold or Orc.'
            ],
        },
    },
}


systems = {
    'default': {
        'name': 'def',                  # shortname for the system, used in some lists and dicts
        'fullName': 'Default Display Name',
        'type': 'dnd',                  # STR: basic system type, and associated assumptions
        'hasHPs': True,                 # BOO: changes the calculations if the system has hit points
        'stats': 6,                     # INT: how many stats in this system, usually 6
        'spread': statArrays['dnd'],    # STR: what spread of stats this system uses
        'acBase': 10,                   # INT: AC base 9 or 10, usually
        'acType': 'ascend',             # STR: 'ascend' or 'descend'
        'meleeMod': 'STR',              # STR: stat used to calc melee attack modifier
        'rangeMod': 'DEX',             # STR: stat used to calc ranged attack modifier
        'saves': False,                 # Pulls STR from Saves dict, above
        'hasWPs': False,                # BOO: notes if this system uses specific WPs a la Dark Dungeons
        'maxLvl': 10,                   # INT: maximum XP level in the game
        'races': False,
    },
    'bnt': {
        'name': 'bnt',
        'fullName': 'Blood & Treasure',
        'maxLvl': 20,
        'saves': saves['three'],
        'races': dict(dnd_races['bnt']),
    },
    'dd': {
        'name': 'dd',
        'fullName': 'Dark Dungeons',
        'acBase': 9,
        'acType': 'descend',
        'hasWPs': True,
        'maxLvl': 36,
        'saves': saves['five'],
    },
    'pla': {
        'name': 'pla',
        'fullName': 'Microlite Platinum',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'acBase': 4,
        'meleeMod': 'PRW',
        'rangeMod': 'PRW',
        'saves': saves['pla'],
        'maxLvl': 15,
    },
    'rbh': {
        'name': 'rbh',
        'fullName': 'Robot Hack',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'acBase': 4,
        'meleeMod': 'PRW',
        'rangeMod': 'PRW',
        'saves': saves['pla'],
        'maxLvl': 15,
    },
    'tnu': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'type': 'tnu',
        'hasHPs': False,
        'spread': statArrays['tnu'],
        'meleeMod': 'FER',
    },
}


def get_system_prefs(system='tnu'):
    sysprefs = dict(systems['default'])
    specific = dict(systems[system.lower()])
    sysprefs.update(specific)
    return sysprefs


if __name__ == "__main__":
    my_data = get_system_prefs('bnt')
    print(my_data)
