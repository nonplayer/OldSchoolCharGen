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
    'ham': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'SOC'],
    'm81': ['STR', 'DEX', 'MND', 'CHA'],
    'tnu': ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL'],
    'pla': ['ICQ', 'MEE', 'MAF', 'PST', 'PRW', 'PND', 'PBT', 'MOV'],
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
    'ddh': {
        'STR': 'Melee Attack rolls, Damage with Melee and Thrown',
        'INT': 'Bonus Skills/MU-Spells/Languages',
        'WIS': 'Saves vs Spells, Initiative',
        'DEX': 'Ranged Attacks, AC, Initiative',
        'CON': 'Hit Point rolls',
        'CHA': 'Leadership, Reaction rolls',
        'SOC': 'Social Reactions, Starting Money'
},
    'ham': {
        'STR': 'Melee Attack Rolls, Damage with Melee and Thrown',
        'DEX': 'Area Effect Saves, Missile Attack Rolls, AC, Initiative',
        'CON': 'Body Saves, Hit Die Rolls',
        'INT': 'Bonus Skills, Magic-User Spells',
        'WIS': 'Mind Saves, Cleric Spells, Initiative',
        'CHA': 'Luck Saves, Rally Saves',
        'SOC': 'Social Reactions, Starting Money'
    },
    'm81': {
        'STR': 'Melee Attack Rolls, Hit Point Rolls',
        'DEX': 'Missile Attack Rolls',
        'MND': 'Magic Attack Rolls, Saves vs Charm/Illusion',
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
    'one': {
        'names': ['Saving Throw'],
        'mods': ['None'],
    },
    'three': {
        'names': ['Fortitude', 'Reflex', 'Willpower'],
        'mods': ['CON', 'DEX', 'WIS'],
    },
    'six': {
        'names': list(statArrays['dnd']),
        'mods': list(statArrays['dnd']),
    },
    # note for classic I made it six, as spells tend to get weird separate bonuses
    'classic': {
        'names': ['Death Ray & Poison', 'Magic Wands', 'Paralysis & Petrification', 'Breath Weapon', 'Rod & Staff',
                  'Spell'],
        'mods': ['None', 'None', 'None', 'None', 'None', 'WIS'],
    },
    'ham': {
        'names': ['Area  (+DEX)', 'Body  (+CON)', 'Death (+nil)', 'Luck  (+CHA)', 'Mind  (+WIS)', 'Rally (+CHA)'],
        'mods': ['DEX', 'CON', 'None', 'CHA', 'WIS', 'CHA'],
    },
    'pla': {
        'names': ['Mind', 'Body', 'Reflex', 'Horror Factor (HF)'],
        'mods': ['MEE', 'PND', 'PRW', 'None', 'None'],
    },
}

languages_dnd = [
    'Celestial (Law)', 'Dragon', 'Drow', 'Druidic', 'Dwarf', 'Elemental, Air', 'Elemental, Earth',
    'Elemental, Fire', 'Elemental, Water', 'Elf', 'Giant', 'Gnoll', 'Gnome', 'Goblin',
    'Grimlock', 'Halfling', 'Infernal (Chaos)', 'Kobold', 'Manticore', 'Medusa', 'Naga',
    'Ogre', 'Ophidian', 'Orc', 'Sylvan',
]

languages_ham = [
    'Celestial (Law)', 'Dragon', 'Drow', 'Druidic', 'Drawf', 'Elemental, Air', 'Elemental, Earth',
    'Elemental, Fire', 'Elemental, Water', 'Elf', 'Giant', 'Gnoll', 'Gnome', 'Goblin',
    'Grimlock', 'Hobbert', 'Infernal (Chaos)', 'Kobold', 'Lupine', 'Manticore', 'Medusa', 'Naga',
    'Ogre', 'Ophidian', 'Orc', 'Sylvan',
]

languages_kaigaku = []

skills_bnt = [
    'Balance (DEX)', 'Bend bars (STR)', 'Break down doors (STR)', 'Climb sheer surfaces (STR)',
    'Decipher codes (INT)', 'Escape bonds (DEX)', 'Find secret doors (INT)', 'Find traps (INT)',
    'Hide in shadows (DEX)', 'Jump (STR)', 'Listen at doors (WIS)', 'Move silently (DEX)',
    'Open locks (DEX)', 'Pick pockets (DEX)', 'Remove traps (DEX)', 'Riding (DEX)', 'Survival (WIS)',
    'Swimming (STR)', 'Tracking (WIS)', 'Trickery (CHA)'
]

skills_dnd = [
    'Accounting (INT)', 'Agriculture (INT)', 'Animal Handling (INT)', 'Animal Training (INT)',
    'Appraising (INT)', 'Arcane Lore (INT)', 'Armorer (STR)', 'Artistic Ability (CHA)',
    'Astrology (WIS)', 'Balance (DEX)', 'Ballet (DEX)', 'Blacksmithing (STR)',
    'Bluff (CHA)', 'Bowyer/Fletcher (DEX)', 'Brewing (INT)', 'Butchery (DEX)',
    'Caber Tossing (STR)', 'Carpentry (STR)', 'Charioteering (DEX)', 'Cobbling (DEX)',
    'Cooking (WIS)', 'Dancing (DEX)', 'Diplomacy (CHA)', 'Direction Sense (WIS)',
    'Disguise (WIS)', 'Engineering (INT)', 'Escape Artist (DEX)', 'Etiquette (Choice of Culture) (CHA)',
    'Fire-building (DEX)', 'First Aid (WIS)', 'Fishing (WIS)', 'Forgery (DEX)',
    'Gambling (CHA)', 'Gaming (INT)', 'Gem-Cutting (DEX)', 'Geography (INT)',
    'Healing (INT)', 'Heraldry (INT)', 'Herbalism (INT)', 'History, Ancient (INT)',
    'History, Local (INT)', 'Hunting (WIS)', 'Intimidation (STR or CHA)', 'Juggling (DEX)',
    'Jumping (STR)', 'Laws (Choice of Culture) (INT)', 'Leatherworking (DEX)', 'Lip Reading (WIS)',
    'Magical Engineering (INT)', 'Mining (INT)', 'Mountaineering (WIS)', 'Musical Instrument (DEX)',
    'Nature Lore (INT)', 'Navigating (WIS)', 'Painting (DEX)', 'Performance (Choice of Medium) (CHA)',
    'Pottery (DEX)', 'Religious Lore (INT)', 'Riding (Choose Animal) (DEX)', 'Rope Use (DEX)',
    'Running (CON)', 'Seamanship (WIS)', 'Seamstress/Tailor (DEX)', 'Sense Motive (WIS)',
    'Set Snares (DEX)', 'Singing (CHA)', 'Stonemasonry (STR)', 'Survival (WIS)',
    'Swimming (STR)', 'Tanning (CON)', 'Tumbling (DEX)',
    'Ventriloquism (CHA)', 'Weaponsmithing (STR)', 'Weather Sense (WIS)', 'Weaving (DEX)',
]

race_choices = {
    'base': ['human', 'dwarf', 'elf', 'halfling', 'halfogre'],
    'bnt': ['human', 'dwarf', 'elf', 'gnome', 'halfling', 'halfelf', 'halforc'],
    'bntx': ['human', 'dwarf', 'elf', 'gnome', 'halfling', 'halfelf', 'halforc'],
}

race_data = {
    'base': {
        'default': {
            'label': "default",
            'traits': [],
            'core_languages': [],
            'mods': {},
            'stat_dice_numbs': 3,
            'stat_dice_sides': 6,
        },
        'human': {
            'label': "Human",
        },
        'clockwork': {
            'label': "Clockwork",
        },
        'drawf': {
            'label': "Drawf",
        },
        'dwarf': {
            'label': "Dwarf",
        },
        'elf': {
            'label': "Elf",
        },
        'halfling': {
            'label': "Halfling",
        },
        'halfogre': {
            'label': "Half-Ogre",
        },
        'hobbert': {
            'label': "Hobbert",
        },
        'lupine': {
            'label': "Lupine",
        },
    },
    'bnt': {
        'default': {
            'label': "default",
            'traits': [],
            'core_languages': [],
            'mods': {},
            'stat_rolls': 3,
            'stat_dice': 6,
        },
        'human': {
            'label': "Human",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) 10% bonus to all earned experience.',
                '(Racial) +1 bonus to all saving throws.',
                ],
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
        },
        'halforc': {
            'label': "Half-Orc",
            'traits': [
                '(Racial) Medium size with a base speed of 30 feet.',
                '(Racial) Darkvision to 60 feet.',
            ],
            'core_languages': ['Orc'],
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
        },
    },
    'bntx': {
        'aasimar': {
            'label': 'Aasimar',
            'traits': [
                '(RACE) Darkvision 60 feet, can cast daylight 1/day, and has resistance to electricity.',
                '(RACE) Can advance to 9th level in most classes, or unlimited in paladin.',
            ],
            'mods': {'WIS': 1, 'CHA': 1},
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
            'mods': {'STR': 1, 'CON': 1, 'WIS': -1, 'CHA': -1},
        },
        'azer': {
            'label': 'Azer',
            'traits': [
                '(RACE) Azer characters have darkvision to a range of 60 and retain all abilities of normal azer.',
                '(RACE) Can multi-class as cleric/fighters, fighter/magic-users and fighter/thieves. Can only'
                ' advance to 6th level max.',
            ],
            'core_languages': ['Elemental, Fire'],
            'mods': {'STR': 1, 'INT': 1, 'CHA': -2},
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
            'mods': {'INT': 1, 'CHA': 1},
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
            'mods': {'STR': -1, 'DEX': 1, 'CHA': -1},
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
            'mods': {'STR': -2, 'DEX': 1, 'CON': -1},
        },
    },
}


#
# Defaults are overridden by the system-specific alterations
#
systems = {
    # the default base assumptions for all new games is "new" DnD rules (3.x+) unless overwritten
    'default': {
        'system_name': 'def',           # shortname for the system, used in some lists and dicts
        'system_fullname': 'Default Display Name (DnD New)',
        'setting': 'fantasy',           # STR: game setting, for use with random setting-specific elements
        'hasHPs': True,                 # BOO: changes the calculations if the system has hit points
        'stats': 6,                     # INT: how many stats in this system, usually 6
        'method': 'standard',           # STR: how to get stats. standard = roll XdY, array = use roll_array values
        'roll_array': [8, 9, 10, 11, 12, 13],   # LIST of numbers to use for auto stats, in ascending order
        'spread': statArrays['dnd'],    # DICT: what spread of stats this system uses
        'affects': statAffects['dnd'],  # DICT: reference of what each stat in the system affects during play
        'acBase': 10,                   # INT: AC base 9 or 10, usually
        'acType': 'ascend',             # STR: 'ascend' or 'descend'
        'acSystem': 'dnd',              # STR: "dnd" = basic D&D armour rules. "pla" = platinum armour rules
        'meleeMod': 'STR',              # STR: stat used to calc melee attack modifier
        'missileMod': 'DEX',            # STR: stat used to calc ranged attack modifier
        'modRange': 'classic',          # STR: style of stat mods generated. classic = +3 to -3, modern = (stat-10)/2,
                                        #      slim = (stat-10)/3
        'HPsMod': 'CON',                # STR: stat used to calc hit point mods
        'saves': dict(saves['six']),    # Pulls STR from Saves dict, above
        'save_style': 'ascend',         # STR: do saves increase when leveling, or decrease? "ascend" or "descend"
        'hasWPs': False,                # BOO: notes if this system uses specific WPs a la Dark Dungeons
        'maxLvl': 20,                   # INT: maximum XP level in the game
        'race_choices': list(dict.keys(race_data['base'])),  # LIST: available choices for selectable races
        'race_data': dict(race_data['base']),   # DICT keyed to the list above
        'core_languages': ['Common'],   # LIST: Free starting languages for all characters
        'language_choices': languages_dnd,      # LIST of base possible bonus languages
        'bonus_langs': True,            # BOO: set False if system has no automatic bonus langs from stats
        'bonus_langs_stat': 'INT',      # STR only if bonus_langs is True
        'skill_choices': skills_dnd,    # LIST of skills for the random skill assigner
        'skills_mod': 'INT',            # STR all caps of stat used to modify starting skills
        'encumbrance': False,           # Does this system use Encumbrance, and if so, what style
    },
    # a fallback blank system for when adding new systems
    'def': {
        'saves': False,                 # def saves is False to make adding new systems less error-prone
    },
    # actual systems and inherited baselines below, alphabetically
    '5th': {
        'saves': False,                 # def saves is False to make adding new systems less error-prone
        'roll_array': [8, 10, 12, 13, 14, 15],
    },
    'dnd_old': {
        'system_name': 'dnd',
        'system_fullname': '"Old School" Dungeons and Dragons',
        'acBase': 9,
        'acType': 'descend',
        'saves': dict(saves['classic']),
        'save_style': 'descend',
        'hasWPs': False,
        'maxLvl': 10,
    },
    'bnt': {
        'system_name': 'bnt',
        'system_fullname': 'Blood & Treasure',
        'affects': statAffects['bnt'],
        'saves': saves['three'],
        'race_choices': list(dict.keys(race_data['bnt'])),
        'race_data': dict(race_data['bnt']),
        'skill_choices': skills_bnt,
    },
    'bntx': {
        'system_fullname': 'Blood & Treasure, Expanded',
        'system_baseline': 'bnt',
        'race_choices': list(dict.keys(race_data['bntx'])) + list(dict.keys(race_data['bnt'])),
        'race_data': {**dict(race_data['bntx']), **dict(race_data['bnt'])},
    },
    'dd': {
        'system_name': 'dd',
        'system_fullname': 'Dark Dungeons',
        'system_baseline': 'dnd_old',
        'hasWPs': True,
        'maxLvl': 36,
    },
    'ddh': {
        'system_name': 'ddh',
        'system_fullname': 'Dark Dungeons HAMMERED',
        'system_baseline': 'dnd_old',
        'race_data': dict(race_data['base']),   # DICT keyed to the list above
        'acSystem': 'dd',              # STR: "dnd" = basic D&D armour rules. "pla" = platinum armour rules
        'stats': 7,
        'spread': statArrays['ham'],
        'affects': statAffects['ddh'],
        'save_style': 'ascend',
        'language_choices': languages_ham,      # LIST of base possible bonus languages
        'hasWPs': True,
        'maxLvl': 36,
    },
    'ddx': {
        'system_name': 'ddx',
        'system_fullname': 'Dark Dungeons X',
        'system_baseline': 'dnd_old',
        'statRolls': 'ddx',
        'method': 'array',
        'roll_array': [9, 11, 12, 13, 14, 16],
        'save_style': 'ascend',
        'hasWPs': True,
        'maxLvl': 36,
    },
    'ham': {
        'system_name': 'ham',
        'system_fullname': 'HAMMERCRAWL!',
        'stats': 7,
        'spread': statArrays['ham'],
        'affects': statAffects['ham'],
        'saves': dict(saves['ham']),
        'maxLvl': 15,
        'encumbrance': 'ham',
    },
    'm81': {
        'system_name': 'm81',
        'system_fullname': 'Microlite81',
        'stats': 4,
        'spread': statArrays['m81'],
        'affects': statAffects['m81'],
        'modRange': 'slim',
        'HPsMod': 'STR',
        'saves': saves['one'],
        'hasWPs': True,
        'maxLvl': 14,
        'skills_mod': 'MND',
        'bonus_langs_stat': 'MND',
    },
    'pla': {
        'system_name': 'pla',
        'system_fullname': 'Microlite Platinum (WIP)',
        'stats': 8,
        'spread': statArrays['pla'],
        'affects': statAffects['pla'],
        'acBase': 4,
        'acSystem': 'pla',
        'meleeMod': 'PRW',
        'missileMod': 'PRW',
        'modRange': 'modern',
        'HPsMod': 'PND',
        'saves': False,
        'maxLvl': 15,
        'bonus_langs': False,
    },
    'rbh': {
        'system_name': 'rbh',
        'system_fullname': 'Robot Hack (WIP)',
        'system_baseline': 'pla',
    },
    'rpt': {
        'system_name': 'rpt',
        'system_fullname': 'Ruptures (WIP)',
        'system_baseline': 'pla',
    },
    'tnu': {
        'system_name': 'tnu',
        'system_fullname': 'The Nightmares Underneath',
        'hasHPs': False,
        'spread': statArrays['tnu'],
        'affects': statAffects['tnu'],
        'meleeMod': 'FER',
        'maxLvl': 10,
        'saves': False,
        'bonus_langs': False,
    },
}


def get_system_prefs(system='def'):
    if system not in list(dict.keys(systems)):
        system = 'def'
    sysprefs = dict(systems['default'])
    specific = dict(systems[system.lower()])
    if 'system_baseline' in list(dict.keys(specific)):
        baseline = dict(systems[str(specific['system_baseline'])])
        sysprefs.update(baseline)
    sysprefs.update(specific)
    return sysprefs


if __name__ == "__main__":
    my_data = get_system_prefs('dd')
    print(my_data)
