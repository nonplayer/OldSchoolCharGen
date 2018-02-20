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
        if any('A Tower Shield' in x for x in armour):
            ac_mod += 2
        elif any('A Shield' in x for x in armour):
            ac_mod += 1
    if prefs['acType'] == 'descend':
        ac_final = ac_base - ac_mod
    else:
        ac_final = ac_base + ac_mod
    return ac_final


def generate(game_system='tnu'):
    ch_data = {}
    #
    # first let's load those system prefs, to accommodate multiple game variants
    #
    if game_system not in supported_systems:
        game_system = 'tnu'
    prefs = dict(systems.get_system_prefs(game_system.upper()))
    ch_data['system'] = prefs['fullName']
    #
    # let's get that juicy character data and break it out!
    #
    md = dict(professions.get_profession(game_system))  # my data
    ch_data['short'] = md['short']
    ch_data['long'] = md['long']
    ch_data['lvl'] = int(md['level'])
    ch_data['align'] = random.choice(md['alignAllowed'])
    primes = list(md['primAttr'])
    spread = list(prefs['spread'])
    stats_d = dice.get_spread(spread, primes)
    ch_data['stats'] = stats_d
    ch_data['affects'] = dict(prefs['affects'])
    ch_data['traits'] = list(md['special'])
    ch_data['personal'] = md['personal']
    ch_data['background'] = md['background']
    ch_data['age'] = md['age']
    ch_data['looks'] = md['looks']
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
    ch_data['languages'] = prefs['langs']
    if prefs['races']:
        my_race = random.choice(list(prefs['races']))
        ch_data['race'] = prefs['races'][my_race]['label']
        ch_data['traits'] = ch_data['traits'] + prefs['races'][my_race]['traits']
        ch_data['languages'] = ch_data['languages'] + prefs['races'][my_race]['langs']
    elif md['race']:
        ch_data['race'] = md['race']
    else:
        ch_data['race'] = 'Human'
    #
    # get more basic stuff:
    #
    ch_data['hd'] = md['hd']
    my_class = dict(gen_social(int(dice.roll(3, 6))))
    ch_data['soc_class'] = my_class['title']
    ch_data['soc_mod'] = str(my_class['mod'])
    if 'haspa' in md['flags']:
        ch_data['pa'] = 'Yes'
    else:
        ch_data['pa'] = 'None'
    if prefs['saves']:
        ch_data['saves'] = gen_saves(prefs['saves'], md['saves'])
    else:
        ch_data['saves'] = False
    #
    # next come the skills, if any:
    #
    if md['skills']:
        ch_data['skills'] = list(sorted(md['skills']))
    else:
        ch_data['skills'] = False
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
    ch_data['melee'] = ch_data['stats'][str(prefs['meleeMod'])]['mod'] + combat_mod
    ch_data['range'] = ch_data['stats'][str(prefs['rangeMod'])]['mod'] + combat_mod
    # and make them look pretty:
    if ch_data['melee'] > 0:
        ch_data['melee'] = str("+" + str(ch_data['melee']))
    else:
        ch_data['melee'] = str(ch_data['melee'])
    if ch_data['range'] > 0:
        ch_data['range'] = str("+" + str(ch_data['range']))
    else:
        ch_data['range'] = str(ch_data['range'])
    #
    # let's get that gear list:
    #
    if prefs['type'] == 'tnu':
        my_gear = list(equipment_tnu.get_gear(ch_data['short'], my_class['label']))
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
    ch_data['weapons'] = sorted(my_weaponlist)
    ch_data['armour'] = sorted(my_armourlist)
    ch_data['gear'] = sorted(my_gear)
    #
    # now to generate the character's armour class
    #
    ch_data['ac'] = gen_ac(prefs, my_armourlist)
    if prefs['type'] is ['dnd']:
        if prefs['acType'] == 'descend':
            ch_data['ac'] -= stats_d['DEX']['mod']
        else:
            ch_data['ac'] += stats_d['DEX']['mod']
    #
    # let's get those spells now:
    #
    ch_data['num_spells'] = 0
    ch_data['spells'] = []
    if 'caster' in md['flags']:
        ch_data['caster'] = True
        my_castmod = stats_d[md['casterStat']]['mod']
        ch_data['num_spells'] = ch_data['lvl'] * md['spellsPerLvl'] + my_castmod
        if md['cantrips']:
            ch_data['spells'] = list(spells_osr.get_cantrips(prefs['name'], md['spellChooseAs'], md['cantrips']))
        if ch_data['num_spells'] > 0:
            my_spells = list(gen_spells(prefs['name'], md['spellChooseAs'], ch_data['align'], ch_data['num_spells']))
            if md['extraspells']:
                for i in list(md['extraspells']):
                    my_spells.append(i)
            sorted(my_spells)
            ch_data['spells'] = my_spells + ch_data['spells']
    else:
        ch_data['caster'] = False
    return ch_data


def print_character(system_name):
    system_name = system_name.lower()
    ch_data = generate(system_name)
    print("\nA new random character for " + str(ch_data['system']))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    print("Profession: %s;  Level: %s;  Race: %s" % (ch_data['long'], str(ch_data['lvl']), ch_data['race']))
    print("Alignment: %s;  Age: %s;  Looks: %s" % (ch_data['align'].title(), ch_data['age'], ch_data['looks']))
    print("Trait: %s;  Background: %s;  Social Status: %s (%s)" %
          (ch_data['personal'], ch_data['background'], ch_data['soc_class'], str(ch_data['soc_mod'])))
    print("Hit Die: d%s;  Psychic Armour: %s" % (str(ch_data['hd']), str(ch_data['pa'])))
    print("---------------")
    print("\nAttribute Scores:")
    print("-----------------")
    for key, value in dict.items(ch_data['stats']):
        print("%s: %s (%s): Affects %s" % (key, str(value['val']), str(value['mod']), str(ch_data['affects'][key])))
    if ch_data['saves']:
        print("\nSaving Throws:")
        print("--------------")
        for key, value in dict.items(ch_data['saves']):
            print("%s: %s" % (key, str(value)))
    print("\nLanguages:")
    print("----------")
    for x in list(ch_data['languages']):
        print(x)
    if ch_data['skills']:
        print("\nSkills:")
        print("-------")
        for x in list(ch_data['skills']):
            print(x)
    print("\nCombat Mods and Traits:")
    print("-----------------------")
    print("Melee: %s;  Ranged: %s;  AC: %s" % (str(ch_data['melee']), str(ch_data['range']), str(ch_data['ac'])))
    print("\nTraits and Abilities:")
    print("--------------------")
    for x in list(ch_data['traits']):
        print(x)
    print("\nMy Weapons:")
    print("-----------")
    for x in list(ch_data['weapons']):
        print(x)
    print("\nMy Armour:")
    print("----------")
    for x in list(ch_data['armour']):
        print(x)
    print("\nMy Gear:")
    print("--------")
    for x in list(ch_data['gear']):
        print(x)
    if ch_data['caster']:
        print("\nSpells Known:")
        print("-------------")
        if ch_data['num_spells'] <= 0:
            print("I have no spells because I am the worst %s ever!" % ch_data['long'])
        else:
            for i in list(ch_data['spells']):
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
