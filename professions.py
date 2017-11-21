'''
FLAGS:
note that some are one-or-the-other pairs
these are pulled together into a special new list during initial class generator
checks are made against that list "if word in list, then do sub-function" etc

(required)
base/optional   = designates what source material the class is from
human/demi      = are they human or demihuman

(optional)
caster          = designates the class as starting with magic
subclass        = has special subclass stuff, like with demihumans
xtragear        = has extra gear
xtraspells      = has bonus spells
haspa           = class has psychic armor

alignments options:
'chaos', 'evil', 'good', 'law', 'neutral'

"attacksAs" options:
best    = best bonuses in the game
mid     = mid-tier attack bonuses
worst   = worst bonuses in the game
none    = absolutely no level-based bonuses! to combat!
NOTE!: at least in base, TNU characters all use either best or none
'''

import random

tnu_profs = {
    'default': {
        'short': 'default',                         # STR: short name for frequent use in this code
        'long': 'Default Class Name',               # STR: Display Name
        'flags': [],                                    # LIST of flags for different effects
        'level': 1,                                     # INT: right now only used for # of spells mastered
        'hd': 8,                                        # INT: hit dice for calculations
        'primAttr': [],                                 # LIST of one or two stats for high stat roll assignments
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],    # LIST of allowed alignments for random choice
        'attacksAs': 'none',                            # STRING: what category fo combat bonuses
        'spellChooseAs': '',                            # STRING: if caster, usually = short
        'spellsPerLvl': 0,                              # INT: if caster, how many spell choices per level
        'casterStat': '',                               # STRING: stat used for spells, if a caster
        'skills': ['Placeholder for Skills'],           # Unsure, placeholder as I figure out skills. Might go unused.
        'restrictions': ['Placeholder for Restrictions'],   # Unsure, placeholder
        'special': ['Placeholder for Special Abilities'],   # Unsure, placeholder
        'extragear': [],                                # LIST: some professions have extra gear, put it here
    },
    'assassin' : {
        'short': 'assassin',
        'long': 'Assassin',
        'primAttr': ['DEX', 'FER'],
        'alignAllowed': ['chaos', 'evil', 'law', 'neutral'],
        'attacksAs': 'best',
    },
    'bard' : {
        'short': 'bard',
        'long': 'Bard',
        'flags': ['base', 'human', 'caster'],
        'hd': 6,
        'primAttr': ['CHA', 'HEA'],
        'alignAllowed': ['chaos', 'good', 'law', 'neutral'],
        'spellChooseAs': 'bard',
        'spellsPerLvl': 1,
        'casterStat': 'CHA',
    },
    'champ_chaos' : {
        'short': 'champ_chaos',
        'long': 'Champion of Chaos',
        'flags': ['base', 'human', 'caster', 'xtragear'],
        'primAttr': ['HEA', 'INT'],
        'alignAllowed': ['chaos'],
        'attacksAs': 'best',
        'spellChooseAs': 'champ_chaos',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'extragear': ['RANDOM_d6 doses of hallucinogenic cactus'],
    },
    'champ_evil' : {
        'short': 'champ_evil',
        'long': 'Champion of Evil',
        'flags': ['base', 'human', 'xtragear'],
        'primAttr': ['HEA', 'FER'],
        'alignAllowed': ['evil'],
        'attacksAs': 'best',
        'extragear': ['WEAPON: an additional close combat weapon from your special list'],
    },
    'champ_good' : {
        'short': 'champ_good',
        'long': 'Champion of Good',
        'flags': ['base', 'human', 'xtragear'],
        'primAttr': ['HEA', 'CHA'],
        'alignAllowed': ['good'],
        'attacksAs': 'best',
        'extragear': ['RANDOM_d6 doses of antitoxin', 'RANDOM_d6 uses of bandages'],
    },
    'champ_law' : {
        'short': 'champ_law',
        'long': 'Champion of Law',
        'flags': ['base', 'human', 'xtragear'],
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['law'],
        'attacksAs': 'best',
        'extragear': ['a written copy of The Law'],
    },
    'cultist' : {
        'short': 'cultist',
        'long': 'Cultist',
        'flags': ['base', 'human', 'caster'],
        'hd': 6,
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'attacksAs': 'best',
        'spellChooseAs': 'cultist',
        'spellsPerLvl': 2,
        'casterStat': 'WIL',
    },
    'fighter' : {
        'short': 'fighter',
        'long': 'Fighter',
        'primAttr': ['FER', 'HEA'],
        'attacksAs': 'best',
    },
    'scholar' : {
        'short': 'scholar',
        'long': 'Scholar',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'hd': 4,
        'primAttr': ['CHA', 'INT'],
        'alignAllowed': ['evil', 'good', 'law', 'neutral'],
        'spellChooseAs': 'scholar',
        'spellsPerLvl': 1,
        'casterStat': 'INT',
    },
    'thief' : {
        'short': 'thief',
        'long': 'Thief',
        'hd': 6,
        'primAttr': ['DEX'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
    },
    'wizard' : {
        'short': 'wizard',
        'long': 'Wizard',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'hd': 4,
        'primAttr': ['INT', 'WIL'],
        'spellChooseAs': 'wizard',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
    },
}


'''
fey_knight = {}
halfling = {}
berserker = {}
disciple = {}
'''


dd_profs = {
    'default': {
        'short': 'default',                             # STR: class name for references
        'long': 'Default Class name',                   # STR: class name for display
        'flags': ['base', 'human'],                     # LIST of flags for different effects
        'level': 1,                                     # INT: right now only used for # of spells mastered
        'nextXP': '2000',                               # STR: amount of XP needed for next level
        'hd': 6,                                        # INT: The Hit Die of the class
        'primAttr': [],                                 # LIST of one or two stats for high stat roll assignments
        'alignAllowed': ['chaos', 'law', 'neutral'],    # LIST of allowed alignments for random choice
        'attacksAs': 'mid',                             # STRING: what category of combat bonuses
        'wps': 2,                                       # INT: How many starting Weapon Proficiencies
        'weapons': 'all',                               # STR: Category of weapons allowed as choices
        'armour': 'all',                                # STR: Category of armours allowed as choices
        'spellChooseAs': '',                            # STRING: if caster, usually = short
        'spellsPerLvl': 0,                              # INT: if caster, how many spell choices per level
        'casterStat': '',                               # STRING: stat used for spells, if a caster
        'saves': [12, 13, 14, 15, 16],                  # LIST of 5 integers, in order
        'skills': ['Placeholder for Skills'],           # Unsure, placeholder as I figure out skills. Might go unused.
        'restrictions': ['Placeholder for Restrictions'],   # Unsure, placeholder
        'special': ['Placeholder for Special Abilities'],   # Unsure, placeholder
        'extragear': [],                                # LIST: some professions have extra gear, put it here
        'extraspells': [],                              # LIST: some magicians get free spells plus their choices
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster', 'xtragear'],
        'nextXP': '1500',
        'primAttr': ['WIS'],
        'weapons': 'cleric',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 0,
        'casterStat': 'WIS',
        'saves': [11, 12, 14, 16, 15],
        'extragear': ['a Holy Symbol'],
},
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'flags': ['base', 'demi'],
        'nextXP': '2200',
        'hd': 8,
        'primAttr': ['CON', 'STR'],
        'attacksAs': 'best',
        'wps': 4,
        'saves': [8, 9, 10, 13, 12],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'flags': ['base', 'demi', 'caster', 'xtragear'],
        'nextXP': '4000',
        'primAttr': ['STR', 'INT'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 0,
        'casterStat': 'INT',
        'saves': [12, 13, 13, 15, 15],
        'extragear': ['a Spellbook'],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'wps': 4,
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'CON'],
        'weapons': 'half',
        'saves': [8, 9, 10, 13, 12],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster', 'xtragear', 'xtraspells'],
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['INT'],
        'attacksAs': 'worst',
        'weapons': 'mu',
        'armour': 'mu',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 0,
        'casterStat': 'INT',
        'saves': [13, 14, 13, 16, 15],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
    },
    'mystic': {
        'short': 'mystic',
        'long': 'Mystic ',
        'primAttr': ['WIS', 'DEX'],
        'weapons': 'thief',
        'armour': 'thief',
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'flags': ['base', 'human', 'xtragear'],
        'nextXP': '1200',
        'hd': 4,
        'primAttr': ['DEX'],
        'weapons': 'thief',
        'armour': 'thief',
        'saves': [13, 14, 13, 16, 15],
        'extragear': ['a Set of Thieves\' Tools'],
    },
}


base_profs_tnu = [
    'assassin', 'bard', 'champ_chaos', 'champ_evil', 'champ_good', 'champ_law', 'cultist', 'fighter', 'scholar', 'thief', 'wizard'
]


proflists = {
    'dd': {
        'choices': ['cleric', 'fighter', 'mu', 'thief', 'elf', 'dwarf', 'halfling', 'mystic'],
        'dict': dd_profs,
    },
    'tnu': {
        'choices': ['assassin', 'bard', 'champ_chaos', 'champ_evil', 'champ_good', 'champ_law', 'cultist', 'fighter', 'scholar', 'thief', 'wizard'],
        'dict': tnu_profs,
    },
    'template': {
        'choices': [],
        'dict': '',
    },
}

'''
racial_profs = [fey_knight, halfling]
optional_profs = [berserker, disciple]
'''

'''
FOR NOW, this will only return the base classes. Once I add the extended classes, I'll
modify this to allow passing a selector.
'''


# this returns a random character profession and all its base data
def get_profession(system='tnu'):
    my_list = proflists[system]['choices']
    my_dict = proflists[system]['dict']
    prof_data = my_dict['default']
    prof_spec = my_dict[random.choice(my_list)]
    prof_data.update(prof_spec)
    return prof_data


def get_system_prefs(system='tnu'):
    sysprefs = dict(systems['default'])
    specific = dict(systems[system.lower()])
    sysprefs.update(specific)
    return sysprefs



'''
for key, value in dict.items(get_profession()):
    print(key, ":", value)
'''


if __name__ == "__main__":
    for key, value in dict.items((get_profession('dd'))):
        print(key, ":", value)
