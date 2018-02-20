"""
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use short instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
"""

import random
import argparse

import dice
import equipment_osr
import equipment_tnu
import professions
import spells_osr
import spells_tnu
import systems

parser = argparse.ArgumentParser(description='Get Game System')
parser.add_argument('-g', '--game_system', type=str, required=True, choices=['bnt', 'dd', 'tnu'],
                    help='The abbreviated Game System (bnt, dd, tnu)')
parser.add_argument('-H', '--hammercrawl', action='store_true',
                    help='Enable HAMMERCRAWL! extended features (currently disabled)')
args = parser.parse_args()

supported_systems = [
    'tnu', 'dd', 'bnt'
]


def gen_stats(spread, primes):
    stats = dice.get_spread(spread, primes)
    return stats


def gen_saves(names, values):
    saves = dict(zip(names, values))
    return saves


def gen_spells(gamesystem, prof, align, num):
    my_spells = []
    if gamesystem == 'tnu':
        my_spells = spells_tnu.get_spells(prof, align, num)
    elif gamesystem in ['bnt', 'dd', 'pla']:
        my_spells = spells_osr.get_spells(gamesystem, prof, num)
    return my_spells


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
    elif prefs['type'] == 'dnd':
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


def generate(game_system='tnu'):
    DATA = {}
    #
    # first let's load those system prefs, to accommodate multiple game variants
    #
    if game_system not in supported_systems:
        game_system = 'tnu'
    prefs = dict(systems.get_system_prefs(game_system.upper()))
    DATA['system'] = prefs['fullName']
    #
    # let's get that juicy character data and break it out!
    #
    md = dict(professions.get_profession(game_system))  # my data
    DATA['short'] = md['short']
    DATA['long'] = md['long']
    DATA['lvl'] = int(md['level'])
    DATA['align'] = random.choice(md['alignAllowed'])
    primes = list(md['primAttr'])
    spread = list(prefs['spread'])
    stats_d = dice.get_spread(spread, primes)
    DATA['stats'] = stats_d
    DATA['traits'] = list(md['special'])
    DATA['personal'] = md['personal']
    DATA['background'] = md['background']
    DATA['age'] = md['age']
    DATA['looks'] = md['looks']
    #
    # get stats average, for reasons:
    #
    stats_l = []
    for key, value in dict.items(stats_d):
        stats_l.append(int(value['val']))
    stats_avg = int(round(sum(stats_l) / len(stats_l)))
    #
    # get character race, if applicable:
    #
    DATA['languages'] = prefs['langs']
    if prefs['races']:
        my_race = random.choice(list(prefs['races']))
        DATA['race'] = prefs['races'][my_race]['label']
        DATA['traits'] = DATA['traits'] + prefs['races'][my_race]['traits']
        DATA['languages'] = DATA['languages'] + prefs['races'][my_race]['langs']
    elif md['race']:
        DATA['race'] = md['race']
    else:
        DATA['race'] = 'Human'
    #
    # get more basic stuff:
    #
    DATA['hd'] = md['hd']
    my_class = dict(gen_social(int(dice.roll(3, 6))))
    DATA['soc_class'] = my_class['title']
    DATA['soc_mod'] = str(my_class['mod'])
    if 'haspa' in md['flags']:
        DATA['pa'] = 'Yes'
    else:
        DATA['pa'] = 'None'
    if prefs['saves']:
        DATA['saves'] = gen_saves(prefs['saves'], md['saves'])
    else:
        DATA['saves'] = False
    #
    # next come the skills, if any:
    #
    if md['skills']:
        DATA['skills'] = list(sorted(md['skills']))
    else:
        DATA['skills'] = False
    #
    # time for the combat data. Right now it's just level 1 hacking,
    # but I might update if I ever get around to multi-level generation
    # (but admittedly this is unlikely)
    #
    if game_system in ['dd']:
        combat_mod = 1
    elif md['attacksAs'] in ['best', 'mid-hi']:
        combat_mod = 1
    else:
        combat_mod = 0
    DATA['melee'] = DATA['stats'][str(prefs['meleeMod'])]['mod'] + combat_mod
    DATA['range'] = DATA['stats'][str(prefs['rangeMod'])]['mod'] + combat_mod
    # and make them look pretty:
    if DATA['melee'] > 0:
        DATA['melee'] = str("+" + str(DATA['melee']))
    else:
        DATA['melee'] = str(DATA['melee'])
    if DATA['range'] > 0:
        DATA['range'] = str("+" + str(DATA['range']))
    else:
        DATA['range'] = str(DATA['range'])
    #
    # let's get that gear list:
    #
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
    #
    # pull out the weapons and armour into their own lists
    #
    my_weapons = list(filter(lambda wep: wep.startswith('WEAPON: '), my_gear))
    my_armour = list(filter(lambda arm: arm.startswith('ARMOUR: '), my_gear))
    my_weaponlist = []
    my_armourlist = []
    for w in my_weapons:
        my_gear.remove(w)
        my_weaponlist.append(str.title(w[8:]))
    for a in my_armour:
        my_gear.remove(a)
        my_armourlist.append(str.title(a[8:]))
    DATA['weapons'] = sorted(my_weaponlist)
    DATA['armour'] = sorted(my_armourlist)
    DATA['gear'] = sorted(my_gear)
    #
    # now to generate the character's armour class
    #
    DATA['ac'] = gen_ac(prefs, my_armourlist)
    if prefs['type'] is ['dnd']:
        if prefs['acType'] == 'descend':
            DATA['ac'] -= stats_d['DEX']['mod']
        else:
            DATA['ac'] += stats_d['DEX']['mod']
    #
    # let's get those spells now:
    #
    DATA['num_spells'] = 0
    DATA['spells'] = []
    if 'caster' in md['flags']:
        DATA['caster'] = True
        my_castmod = stats_d[md['casterStat']]['mod']
        DATA['num_spells'] = DATA['lvl'] * md['spellsPerLvl'] + my_castmod
        if md['cantrips']:
            DATA['spells'] = list(spells_osr.get_cantrips(prefs['name'], md['spellChooseAs'], md['cantrips']))
        if DATA['num_spells'] > 0:
            my_spells = list(gen_spells(prefs['name'], md['spellChooseAs'], DATA['align'], DATA['num_spells']))
            if md['extraspells']:
                for i in list(md['extraspells']):
                    my_spells.append(i)
            sorted(my_spells)
            DATA['spells'] = my_spells + DATA['spells']
    else:
        DATA['caster'] = False
    return DATA


def print_character(system_name):
    system_name = system_name.lower()
    DATA = generate(system_name)
    print("\nA new random character for " + str(DATA['system']))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    print("Profession: %s;  Level: %s;  Race: %s" % (DATA['long'], str(DATA['lvl']), DATA['race']))
    print("Alignment: %s;  Age: %s;  Looks: %s" % (DATA['align'].title(), DATA['age'], DATA['looks']))
    print("Trait: %s;  Background: %s;  Social Status: %s (%s)" %
          (DATA['personal'], DATA['background'], DATA['soc_class'], str(DATA['soc_mod'])))
    print("Hit Die: d%s;  Psychic Armour: %s" % (str(DATA['hd']), str(DATA['pa'])))
    print("---------------")
    print("\nAttribute Scores:")
    print("-----------------")
    for key, value in dict.items(DATA['stats']):
        print("%s: %s (%s)" % (key, str(value['val']), str(value['mod'])))
    if DATA['saves']:
        print("\nSaving Throws:")
        print("--------------")
        for key, value in dict.items(DATA['saves']):
            print("%s: %s" % (key, str(value)))
    print("\nLanguages:")
    print("----------")
    for x in list(DATA['languages']):
        print(x)
    if DATA['skills']:
        print("\nSkills:")
        print("-------")
        for x in list(DATA['skills']):
            print(x)
    print("\nCombat Mods and Traits:")
    print("-----------------------")
    print("Melee: %s;  Ranged: %s;  AC: %s" % (str(DATA['melee']), str(DATA['range']), str(DATA['ac'])))
    print("\nTraits and Abilities:")
    print("--------------------")
    for x in list(DATA['traits']):
        print(x)
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
            print("I have no spells because I am the worst %s ever!" % DATA['long'])
        else:
            for i in list(DATA['spells']):
                print(i)
    print("")


if __name__ == "__main__":
    game_sys = args.game_system
    if args.hammercrawl:
        print("HAMMERCRAWL TIME!!!!! Okay this currently does nothing, but stay tuned for more...")
    while game_sys not in supported_systems:
        print("\nGame System choice is missing or invalid. Please enter one of the following systems:\n")
        print("bnt = Blood & Treasure (1st Edition)")
        print("dd  = Dark Dungeons")
        print("tnu = The Nightmares Underneath")
        print()
        game_sys = input("Enter the system abbreviation from above: ")
    print_character(game_sys)
