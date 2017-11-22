"""
This file will be where I eventually expand the program to accommodate different games.
Right now, I'm just focusing on The Nightmares Underneath.
I'm sure there's got to be a better way to do this in a "pythonic" way, but I'm new, so this is my solution.

Systems Represented:
bnt = Blood & Treasure
dd = Dark Dungeons (my first planned expansion, further down the road)
dcc = Dungeon Crawl Classics
tnu = The Nightmares Underneath
plt = Microlite Platinum

Valid Types:
dnd = this game follows most basic D&D expectations
plt = this game derives from microlite platinum
tnu = the nightmares underneath (it really is pretty unique here...)

"""

statArrays = {
    'dnd': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    'dcc': ['STR', 'AGI', 'STA', 'PER', 'INT', 'LUC'],
    'tnu': ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL'],
    'pla': ['ICQ', 'MEE', 'MAF', 'PST', 'PRW', 'PND', 'PBT', 'RUN'],
}

saves = {
    'one': [],
    'three': ['Fortitude', 'Reflex', 'Willpower'],
    'five': ['Death Ray & Poison', 'Magic Wands', 'Paralysis & Petrification', 'Breath Weapon', 'Rod, Staff, & Spell'],
    'six': statArrays['dnd'],
    'pla': [],
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
        'saves': 'five',                # STR: 'one', 'three', 'five', or 'six' (as TBH, 3E, B/X, and 5E)
        'hasWPs': False,                # BOO: notes if this system uses specific WPs a la Dark Dungeons
        'maxLvl': 10,                   # INT: maximum XP level in the game
    },
    'bnt': {
        'name': 'bnt',
        'fullName': 'Blood & Treasure',
        'maxLvl': 20,
    },
    'dcc': {
        'name': 'dcc',
        'fullName': 'Dungeon Crawl Classics',
        'spread': statArrays['dcc'],
        'saves': 'three',
    },
    'dd': {
        'name': 'dd',
        'fullName': 'Dark Dungeons',
        'acBase': 9,
        'acType': 'descend',
        'hasWPs': True,
        'maxLvl': 36,
    },
    'pla': {
        'name': 'pla',
        'fullName': 'Microlite Platinum',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'acBase': 4,
        'saves': 'pla',
        'maxLvl': 15,
    },
    'rbh': {
        'name': 'rbh',
        'fullName': 'Robot Hack',
        'type': 'pla',
        'stats': 8,
        'spread': statArrays['pla'],
        'acBase': 4,
        'saves': 'pla',
        'maxLvl': 15,
    },
    'tnu': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'type': 'tnu',
        'hasHPs': False,
        'spread': statArrays['tnu'],
        'saves': None,
    },
}


def get_system_prefs(system='tnu'):
    sysprefs = dict(systems['default'])
    specific = dict(systems[system.lower()])
    sysprefs.update(specific)
    return sysprefs


if __name__ == "__main__":
    my_data = get_system_prefs('tnu')
    print(my_data)
    print(my_data['spread'])
    for i in list(my_data['spread']):
        print(i)
