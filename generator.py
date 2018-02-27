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


class Character(dict):
    def __init__(self, game_system, prefs, profession):
        super(Character, self).__init__()
        self['system'] = prefs['fullName']
        self['affects'] = dict(prefs['affects'])
        self['languages'] = prefs['langs']
        #
        # let's get that juicy character data and break it out!
        #
        self.load_profession_data(profession)
        primes = list(profession['primAttr'])
        spread = list(prefs['spread'])
        stats = dice.get_spread(spread, primes)
        self['stats'] = stats
        #
        # get stats average, for reasons:
        #
        # TODO: turn this into a list comp: sum([...]) / len(stats)
        stat_values = []
        for key, value in dict.items(stats):
            stat_values.append(int(value['val']))
        stats_avg = int(round(sum(stat_values) / len(stat_values)))
        #
        # get character race, if applicable:
        #
        if prefs['races']:
            my_race = random.choice(list(prefs['races']))
            self['race'] = prefs['races'][my_race]['label']
            self['traits'] = self['traits'] + prefs['races'][my_race]['traits']
            self['languages'] = self['languages'] + prefs['races'][my_race]['langs']
        elif profession['race']:
            self['race'] = profession['race']
        else:
            self['race'] = 'Human'
        #
        # get more basic stuff:
        #
        my_class = dict(gen_social(int(dice.roll(3, 6))))
        self['soc_class'] = my_class['title']
        self['soc_mod'] = str(my_class['mod'])
        if prefs['saves']:
            self['saves'] = gen_saves(prefs['saves'], profession['saves'])
        else:
            self['saves'] = False
        #
        # time for the combat data. Right now it's just level 1 hacking,
        # but I might update if I ever get around to multi-level generation
        # (but admittedly this is unlikely)
        #
        if game_system in ['dd']:
            combat_mod = 1
        elif profession['attacksAs'] in ['best', 'mid-hi']:
            combat_mod = 1
        else:
            combat_mod = 0
        self['melee'] = self['stats'][str(prefs['meleeMod'])]['mod'] + combat_mod
        self['range'] = self['stats'][str(prefs['rangeMod'])]['mod'] + combat_mod
        # and make them look pretty:
        if self['melee'] > 0:
            self['melee'] = str("+" + str(self['melee']))
        else:
            self['melee'] = str(self['melee'])
        if self['range'] > 0:
            self['range'] = str("+" + str(self['range']))
        else:
            self['range'] = str(self['range'])
        #
        # let's get that gear list:
        #
        if prefs['type'] == 'tnu':
            my_gear = list(equipment_tnu.get_gear(self['short'], my_class['label']))
        elif prefs['type'] in ['dnd']:
            my_gear = list(equipment_osr.get_gear(profession, prefs['name'], stats_avg))
        elif prefs['type'] == 'pla':
            my_gear = []
        else:
            my_gear = []
        if profession['extragear']:
            for i in list(profession['extragear']):
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
        self['weapons'] = sorted(my_weaponlist)
        self['armour'] = sorted(my_armourlist)
        self['gear'] = sorted(my_gear)
        #
        # now to generate the character's armour class
        #
        self['ac'] = gen_ac(prefs, my_armourlist)
        if prefs['type'] is ['dnd']:
            if prefs['acType'] == 'descend':
                self['ac'] -= stats['DEX']['mod']
            else:
                self['ac'] += stats['DEX']['mod']
        #
        # let's get those spells now:
        #
        self['num_spells'] = 0
        self['spells'] = []
        if 'caster' in profession['flags']:
            self['caster'] = True
            my_castmod = stats[profession['casterStat']]['mod']
            self['num_spells'] = self['lvl'] * profession['spellsPerLvl'] + my_castmod
            if profession['cantrips']:
                self['spells'] = list(
                    spells_osr.get_cantrips(prefs['name'], profession['spellChooseAs'], profession['cantrips']))
            if self['num_spells'] > 0:
                my_spells = list(
                    gen_spells(prefs['name'], profession['spellChooseAs'], self['align'], self['num_spells']))
                if profession['extraspells']:
                    for i in list(profession['extraspells']):
                        my_spells.append(i)
                sorted(my_spells)
                self['spells'] = my_spells + self['spells']
        else:
            self['caster'] = False

    def load_profession_data(self, profession):
        self['short'] = profession['short']
        self['long'] = profession['long']
        self['lvl'] = int(profession['level'])
        self['align'] = random.choice(profession['alignAllowed'])
        self['restrictions'] = list(profession['restrictions'])
        self['traits'] = list(profession['special'])
        self['personal'] = profession['personal']
        self['background'] = profession['background']
        self['age'] = profession['age']
        self['looks'] = profession['looks']
        self['hd'] = profession['hd']
        if 'haspa' in profession['flags']:
            self['pa'] = 'Yes'
        else:
            self['pa'] = 'None'
        #
        # next come the skills, if any:
        #
        if profession['skills']:
            self['skills'] = list(sorted(profession['skills']))
        else:
            self['skills'] = False


def generate(game_system='tnu'):
    #
    # first let's load those system prefs, to accommodate multiple game variants
    #
    prefs = dict(systems.get_system_prefs(game_system.upper()))
    profession = dict(professions.get_profession(game_system))

    character = Character(game_system, prefs, profession)

    return character




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
    print("\nRestrictions:")
    print("--------------------")
    for x in list(ch_data['restrictions']):
        print(x)
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
