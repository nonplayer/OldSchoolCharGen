'''
This file will be where I eventually expand the program to accommodate different games.
Right now, I'm just focusing on The Nightmares Underneath.
I'm sure there's got to be a better way to do this in a "pythonic" way, but I'm new, so this is my solution.

TNU = The Nightmares Underground
DD = Dark Dungeons (my first planned expansion, further down the road)
'''

systems ={
    'template': {
        'name': 'tmp',
        'fullName': 'Display Name',
        'hasHPs': True,     # changes the calculations if the system has hit points
    },
    'TNU': {
        'name': 'tnu',
        'fullName': 'The Nightmares Underneath',
        'hasHPs': False,
    },
    'DD': {
        'name': 'dd',
        'fullName': 'Dark Dungeons',
        'hasHPs': True,
    },
}

def get_system_prefs(sysName='TNU'):
    sysData = dict(systems[sysName.upper()])
    return sysData

if __name__ == "__main__":
    print(get_system_prefs('tnu'))
