"""
Systems Represented:
bnt = Blood & Treasure
dd = Dark Dungeons (my first planned expansion, further down the road)
m81 = Microlite81
tnu = The Nightmares Underneath
plt = Microlite Platinum

Valid Types:
dnd = this game follows most basic D&D expectations
plt = this game derives from microlite platinum
tnu = the nightmares underneath (it really is pretty unique here...)

Valid modRanges:
classic = the classic +3 to -3 D&D stat mod range
modern = (stat-10)/2, round down
slim = (stat-10)/3, round down
"""

statArrays = {
    'dnd': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    'm81': ['STR', 'DEX', 'MIND', 'CHA'],
    'tnu': ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL'],
    'pla': ['ICQ', 'MEE', 'MAF', 'PST', 'PRW', 'PND', 'PBT', 'RUN'],
}

statAffects = {
    'bnt': {
        'STR': 'Melee Attack rolls, Damage with Melee and Thrown',
        'INT': 'Known Languages, Mage Spells per day',
        'WIS': 'Will Saves, Cleric Spells per day',
        'DEX': 'Ranged Attacks, AC, Reflex Saves',
        'CON': 'Hit Point rolls, Fortitude Saves',
        'CHA': 'Leadership, Reaction rolls, Bard/Sorc Spells per day'
    },
    'dnd': {
        'STR': 'Melee Attack rolls, Damage with Melee and Thrown',
        'INT': '',
        'WIS': 'Saves vs Spells',
        'DEX': 'Ranged Attacks, AC, Initiative',
        'CON': 'Hit Point rolls',
        'CHA': 'Leadership, Reaction rolls'
    },
    'm81': {
        'STR': 'Melee Attack Rolls, Hit Point Rolls',
        'DEX': 'Missile Attack Rolls',
        'MIND': 'Magic Attack Rolls, Saves vs Charm/Illusion',
        'CHA': '???'
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

langs = [
    'Celestial (Law)', 'Dragon', 'Druidic', 'Dwarf', 'Elemental, Air', 'Elemental, Earth',
    'Elemental, Fire', 'Elemental, Water', 'Elf', 'Giant', 'Gnoll ', 'Gnome', 'Goblin',
    'Grimlock', 'Halfling', 'Infernal (Chaos)', 'Kobold', 'Manticore', 'Medusa', 'Naga',
    'Ogre', 'Ophidian', 'Orc', 'Sylvan',
]

dnd_races = {
    'bnt': {
        'human': {
            'label': "Human",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) 10% bonus to all earned experience.',
                '(Racial) +1 bonus to all saving throws.',
                ],
            'langs': [],
        },
        'dwarf': {
            'label': "Dwarf",
            'traits': [
                '(Racial) Medium size with a base speed of 20.',
                '(Racial) See in the dark up to 60 feet via black and white "darkvision".',
                '(Racial) +3 bonus on Fortitude saving throws vs poison.',
                '(Racial) +3 bonus on Will saves against magic (Dwarf spellcasters lose this bonus).',
                '(Racial) knack for noticing unusual stonework and intuiting depth.',
                '(Racial) +1 attack vs goblins, hobgoblins and orcs.',
                '(Racial) +4 AC vs large humanoids like giants.'
            ],
            'langs': ['Dwarven'],
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
            ],
            'langs': ['Elven'],
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
            ],
            'langs': ['Gnome'],
        },
        'halfelf': {
            'label': "Half-Elf",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to a range of 60 feet.',
                '(Racial) 30% magic resistance to sleep and enchantment spells.',
                '(Racial) Knack for trickery.',
            ],
            'langs': ['Elven'],
        },
        'halforc': {
            'label': "Half-Orc",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to 60 feet.',
            ],
            'langs': ['Orc'],
        },
        'halfling': {
            'label': "Halfling",
            'traits': [
                '(Racial) Small size with a base speed of 20 feet.',
                '(Racial) Darkvision to a range of 30 feet.',
                '(Racial) +1 bonus when attacking with slings and thrown weapons.',
                '(Racial) Knack for hiding, moving silently and getting into trouble.',
            ],
            'langs': ['Halfling'],
        },
    },
}


#
# Defaults are overridden by the system-specific alterations
#
systems = {
    'default': {
        'name': 'def',                  # shortname for the system, used in some lists and dicts
        'fullName': 'Default Display Name',
        'type': 'dnd',                  # STR: used to determine armor types, equipment lists, and AC assumptions
        'hasHPs': True,                 # BOO: changes the calculations if the system has hit points
        'stats': 6,                     # INT: how many stats in this system, usually 6
        'spread': statArrays['dnd'],    # DICT: what spread of stats this system uses
        'affects': statAffects['dnd'],  # DICT: reference of what each stat in the system affects during play
        'acBase': 10,                   # INT: AC base 9 or 10, usually
        'acType': 'ascend',             # STR: 'ascend' or 'descend'
        'meleeMod': 'STR',              # STR: stat used to calc melee attack modifier
        'missileMod': 'DEX',            # STR: stat used to calc ranged attack modifier
        'modRange': 'classic',          # STR: style of stat mods generated. classic = +3 to -3, modern = (stat-10)/2,
                                        #      slim = (stat-10)/3
        'HPsMod': 'CON',                # STR: stat used to calc hit point mods
        'saves': False,                 # Pulls STR from Saves dict, above
        'hasWPs': False,                # BOO: notes if this system uses specific WPs a la Dark Dungeons
        'maxLvl': 10,                   # INT: maximum XP level in the game
        'races': False,
        'langs': ['Common'],
    },
    'bnt': {
        'name': 'bnt',
        'fullName': 'Blood & Treasure',
        'affects': statAffects['bnt'],
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
    'm81': {
        'name': 'm81',
        'fullName': 'Microlite81',
        'type': 'dnd',
        'stats': 4,
        'spread': statArrays['m81'],
        'affects': statAffects['m81'],
        'modRange': 'slim',
        'HPsMod': 'STR',
        'saves': saves['five'],
        'hasWPs': True,
        'maxLvl': 14,
    },
    'pla': {
        'name': 'pla',
        'fullName': 'Microlite Platinum',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'affects': statAffects['pla'],
        'acBase': 4,
        'meleeMod': 'PRW',
        'missileMod': 'PRW',
        'modRange': 'modern',
        'HPsMod': 'PND',
        'saves': saves['pla'],
        'maxLvl': 15,
    },
    'rbh': {
        'name': 'rbh',
        'fullName': 'Robot Hack',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'affects': statAffects['pla'],
        'acBase': 4,
        'meleeMod': 'PRW',
        'missileMod': 'PRW',
        'modRange': 'modern',
        'saves': saves['pla'],
        'maxLvl': 15,
    },
    'tnu': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'type': 'tnu',
        'hasHPs': False,
        'spread': statArrays['tnu'],
        'affects': statAffects['tnu'],
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
