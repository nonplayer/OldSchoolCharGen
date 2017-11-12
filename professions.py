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
}
'''

import random
from random import choice as ch

template = {
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
}

assassin = {
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
}

bard = {
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
}

champ_chaos = {
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
}

champ_evil = {
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
}

champ_good = {
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
}

champ_law = {
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
}

cultist = {
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
}

fighter = {
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
}

scholar = {
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
}

thief = {
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
}

wizard = {
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
}

'''
fey_knight = {}
halfling = {}
berserker = {}
disciple = {}
'''

base_profs = [
    assassin, bard, champ_chaos, champ_evil, champ_good, champ_law, cultist, fighter, scholar, thief, wizard
]

'''
racial_profs = [fey_knight, halfling]
optional_profs = [berserker, disciple]
'''

'''
FOR NOW, this will only return the base classes. Once I add the extended classes, I'll
modify this to allow passing a selector.
'''

def get_profession():
    profession = random.choice(base_profs)
    return profession

'''
for key, value in dict.items(get_profession()):
    print(key, ":", value)
'''

if __name__ == "__main__":
    for key, value in dict.items((get_profession())):
        print(key, ":", value)
