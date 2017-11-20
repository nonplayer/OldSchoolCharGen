'''
This file will be where I eventually expand the program to accommodate different games.
Right now, I'm just focusing on The Nightmares Underneath.
I'm sure there's got to be a better way to do this in a "pythonic" way, but I'm new, so this is my solution.

TNU = The Nightmares Underground
DD = Dark Dungeons (my first planned expansion, further down the road)
'''

statArrays = {
    'dnd': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    'dcc': ['STR', 'AGI', 'STA', 'PER', 'INT', 'LUC'],
    'tnu': ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL'],
    'par': ['ICQ', 'MEE', 'MAF', 'PST', 'PRW', 'PND', 'PBT', 'RUN'],
}

saves = {
    'one': [],
    'three': ['Fortitude', 'Reflex', 'Willpower'],
    'five': ['Death Ray & Poison', 'Magic Wands', 'Paralysis & Petrification', 'Breath Weapon', 'Rod, Staff, & Spell'],
    'six': statArrays['dnd'],
    'par': [],
}

systems = {
    'template': {
        'name': 'tmp',
        'fullName': 'Display Name',
        'hasHPs': True,     # BOOL: changes the calculations if the system has hit points
        'stats': 6,         # INT: how many stats in this system, usually 6
        'spread': 'tnu',    # STR: what spread of stats this system uses
        'acBase': 10,       # INT: AC base 9 or 10, usually
        'acType': '',       # STR: 'ascend' or 'descend'
        'saves': '',        # STR: 'one', 'three', 'five', or 'six' (such as TBH, 3E, B/X, and 5E, respectively)
    },
    'dcc': {
        'name': 'dcc',
        'fullName': 'Dungeon Crawl Classics',
        'hasHPs': True,
        'stats': 6,
        'spread': statArrays['dcc'],
        'acBase': 10,
        'acType': 'ascend',
        'saves': 'three',
    },
    'dd': {
        'name': 'dd',
        'fullName': 'Dark Dungeons',
        'hasHPs': True,
        'stats': 6,
        'spread': statArrays['dnd'],
        'acBase': 9,
        'acType': 'descend',
        'saves': 'five',
    },
    'par': {
        'name': 'par',
        'fullName': 'Pargraydeum Franstasy Gnoll-Praying Thing',
        'hasHPs': True,
        'stats': 8,
        'spread': statArrays['par'],
        'acBase': 0,
        'acType': 'ascend',
        'saves': 'par',
    },
    'tnu': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'hasHPs': False,
        'stats': 6,
        'spread': statArrays['tnu'],
        'acBase': 10,
        'acType': 'ascend',
        'saves': None,
    },
}


def get_system_prefs(system='tnu'):
    # until later expanded, use TNU only
    if system != 'tnu':
        system = 'tnu'
    sysprefs = dict(systems[system.lower()])
    return sysprefs


if __name__ == "__main__":
    my_data = get_system_prefs('tnu')
    print(my_data)
    print(my_data['spread'])
    for i in list(my_data['spread']):
        print(i)
