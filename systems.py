'''
This file will be where I eventually expand the program to accommodate different games.
Right now, I'm just focusing on The Nightmares Underneath.
I'm sure there's got to be a better way to do this in a "pythonic" way, but I'm new, so this is my solution.

TNU = The Nightmares Underground
DD = Dark Dungeons (my first planned expansion, further down the road)
'''

statArrays = {
    'dnd': ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'],
    'dcc': ['', '', '', '', '', ''],
    'tnu': ['', '', '', '', '', ''],
    'pal': ['IQ', 'ME', 'MA', 'PS', 'PP', 'PE', 'PB', 'SPD'],
}

saves = {
    'one': [],
    'three': [],
    'five': [],
    'six': [],
}

systems ={
    'template': {
        'name': 'tmp',
        'fullName': 'Display Name',
        'hasHPs': True,     # BOOL: changes the calculations if the system has hit points
        'stats': 'tnu',
        'acBase': 10,       # INT: AC base 9 or 10, usually
        'acType': '',       # STR: 'ascend' or 'descend'
        'saves': '',        # STR: 'one', 'three', 'five', or 'six' (such as TBH, 3E, B/X, and 5E, respectively)
    },
    'TNU': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'hasHPs': False,
        'stats': 'tnu',
        'acBase': 10,
        'acType': 'ascend',
        'saves': 'six',
    },
    'DD': {
        'name': 'dd',
        'fullName': 'Dark Dungeons',
        'hasHPs': True,
        'stats': 'dnd',
        'acBase': 9,
        'acType': 'descend',
        'saves': 'five',
    },
}

def get_system_prefs(sysName='TNU'):
    sysData = dict(systems[sysName.upper()])
    return sysData

if __name__ == "__main__":
    print(get_system_prefs('tnu'))
