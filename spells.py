import random
from random import choice as ch

'''
# TO call this function, it needs:
# prof shortname as a STRING
# alignment as a STRING
# number of allowed spells as an INT

# EXAMPLE:
get_spells('scholar', 'good', 3)

'''

# build the roll range lists for the schools
ALL = list(range(1, 101))
BAT = list(range(1, 11))
DIV = list(range(11, 21))
ENC = list(range(21, 31))
EVO = list(range(31, 41))
HEA = list(range(41, 51))
ILL = list(range(51, 61))
LAW = list(range(61, 71))
QUI = list(range(71, 81))
SUM = list(range(81, 91))
TRA = list(range(91, 101))

# valid spell rolls based on profession
spellValids = {
    'bard' : {
        'commons' : ALL,
        'alts' : DIV + ENC + HEA + ILL,  # special alternate list of choices
    },
    'champ_chaos' : {
        'commons' : list(range(1, 61)) + list(range(71, 101)),
        'alts' : list(range(1, 61)) + list(range(71, 101)),  # can't use law
    },
    'cultist' : {
        'commons' : ALL,
        'alts' : ALL,
    },
    'scholar' : {
        'commons' : ALL,  # only prof with alignment-based choices
        'alts' : ALL,
        'evil' : BAT,
        'good' : HEA,
        'law' : LAW,
    },
    'wizard' : {
        'commons' : ALL,
        'alts' : ALL,
    },
}

# here are all the spells!
spellsDict = {
    '1': 'Accurate Weapon (level 1)',
    '2': 'Blessing and Bane (level 3)',
    '3': 'Brutal Weapon (level 2)',
    '4': 'Eldritch Darts (level 1)',
    '5': 'Magic Weapon (level 2)',
    '6': 'Martial Inspiration (level 3)',
    '7': 'Protection from Missiles (level 4)',
    '8': 'Protection from Weapons (level 3)',
    '9': 'Vorpal Blessing (level 1)',
    '10': 'Wizard Sword (level 1)',
    '11': 'Clairaudience (level 3)',
    '12': 'Clairvoyance (level 4)',
    '13': 'Detect Evil (level 2)',
    '14': 'Detect Magic (level 1)',
    '15': 'Find Poison (level 1)',
    '16': 'Find Traps (level 2)',
    '17': 'Identify (level 3)',
    '18': 'Know Alignment (level 1)',
    '19': 'Locate Object (level 3)',
    '20': 'Sense Nightmares (level 1)',
    '21': 'Cause Fear (level 3)',
    '22': 'Charm Animals (level 2)',
    '23': 'Charm Monster (level 5)',
    '24': 'Charm Person (level 1)',
    '25': 'Confusion (level 4)',
    '26': 'Fearlessness (level 1)',
    '27': 'Inspiration (level 1)',
    '28': 'Paralysis (level 4)',
    '29': 'Sleep (level 1)',
    '30': 'Truth Telling (level 2)',
    '31': 'Acid Spray (level 3)',
    '32': 'Bridge (level 1)',
    '33': 'Chromatic Spray (level 2)',
    '34': 'Create Object (level 3)',
    '35': 'Floating Platform (level 1)',
    '36': 'Ghostly Hands (level 1)',
    '37': 'Light (level 1)',
    '38': 'Magic Missile (level 1)',
    '39': 'Magic Rope (level 4)',
    '40': 'Web Trap (level 2)',
    '41': 'Cure Disease (level 1)',
    '42': 'Cure Wound (level 3)',
    '43': 'Endure Pain (level 1)',
    '44': 'Indivisible (level 1)',
    '45': 'Negate Poison (level 1)',
    '46': 'Purify Food and Drink (level 2)',
    '47': 'Raise the Dead (level 8)',
    '48': 'Regenerate (level 5)',
    '49': 'Remove Curse (level 6)',
    '50': 'Second Wind (level 4)',
    '51': 'Detect Illusion (level 1)',
    '52': 'Duplicate Images (level 3)',
    '53': 'Faerie Dust (level 3)',
    '54': 'Fools\' Gold (level 2)',
    '55': 'Illusory Appearance (level 1)',
    '56': 'Illusory Being (level 5)',
    '57': 'Illusory Terrain (level 4)',
    '58': 'Invisibility (level 2)',
    '59': 'Message (level 1)',
    '60': 'Ventriloquism (level 1)',
    '61': 'Binding (level varies)',
    '62': 'Forlorn Encystment (level 9)',
    '63': 'Holy Water (level 1)',
    '64': 'Immobilize Animal (level 2)',
    '65': 'Immobilize Monster (level 4)',
    '66': 'Immobilize Person (level 3)',
    '67': 'The Power of Law (level 3)',
    '68': 'Protection from Chaos (level 2)',
    '69': 'Protection from Evil (level 1)',
    '70': 'Voice of Command (level 6)',
    '71': 'Arcane Connection (level varies)',
    '72': 'Contingency (level varies)',
    '73': 'Counterspell (level varies)',
    '74': 'Dispel Magic (level 3)',
    '75': 'Magic Resistance (level 6)',
    '76': 'Move Spell (level varies)',
    '77': 'Permanency (level 8)',
    '78': 'Spell Burn (level 1)',
    '79': 'Spell Extension (level 5)',
    '80': 'Transfer Spells (level 2)',
    '81': 'Conjuration (level 1)',
    '82': 'Create Food and Drink (level 1)',
    '83': 'Invisible Servant (level 3)',
    '84': 'Magic Steed (level 2)',
    '85': 'Minion (level 2)',
    '86': 'Summon Air Elemental (level 4)',
    '87': 'Summon Earth Elemental (level 2)',
    '88': 'Summon Fire Elemental (level 9)',
    '89': 'Summon Monster (level 1d8)',
    '90': 'Summon Water Elemental (level 5)',
    '91': 'Alter Items (level 2)',
    '92': 'Climbing (level 1)',
    '93': 'Colour Change (level 1)',
    '94': 'Enlarge (level 2)',
    '95': 'False Magnetism (level 3)',
    '96': 'Featherlight (level 1)',
    '97': 'Shapechange (level 5)',
    '98': 'Shrink (level 2)',
    '99': 'Transmute (level 7)',
    '100': 'Vulnerability (level varies)',
    }

'''
dict of only level 1 and "varies" spells, for later use if I need them:
    '1': 'Accurate Weapon (level 1)',
    '4': 'Eldritch Darts (level 1)',
    '9': 'Vorpal Blessing (level 1)',
    '10': 'Wizard Sword (level 1)',
    '14': 'Detect Magic (level 1)',
    '15': 'Find Poison (level 1)',
    '18': 'Know Alignment (level 1)',
    '20': 'Sense Nightmares (level 1)',
    '24': 'Charm Person (level 1)',
    '26': 'Fearlessness (level 1)',
    '27': 'Inspiration (level 1)',
    '29': 'Sleep (level 1)',
    '32': 'Bridge (level 1)',
    '35': 'Floating Platform (level 1)',
    '36': 'Ghostly Hands (level 1)',
    '37': 'Light (level 1)',
    '38': 'Magic Missile (level 1)',
    '41': 'Cure Disease (level 1)',
    '43': 'Endure Pain (level 1)',
    '44': 'Indivisible (level 1)',
    '45': 'Negate Poison (level 1)',
    '51': 'Detect Illusion (level 1)',
    '59': 'Message (level 1)',
    '60': 'Ventriloquism (level 1)',
    '61': 'Binding (level varies)',
    '63': 'Holy Water (level 1)',
    '69': 'Protection from Evil (level 1)',
    '71': 'Arcane Connection (level varies)',
    '72': 'Contingency (level varies)',
    '73': 'Counterspell (level varies)',
    '76': 'Move Spell (level varies)',
    '78': 'Spell Burn (level 1)',
    '81': 'Conjuration (level 1)',
    '82': 'Create Food and Drink (level 1)',
    '92': 'Climbing (level 1)',
    '93': 'Colour Change (level 1)',
    '96': 'Featherlight (level 1)',
    '100': 'Vulnerability (level varies)',
'''

# let's generate some spells!
def get_spells(prof, align, count):
    mySpells = []
    myRolls = spells_by_prof(prof, align, count)
    while set(myRolls).issubset(QUI):
        '''complete reroll if all four spells end up being from Quintessence school:'''
        myRolls = spells_by_prof(prof, align, count)
    for roll in myRolls:
        newSpell = spellsDict[str(roll)]
        mySpells.append(newSpell)
    return sorted(mySpells)

def spells_by_prof(prof, align, count):
    spellRolls = []
    #testCount = 0
    while len(spellRolls) < count:
        selectionA = spellValids[prof]['commons']
        if align in spellValids[prof]:
            '''some profs have alignment-based options:'''
            selectionB = spellValids[prof][align]
        else:
            selectionB = spellValids[prof]['alts']
        '''get the spell roll from either commons or special alternatives:'''
        spellRolls = list(set(random.sample(list(selectionA + selectionB), count)))
        #testCount += 1
        #print("This ran", testCount, "times")
    #print(len(spellRolls))
    return spellRolls


# test it out
def main():
    for each in get_spells('champ_chaos', 'evil', 1):
        print(each)

if __name__ == "__main__":
    main()
