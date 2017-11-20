'''
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use profShort instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
'''

import random

import dice
import equipment
import professions
import spells
import systems

supported_systems = [
    'TNU',
]


def gen_stats(spread, primes):
    system = system.upper()
    stats = dice.get_spread(spread, primes)
    return stats


def gen_spells(prof, align, num):
    my_spells = spells.get_spells(prof, align, num)
    return my_spells


# a quick spell printer for testing the TNU spell generator
def print_spells(prof, align, num):
    printList = list(gen_spells(prof, align, num))
    print("\nMy Character's List of Spells:")
    print("------------------------------")
    for each in printList:
        print(each)
    return


def gen_social(status):
    social = {'title': '', 'mod': 0, 'label': ''}
    if status == 18:
        social.update({'title': 'Royalty', 'mod': 3, 'label': 'royal'})
    elif status >= 16:
        social.update({'title': 'Greater Nobility', 'mod': 2, 'label': 'greater'})
    elif status >= 13:
        social.update({'title': 'Lesser Nobility', 'mod': 1, 'label': 'lesser'})
    elif status >= 9:
        social.update({'title': 'Middle Class', 'mod': 0, 'label': 'middle'})
    elif status >= 6:
        social.update({'title': 'Poor', 'mod': -1, 'label': 'poor'})
    elif status >= 4:
        social.update({'title': 'Peasantry', 'mod': -2, 'label': 'peasant'})
    else:
        social.update({'title': 'Scum', 'mod': -3, 'label': 'wretched'})
    return social


def generate(game_system='tnu'):
    DATA = {}
    # first let's load those system prefs - for later expansion
    if game_system not in supported_systems:
        game_system = 'TNU'
    sys_prefs = dict(systems.get_system_prefs(game_system.upper()))
    # let's get that juicy character data!
    md = dict(professions.get_profession())  # my data
    # my_flags = list(md['flags'])
    # now let's break it out:
    DATA['short'] = md['profShort']
    DATA['long'] = md['profLong']
    DATA['lvl'] = int(md['level'])
    DATA['align'] = random.choice(md['alignAllowed'])
    primes = list(md['primAttr'])
    spread = list(sys_prefs['spread'])
    my_stats = dice.get_spread(spread, primes)
    DATA['stats'] = my_stats
    # former method, kept for short-term posterity
    #for key, value in dict.items(my_stats):
    #    DATA[key.lower() + '_val'] = str(value['val'])
    #    DATA[key.lower() + '_mod'] = str(value['mod'])
    DATA['hd'] = md['hd']
    my_class = dict(gen_social(int(dice.roll(3, 6))))
    DATA['soc_class'] = my_class['title']
    DATA['soc_mod'] = str(my_class['mod'])
    if sys_prefs['hasHPs']:
        print("This System DOES have Hit Points!")
    if 'haspa' in md['flags']:
        DATA['pa'] = 'Yes'
    else:
        DATA['pa'] = 'None'
    # let's get that gear list:
    my_gear = list(equipment.get_gear(DATA['short'], my_class['label']))
    my_weapons = list(filter(lambda x: x.startswith('WEAPON: '), my_gear))
    my_armour = list(filter(lambda x: x.startswith('ARMOUR: '), my_gear))
    my_weaponlist = []
    my_armourlist = []
    for x in my_weapons:
        my_gear.remove(x)
        my_weaponlist.append(str.title(x[8:]))
    for x in my_armour:
        my_gear.remove(x)
        my_armourlist.append(str.title(x[8:]))
    DATA['weapons'] = my_weaponlist
    DATA['armour'] = my_armourlist
    DATA['gear'] = my_gear
    # let's get those spells now:
    DATA['num_spells'] = 0
    if 'caster' in md['flags']:
        DATA['caster'] = True
        my_castmod = my_stats[md['casterStat']]['mod']
        DATA['num_spells'] = DATA['lvl'] + my_castmod
        if DATA['num_spells'] > 0:
            my_spells = list(gen_spells(DATA['short'], DATA['align'], DATA['num_spells']))
            DATA['spells'] = my_spells
    else:
        DATA['caster'] = False
    # print('\n\nOUTPUT TEST: My "DATA": ', DATA)
    return DATA


def print_character(system):
    DATA = generate(system)
    # for local testing, print to debug:
    print("\nNOTICE: You are running in test mode, on-screen print is enabled")
    print("\nA new random character for " + str(DATA['long']))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    print("Profession: " + DATA['long'] + "; Level: " + str(DATA['lvl']) + "; Alignment:", DATA['align'].title())
    print("Hit Die: d" + str(DATA['hd']) + "; Psychic Armour: " + str(DATA['pa']) + "; Social Status: " + DATA['soc_class'] + "("+ str(DATA['soc_mod']) + ")" )
    print("---------------")
    print("\nAttribute Scores:")
    print("-----------------")
    for key, value in dict.items(DATA['stats']):
        print(key + ": " + str(value['val']) + ' (' + str(value['mod']) + ')')
    print("\nCombat Traits:")
    print("--------------")
    print("Melee: " + "  Ranged: " + "")
    print("\nMy Weapons:")
    print("-----------")
    for x in list(DATA['weapons']):
        print(x)
    print("\nMy Armour:")
    print("----------")
    for x in list(DATA['armour']):
        print(x)
    print("\nMy Gear:")
    print("--------")
    for x in list(DATA['gear']):
        print(x)
    if DATA['caster']:
        print("\nSpells Known:")
        print("-------------")
        if DATA['num_spells'] <= 0:
            print("I have no spells because I am the worst", DATA['long'], "ever!")
        else:
            for i in list(DATA['spells']):
                print(i)


if __name__ == "__main__":
    # if run as-is, flagPrint "True" will enable screen print of character
    print_character('tnu')
