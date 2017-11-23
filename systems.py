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
            'traits': ['Humans are medium creatures with a base speed of 30 feet.',
                       'Humans enjoy a 10% bonus to all earned experience.',
                       'Humans receive a +1 bonus to all saving throws.',
                       'All humans speak Common and can learn any other language.'],
        },
        'dwarf': {
            'label': "Dwarf",
            'traits': [
                'Dwarves are medium creatures with a base speed of 20.',
                'Dwarves can see in the dark up to 60 feet via black and white "darkvision".',
                'Dwarves receive a +3 bonus on Fortitude saving throws vs poison.',
                'Dwarves receive a +3 bonus on Will saves against magic (Dwarf spellcasters lose this bonus).',
                'Dwarves have a knack for noticing unusual stonework and intuiting depth.',
                'Dwarves speak Common and Dwarven. They might also speak Gnome, Goblin, '
                'Kobold, Orc, Ogre, Hill Giant and Earth Elemental.',
                'Dwarves gain +1 attack vs goblins, hobgoblins and orcs.',
                'Dwarves gain +4 AC vs large humanoids like giants.'
            ],
        },
        'elf': {
            'label': "Elf",
            'traits': [
                'Elves are medium creatures with a base speed of 30 feet.',
                'Elves have darkvision to a range of 60 feet.',
                'Elves have a chance to find secret doors by passing within 5 feet.',
                'Elves receive a +1 bonus to hit with long and short bows, and long and short swords.',
                'Elves have 90% magic resistance to sleep spells and enchantment spells.',
                'Elves are immune to a ghoul\'s paralysis touch.',
                'Elves speak Common and Elven. They might also speak Gnoll, Gnome, Goblin, Orc, Sylvan and Dragon.'
            ],
        },
        'gnome': {
            'label': "Gnome",
            'traits': [
                'Gnomes are small creatures with a base speed of 20 feet.',
                'Gnomes have darkvision to a range of 60 feet.',
                'Gnomes have a knack for listening at doors.',
                'Gnomes with CHA of 10 or higher can cast the following spells, each once per day: '
                'Audible glamer, dancing lights and prestidigitation.',
                'Gnomes receive a +2 bonus on Will saving throws against illusions.',
                'Gnomes speak Common and Gnome. They might also speak Dwarf, Elf, Goblin, '
                'Hill Giant, Orc, Sylvan and the language of burrowing mammals.'
            ],
        },
        'halfelf': {
            'label': "Half-Elf",
            'traits': [
                'Half-elves are medium creatures with a base speed of 30 feet.',
                'Half-elves have darkvision to a range of 60 feet.',
                'Half-elves have 30% magic resistance to sleep and enchantment spells.',
                'Half-elves have a knack for trickery.',
                'Half-elves speak Common and Elven and can learn virtually any other language.'
            ],
        },
        'halforc': {
            'label': "Half-Orc",
            'traits': [
                'Half-orcs are medium creatures with a base speed of 30 feet.',
                'Half-orcs have darkvision to 60 feet.',
                'Half-orcs speak Common and Orc. They might also speak Gnoll, Goblin, Hill Giant, Ogre or Dragon.'
            ],
        },
        'halfling': {
            'label': "Halfling",
            'traits': [
                'Halflings are small creatures with a base speed of 20 feet.',
                'Halflings have darkvision to a range of 30 feet.',
                'Halflings enjoy a +1 bonus when attacking with slings and thrown weapons.',
                'Halflings have a knack for hiding, moving silently and getting into trouble.',
                'Halflings speak Common and Halfling. They might also speak '
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
