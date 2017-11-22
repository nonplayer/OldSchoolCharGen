"""
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use short instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
"""

import random

import dice
import equipment_osr
import equipment_tnu
import professions
import spells_osr
import spells_tnu
import systems

supported_systems = [
    'tnu', 'dd',
]


def gen_stats(spread, primes):
    stats = dice.get_spread(spread, primes)
    return stats


def gen_spells(gamesystem, prof, align, num):
    my_spells = []
    if gamesystem == 'tnu':
        my_spells = spells_tnu.get_spells(prof, align, num)
    elif gamesystem in ['bnt', 'dd', 'pla']:
        my_spells = spells_osr.get_spells(gamesystem, prof, num)
    return my_spells


# a quick spell printer for testing the TNU spell generator
def print_spells(prof, align, num):
    print_list = list(gen_spells(prof, align, num))
    print("\nMy Character's List of Spells:")
    print("------------------------------")
    for each in print_list:
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


def gen_ac(prefs, armour):
    ac_base = int(prefs['acBase'])
    ac_mod = 0
    if prefs['name'] == 'tnu':
        # no characters in TNU actually start with plate, thus its absence
        if any('Heavy Armour' in x for x in armour):
            ac_mod += 5
        elif any('Light Armour' in x for x in armour):
            ac_mod += 3
    elif prefs['name'] in ['bnt', 'dd']:
        if any('Plate Armour' in x for x in armour):
            ac_mod += 8
        elif any('Plate Mail' in x for x in armour):
            ac_mod += 7
        elif any('Splint Mail' in x for x in armour):
            ac_mod += 6
        elif any('Chain Mail' in x for x in armour):
            ac_mod += 5
        elif any('Scale Mail' in x for x in armour):
            ac_mod += 4
        elif any('Studded Leather' in x for x in armour):
            ac_mod += 3
        elif any('Leather Armour' in x for x in armour):
            ac_mod += 2
        elif any('Padded Armour' in x for x in armour):
            ac_mod += 1
    if prefs['name'] not in ['pla']:
        if any('a Tower Shield' in x for x in armour):
            ac_mod += 2
        elif any('a Shield' in x for x in armour):
            ac_mod += 1
    if prefs['acType'] == 'descend':
        ac_final = ac_base - ac_mod
    else:
        ac_final = ac_base + ac_mod
    return ac_final


def gen_melee():
    return


def gen_ranged():
    return


def generate(game_system='tnu'):
    DATA = {}
    # first let's load those system prefs - for later expansion
    if game_system not in supported_systems:
        game_system = 'tnu'
    prefs = dict(systems.get_system_prefs(game_system.upper()))
    DATA['system'] = prefs['fullName']
    # let's get that juicy character data!
    md = dict(professions.get_profession(game_system))  # my data
    # my_flags = list(md['flags'])
    # now let's break it out:
    DATA['short'] = md['short']
    DATA['long'] = md['long']
    DATA['lvl'] = int(md['level'])
    DATA['align'] = random.choice(md['alignAllowed'])
    primes = list(md['primAttr'])
    spread = list(prefs['spread'])
    statsD = dice.get_spread(spread, primes)
    DATA['stats'] = statsD
    # get stats average, for reasons:
    statsL = []
    for key, value in dict.items(statsD):
        statsL.append(int(value['val']))
    stats_avg = int(round(sum(statsL) / len(statsL)))
    # get more basic stuff:
    DATA['hd'] = md['hd']
    my_class = dict(gen_social(int(dice.roll(3, 6))))
    DATA['soc_class'] = my_class['title']
    DATA['soc_mod'] = str(my_class['mod'])
    if 'haspa' in md['flags']:
        DATA['pa'] = 'Yes'
    else:
        DATA['pa'] = 'None'
    # let's get that gear list:
    if prefs['type'] == 'tnu':
        my_gear = list(equipment_tnu.get_gear(DATA['short'], my_class['label']))
    elif prefs['type'] in ['dnd']:
        my_gear = list(equipment_osr.get_gear(md, prefs['name'], stats_avg))
    elif prefs['type'] == 'pla':
        my_gear = []
    else:
        my_gear = []
    if md['extragear']:
        for i in list(md['extragear']):
            my_gear.append(i)
    # pull out the weapons and armour into their own lists
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
    DATA['weapons'] = sorted(my_weaponlist)
    DATA['armour'] = sorted(my_armourlist)
    DATA['gear'] = sorted(my_gear)
    # now to generate the character's armour class
    DATA['ac'] = gen_ac(prefs, my_armourlist)
    if prefs['type'] is ['dnd']:
        if prefs['acType'] == 'descend':
            DATA['ac'] -= statsD['DEX']['mod']
        else:
            DATA['ac'] += statsD['DEX']['mod']
    # let's get those spells now:
    DATA['num_spells'] = 0
    if 'caster' in md['flags']:
        DATA['caster'] = True
        my_castmod = statsD[md['casterStat']]['mod']
        DATA['num_spells'] = DATA['lvl'] * md['spellsPerLvl'] + my_castmod
        if DATA['num_spells'] > 0:
            my_spells = list(gen_spells(prefs['name'], md['spellChooseAs'], DATA['align'], DATA['num_spells']))
            if md['extraspells']:
                for i in list(md['extraspells']):
                    my_spells.append(i)
            sorted(my_spells)
            DATA['spells'] = my_spells
    else:
        DATA['caster'] = False
    #print('\n\nOUTPUT TEST: My "DATA": ', DATA)
    return DATA


def print_character(system_name):
    system_name = system_name.lower()
    DATA = generate(system_name)
    print("\nA new random character for " + str(DATA['system']))
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
    print("Melee: " + "  Ranged: " + "  AC: " + str(DATA['ac']))
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
    print("")


if __name__ == "__main__":
    ## if run as-is, flagPrint "True" will enable screen print of character
    #print("\nThis is a random 1st-level Character Generator for old school RPGs.")
    #print("NOTICE: Currently only 'tnu' is supported, but additional systems are being planned.")
    #print("Which system would you like to use? Enter the number or acronym below:\n")
    #print(" [1] The Nightmares Underneath (tnu)")
    #selection = str(input("\nYour Selection: "))
    #if selection != '1' and selection != 'tnu':
    #    print("Selection invalid, defaulting to #1: The Nightmares Underneath.\n")
    #    system = 'tnu'
    #elif selection == '1':
    #    system = 'tnu'
    #else:
    #    system = selection
    #print_character(system)
    print_character('dd')
