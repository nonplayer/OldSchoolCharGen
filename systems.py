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
        'HEA': 'Recovery Rolls, Saves vs Disease and Poison, Encumbrance Max (4 + Mod)',
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

languages_dnd = [
    'Celestial (Law)', 'Dragon', 'Drow', 'Druidic', 'Dwarf', 'Elemental, Air', 'Elemental, Earth',
    'Elemental, Fire', 'Elemental, Water', 'Elf', 'Giant', 'Gnoll ', 'Gnome', 'Goblin',
    'Grimlock', 'Halfling', 'Infernal (Chaos)', 'Kobold', 'Manticore', 'Medusa', 'Naga',
    'Ogre', 'Ophidian', 'Orc', 'Sylvan',
]

languages_kaigaku = []

race_choices = {
    'base': ['human', 'dwarf', 'elf', 'halfling'],
    'bnt': ['human', 'dwarf', 'elf', 'gnome', 'halfling', 'halfelf', 'halforc'],
    'bntx': ['human', 'dwarf', 'elf', 'gnome', 'halfling', 'halfelf', 'halforc'],
}

race_data = {
    'base': {
        'human': {
            'label': "Human",
            'traits': [],
            'core_languages': [],
            'mods': {},
        },
    },
    'bnt': {
        'human': {
            'label': "Human",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) 10% bonus to all earned experience.',
                '(Racial) +1 bonus to all saving throws.',
                ],
            'core_languages': [],
            'mods': {},
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
            'core_languages': ['Dwarven'],
            'mods': {},
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
            'core_languages': ['Elven'],
            'mods': {},
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
            'core_languages': ['Gnome'],
            'mods': {},
        },
        'halfelf': {
            'label': "Half-Elf",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to a range of 60 feet.',
                '(Racial) 30% magic resistance to sleep and enchantment spells.',
                '(Racial) Knack for trickery.',
            ],
            'core_languages': ['Elven'],
            'mods': {},
        },
        'halforc': {
            'label': "Half-Orc",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to 60 feet.',
            ],
            'core_languages': ['Orc'],
            'mods': {},
        },
        'halfling': {
            'label': "Halfling",
            'traits': [
                '(Racial) Small size with a base speed of 20 feet.',
                '(Racial) Darkvision to a range of 30 feet.',
                '(Racial) +1 bonus when attacking with slings and thrown weapons.',
                '(Racial) Knack for hiding, moving silently and getting into trouble.',
            ],
            'core_languages': ['Halfling'],
            'mods': {},
        },
    },
    'bntx': {
        'aasimar': {
            'label': 'Aasimar',
            'traits': [
                '(RACE) Darkvision 60 feet, can cast daylight 1/day, and has resistance to electricity.',
                '(RACE) Can advance to 9th level in most classes, or unlimited in paladin.',
            ],
            'core_languages': [],
            'mods': {'WIS': 1, 'CHA': 1,},
        },
        'automaton': {
            'label': 'Automaton',
            'traits': [
                '(RACE) Immune to poison and disease, no need to breathe or eat, but can drink magical potions.',
                '(RACE) Healing spells are only half effective on automatons; spells that repair damage to objects'
                ' act as cure wounds spells of an equivalent level.',
                '(RACE) Half damage from electricity, and have a natural armor class of 12.',
                '(RACE) Can advance to 8th level in any class. Can multi-class as cleric/fighters, fighter/magic-users'
                ' and fighter/thieves.',
            ],
            'core_languages': [],
            'mods': {'STR': 1, 'CON': 1, 'WIS': -1, 'CHA': -1,},
        },
        'azer': {
            'label': 'Azer',
            'traits': [
                '(RACE) Azer characters have darkvision to a range of 60 and retain all abilities of normal azer.',
                '(RACE) Can multi-class as cleric/fighters, fighter/magic-users and fighter/thieves. Can only'
                ' advance to 6th level max.',
            ],
            'core_languages': ['Elemental, Fire'],
            'mods': {'STR': 1, 'INT': 1, 'CHA': -2,},
        },
        'drow': {
            'label': 'Drow (Dark Elf)',
            'traits': [
                '(RACE) Darkvision 120 feet.',
                '(RACE) Drow characters retain drow monster abilities and vulnerabilities to bright light.',
                '(RACE) Female drow can multi-class as cleric/fighters, cleric/magic-users and cleric/thieves;'
                ' male drow can multi-class as fighter/magic-users and magic-user/thieves. Drow can only advance'
                ' up to 8th level.',
            ],
            'core_languages': ['Drow'],
            'mods': {'INT': 1, 'CHA': 1,},
        },
        'goblin': {
            'label': 'Goblin',
            'traits': [
                '(RACE) Land speed of 20 feet.',
                '(RACE) Darkvision 60 feet.',
                '(RACE) Knacks for: for moving silently, riding wolves/worgs.',
                '(RACE) Can multi-class as cleric/thieves, fighter/thieves and magic-user/ thieves.',
            ],
            'core_languages': ['Goblin'],
            'mods': {'STR': -1, 'DEX': 1, 'CHA': -1,},
        },
        'kobold': {
            'label': 'Kobold',
            'traits': [
                '(RACE) Small size creature, but with a standard speed of 30 ft.',
                '(RACE) Darkvision 120 feet; detect stonework as well as dwarves.',
                '(RACE) Scales give a natural +1 bonus to Armor Class.',
                '(RACE) Can multi-class as cleric/sorcerers, fighter/sorcerers and sorcerer/thieves.',
            ],
            'core_languages': ['Kobold'],
            'mods': {'STR': -2, 'DEX': 1, 'CON': -1,},
        },
    },
}


#
# Defaults are overridden by the system-specific alterations
#
systems = {
    'default': {
        'system_name': 'def',                  # shortname for the system, used in some lists and dicts
        'system_fullname': 'Default Display Name',
        'system_type': 'dnd',                  # STR: used to determine armor types, equipment lists, and AC assumptions
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
        'race_choices': list(dict.keys(race_data['base'])), # LIST: available choices for selecable races
        'race_data': dict(race_data['base']),   # DICT keyed to the list above
        'core_languages': ['Common'],   # LIST: Free starting languages for all characters
        'language_choices': languages_dnd,      # LIST of base possible bonus languages
    },
    'bnt': {
        'system_name': 'bnt',
        'system_fullname': 'Blood & Treasure',
        'affects': statAffects['bnt'],
        'maxLvl': 20,
        'saves': saves['three'],
        'race_choices': list(dict.keys(race_data['bnt'])),
        'race_data': dict(race_data['bnt']),
    },
    'bntx': {
        'system_name': 'bnt',
        'system_fullname': 'Blood & Treasure, Expanded',
        'affects': statAffects['bnt'],
        'maxLvl': 20,
        'saves': saves['three'],
        'race_choices': list(dict.keys(race_data['bntx'])) + list(dict.keys(race_data['bnt'])),
        'race_data': {**dict(race_data['bntx']), **dict(race_data['bnt']),},
    },
    'dd': {
        'system_name': 'dd',
        'system_fullname': 'Dark Dungeons',
        'acBase': 9,
        'acType': 'descend',
        'hasWPs': True,
        'maxLvl': 36,
        'saves': saves['five'],
    },
    'm81': {
        'system_name': 'm81',
        'system_fullname': 'Microlite81',
        'system_type': 'dnd',
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
        'system_name': 'pla',
        'system_fullname': 'Microlite Platinum',
        'system_type': 'pla',
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
        'system_name': 'rbh',
        'system_fullname': 'Robot Hack',
        'system_type': 'pla',
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
        'system_name': 'tnu',
        'system_fullname': 'The Nightmares Underneath',
        'system_type': 'tnu',
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
