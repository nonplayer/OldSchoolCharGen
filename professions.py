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
haspa           = class has psychic armor
'''

'''
NOTE: Disciples and Berserkers are on the far out planning stages for now.


alignments options:
'chaos', 'evil', 'good', 'law', 'neutral'

"attacksAs" options:
best    = best bonuses in the game
mid     = mid-tier attack bonuses
worst   = worst bonuses in the game
none    = absolutely no level-based bonuses! to combat!
NOTE!: at least in base, TNU characters all use either best or none

prof_keys = {
    'profShort': '',        # STRING: short name for frequent use in this code
    'profLong': '',         # STRING: capital name for display
    'flags': [],            # LIST of flags for different effects
    'level': 1,             # INT: right now it defaults to 1, used for # of spells mastered
    'hd': 0,                # INT: hit dice for calculations
    'primAttr': [],         # LIST of one or two stats for high roll assignment, all caps like DEX, PER, etc
    'alignAllowed': [],     # LIST of allowed alignments for random choice
    'attacksAs': '',        # STRING: what category fo combat bonuses
    'spellChooseAs': '',    # STRING: if caster, what prof it chooses as, usually = profShort
    'spellsPerLvl': 1,      # INT: if caster, how many spell choices per level
    'casterStat': 'XYZ',    # STRING: stat used for spells, if a caster
    'skills': [],           # Unsure, placeholder as I figure out skills. Might go unused.
    'restrictions': [],     # Unsure, placeholder based on existing profession page details
    'special': [],          # Unsure, placeholder based on existing profession page details
    'extragear': [],        # LIST: some professions have extra gear, put it here
}
'''

import random

tnu_profs = {
    'template' : {
        'profShort': '',
        'profLong': '',
        'flags': ['', ''],
        'level': 1,
        'hd': 0,
        'primAttr': ['', ''],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],  # DO NOT FORGET TO CHANGE
        'attacksAs': 'none',
        'spellChooseAs': '',
        'spellsPerLvl': 0,
        'casterStat': 'XYZ',
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
        'extragear': [],  # DELETE if no extra gear
    },
    'assassin' : {
        'profShort': 'assassin',
        'profLong': 'Assassin',
        'flags': ['base', 'human'],
        'level': 1,
        'hd': 8,
        'primAttr': ['DEX', 'FER'],
        'alignAllowed': ['chaos', 'evil', 'law', 'neutral'],
        'attacksAs': 'best',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'bard' : {
        'profShort': 'bard',
        'profLong': 'Bard',
        'flags': ['base', 'human', 'caster'],
        'level': 1,
        'hd': 6,
        'primAttr': ['CHA', 'HEA'],
        'alignAllowed': ['chaos', 'good', 'law', 'neutral'],
        'attacksAs': 'none',
        'spellChooseAs': 'bard',
        'spellsPerLvl': 1,
        'casterStat': 'CHA',
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'champ_chaos' : {
        'profShort': 'champ_chaos',
        'profLong': 'Champion of Chaos',
        'flags': ['base', 'human', 'caster', 'xtragear'],
        'level': 1,
        'hd': 8,
        'primAttr': ['HEA', 'INT'],
        'alignAllowed': ['chaos'],
        'attacksAs': 'best',
        'spellChooseAs': 'champ_chaos',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
        'extragear': ['RANDOM_d6 doses of hallucinogenic cactus'],
    },
    'champ_evil' : {
        'profShort': 'champ_evil',
        'profLong': 'Champion of Evil',
        'flags': ['base', 'human', 'xtragear'],
        'level': 1,
        'hd': 8,
        'primAttr': ['HEA', 'FER'],
        'alignAllowed': ['evil'],
        'attacksAs': 'best',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
        'extragear': ['WEAPON: an additional close combat weapon from your special list'],
    },
    'champ_good' : {
        'profShort': 'champ_good',
        'profLong': 'Champion of Good',
        'flags': ['base', 'human', 'xtragear'],
        'level': 1,
        'hd': 8,
        'primAttr': ['HEA', 'CHA'],
        'alignAllowed': ['good'],
        'attacksAs': 'best',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
        'extragear': ['RANDOM_d6 doses of antitoxin', 'RANDOM_d6 uses of bandages'],
    },
    'champ_law' : {
        'profShort': 'champ_law',
        'profLong': 'Champion of Law',
        'flags': ['base', 'human', 'xtragear'],
        'level': 1,
        'hd': 8,
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['law'],
        'attacksAs': 'best',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
        'extragear': ['a written copy of The Law'],
    },
    'cultist' : {
        'profShort': 'cultist',
        'profLong': 'Cultist',
        'flags': ['base', 'human', 'caster'],
        'level': 1,
        'hd': 6,
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'attacksAs': 'best',
        'spellChooseAs': 'cultist',
        'spellsPerLvl': 2,
        'casterStat': 'WIL',
        'skills': ['Religious Practices,' 'Cult Doctrine', 'Your Chosen Specialty'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'fighter' : {
        'profShort': 'fighter',
        'profLong': 'Fighter',
        'flags': ['base', 'human'],
        'level': 1,
        'hd': 8,
        'primAttr': ['FER', 'HEA'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'attacksAs': 'best',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'scholar' : {
        'profShort': 'scholar',
        'profLong': 'Scholar',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'level': 1,
        'hd': 4,
        'primAttr': ['CHA', 'INT'],
        'alignAllowed': ['evil', 'good', 'law', 'neutral'],
        'attacksAs': 'none',
        'spellChooseAs': 'scholar',
        'spellsPerLvl': 1,
        'casterStat': 'INT',
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'thief' : {
        'profShort': 'thief',
        'profLong': 'Thief',
        'flags': ['base', 'human'],
        'level': 1,
        'hd': 6,
        'primAttr': ['DEX'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'attacksAs': 'none',
        'spellChooseAs': None,
        'spellsPerLvl': 0,
        'casterStat': None,
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
    'wizard' : {
        'profShort': 'wizard',
        'profLong': 'Wizard',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'level': 1,
        'hd': 4,
        'primAttr': ['INT', 'WIL'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'attacksAs': 'none',
        'spellChooseAs': '',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'skills': ['Placeholder text for Class Skills'],
        'restrictions': ['Placeholder text for Class Restrictions'],
        'special': ['Placeholder text for Class Special Abilities'],
    },
}


'''
fey_knight = {}
halfling = {}
berserker = {}
disciple = {}
'''


dd_profs = {
    'template': {
        'short': 'cleric',      # STR: class name for references
        'long': 'Cleric',       # STR: class name for display
        'wps': 2,               # INT: How many starting Weapon Proficiencies
        'weapons': 'all',       # STR: Category of weapons allowed as choices
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'wps': 2,
        'weapons': 'cleric',
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'wps': 4,
        'weapons': 'all',
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'wps': 2,
        'weapons': 'mu',
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'wps': 2,
        'weapons': 'thief',
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'wps': 2,
        'weapons': 'all',
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'wps': 4,
        'weapons': 'all',
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'wps': 2,
        'weapons': 'half',
    },
}


base_profs_tnu = [
    'assassin', 'bard', 'champ_chaos', 'champ_evil', 'champ_good', 'champ_law', 'cultist', 'fighter', 'scholar', 'thief', 'wizard'
]


proflists = {
    'dd': {
        'choices': ['cleric', 'fighter', 'magic-user', 'thief', 'elf', 'dwarf', 'halfling'],
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


def get_profession(system):
    my_list = proflists[system]['choices']
    my_dict = proflists[system]['dict']
    prof_data = my_dict[random.choice(my_list)]
    return prof_data


'''
for key, value in dict.items(get_profession()):
    print(key, ":", value)
'''


if __name__ == "__main__":
    for key, value in dict.items((get_profession('tnu'))):
        print(key, ":", value)
