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
parser.add_argument('-g', '--game_system', type=str, required=True, choices=['bnt', 'dd', 'm81', 'tnu'],
                    help='The abbreviated Game System (bnt, dd, m81, tnu)')
parser.add_argument('-H', '--hammercrawl', action='store_true',
                    help='Enable HAMMERCRAWL! extended features (currently disabled)')
parser.add_argument('-n', '--number_of_characters', type=int, action='store', default=1,
                    help='How many character to generate.')
args = parser.parse_args()

supported_systems = [
    'tnu', 'dd', 'bnt', 'm81',
]


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
    if prefs['system_name'] == 'tnu':
        # no characters in TNU actually start with plate, thus its absence
        if any('Heavy Armour' in x for x in armour):
            ac_mod += 5
        elif any('Light Armour' in x for x in armour):
            ac_mod += 3
    elif prefs['system_type'] == 'dnd':
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
    if prefs['system_name'] not in ['pla']:
        if any('A Tower Shield' in x for x in armour):
            ac_mod += 2
        elif any('A Shield' in x for x in armour):
            ac_mod += 1
    if prefs['acType'] == 'descend':
        ac_final = ac_base - ac_mod
    else:
        ac_final = ac_base + ac_mod
    return ac_final


class Character(object):
    def __init__(self, game_system, prefs):
        self.prefs = prefs
        self.profession = dict(professions.get_profession(game_system))

        super(Character, self).__init__()

        self.load_prefs_data()
        #
        # let's get that juicy character data and break it out!
        self.load_profession_data()
        self.init_race_and_languages()
        primes = list(self.profession['primAttr'])
        spread = list(self.prefs['spread'])
        stats = dice.get_spread(spread, primes, self.prefs['modRange'])
        self.stats = stats
        #
        # get stats average, for reasons:
        # TODO: turn this into a list comp: sum([...]) / len(stats)
        stat_values = []
        for key, value in dict.items(stats):
            stat_values.append(int(value['val']))
        stats_avg = int(round(sum(stat_values) / len(stat_values)))
        #
        # get more basic stuff:
        self.init_bonus_languages()
        my_class = dict(gen_social(int(dice.roll(3, 6))))
        self.soc_class = my_class['title']
        self.soc_mod = str(my_class['mod'])
        if self.prefs['saves']:
            self.saves = dict(zip(self.prefs['saves'], self.profession['saves']))
        else:
            self.saves = {}
        #
        # let's get that gear list:
        self.init_combat(game_system)
        #
        # let's get that gear list:
        if self.system_type == 'tnu':
            my_gear = list(equipment_tnu.get_gear(self.short, my_class['label']))
        elif self.system_type in ['dnd']:
            my_gear = list(equipment_osr.get_gear(self.profession, self.system, stats_avg))
        elif self.system_type == 'pla':
            my_gear = []
        else:
            my_gear = []
        if self.profession['extragear']:
            for i in list(self.profession['extragear']):
                my_gear.append(i)
        #
        # pull out the weapons and armour into their own lists
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
        self.weapons = sorted(my_weaponlist)
        self.armour = sorted(my_armourlist)
        self.gear = sorted(my_gear)
        #
        # now to generate the character's armour class
        self.ac = gen_ac(self.prefs, my_armourlist)
        if self.system_type is ['dnd']:
            if self.prefs['acType'] == 'descend':
                self.ac -= stats['DEX']['mod']
            else:
                self.ac += stats['DEX']['mod']
        self.init_magic()

    def init_magic(self):
        #
        # let's get those spells now:
        self.num_spells = 0
        self.spells = []
        if 'caster' in self.profession['flags']:
            self.caster = True
            my_castmod = self.stats[self.profession['casterStat']]['mod']
            self.num_spells = self.lvl * self.profession['spellsPerLvl'] + my_castmod
            if self.profession['cantrips']:
                self.spells = list(
                    spells_osr.get_cantrips(self.system, self.profession['spellChooseAs'],
                                            self.profession['cantrips']))
            if self.num_spells > 0:
                my_spells = []
                if self.system == 'tnu':
                    my_spells = spells_tnu.get_spells(self.profession['spellChooseAs'], self.align, self.num_spells)
                elif self.system in ['bnt', 'dd', 'pla']:
                    my_spells = spells_osr.get_spells(self.system, self.profession['spellChooseAs'], self.num_spells)
                if self.profession['extraspells']:
                    for i in list(self.profession['extraspells']):
                        my_spells.append(i)
                sorted(my_spells)
                self.spells = my_spells + self.spells
        else:
            self.caster = False

    def init_combat(self, game_system):
        # time for the combat data. Right now it's just level 1 hacking,
        # but I might update if I ever get around to multi-level generation
        # (but admittedly this is unlikely)
        #
        if game_system in ['dd']:
            combat_mod = 1
        elif self.profession['attacksAs'] in ['best', 'mid-hi']:
            combat_mod = 1
        else:
            combat_mod = 0
        self.melee = self.stats[str(self.prefs['meleeMod'])]['mod'] + combat_mod
        self.range = self.stats[str(self.prefs['missileMod'])]['mod'] + combat_mod
        # and make them look pretty:
        if self.melee > 0:
            self.melee = str("+" + str(self.melee))
        else:
            self.melee = str(self.melee)
        if self.range > 0:
            self.range = str("+" + str(self.range))
        else:
            self.range = str(self.range)

    def init_race_and_languages(self):
        if self.profession['race'] == 'RANDOM':
            my_race = random.choice(list(self.prefs['race_choices']))
            self.race = self.prefs['race_data'][my_race]['label']
            self.traits = self.traits + self.prefs['race_data'][my_race]['traits']
            self.languages = self.prefs['race_data'][my_race]['core_languages']
        else:
            self.race = self.profession['race']
            self.languages = []

    def load_prefs_data(self):
        self.system = self.prefs['system_name']
        self.system_fullname = self.prefs['system_fullname']
        self.system_type = self.prefs['system_type']
        self.affects = dict(self.prefs['affects'])

    def init_bonus_languages(self):
        self.languages = self.languages + self.prefs[ 'core_languages' ] + self.profession[ 'extralangs' ]
        new_languages = self.prefs[ 'language_choices' ]
        for i in self.languages:
            if i in new_languages:
                new_languages.remove(i)
        if self.system in ['m81']:
            bonus_lang_choices = self.stats['MIND']['mod']
        elif self.system_type == 'dnd':
            bonus_lang_choices = self.stats['INT']['mod']
        else:
            bonus_lang_choices = 0
        if bonus_lang_choices > 0:
            while bonus_lang_choices > 0:
                newlang = random.choice(new_languages)
                new_languages.remove(newlang)
                bonus_lang_choices -= 1
                self.languages.append(newlang)

    def load_profession_data(self):
        self.short = self.profession['short']
        self.long = self.profession['long']
        self.lvl = int(self.profession['level'])
        self.align = random.choice(self.profession['alignAllowed'])
        self.restrictions = list(self.profession['restrictions'])
        self.traits = list(self.profession['special'])
        self.personal = self.profession['personal']
        self.background = self.profession['background']
        self.age = self.profession['age']
        self.looks = self.profession['looks']
        self.hd = self.profession['hd']
        if 'haspa' in self.profession['flags']:
            self.pa = 'Yes'
        else:
            self.pa = 'None'
        #
        # next come the skills, if any:
        if self.profession['skills']:
            self.skills = list(sorted(self.profession['skills']))
        else:
            self.skills = []


def generate(game_system='tnu'):
    #
    # first let's load those system prefs, to accommodate multiple game variants
    prefs = dict(systems.get_system_prefs(game_system.upper()))

    return Character(game_system, prefs)


def print_character(game_system):
    game_system = game_system.lower()
    character = generate(game_system)
    print("\nA new random character for " + str(character.system_fullname))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    print("Profession: %s;  Level: %s;  Race: %s" % (character.long, str(character.lvl), character.race))
    print("Alignment: %s;  Age: %s;  Looks: %s" % (character.align.title(), character.age, character.looks))
    print("Trait: %s;  Background: %s;  Social Status: %s (%s)" %
          (character.personal, character.background, character.soc_class, str(character.soc_mod)))
    print("Hit Die: d%s;  Psychic Armour: %s" % (str(character.hd), str(character.pa)))
    print("---------------")
    print("\nAttribute Scores:")
    print("-----------------")
    for key, value in dict.items(character.stats):
        print("%s: %s (%s): Affects %s" % (key, str(value['val']), str(value['mod']), str(character.affects[key])))
    if character.saves:
        print("\nSaving Throws:")
        print("--------------")
        for key, value in dict.items(character.saves):
            print("%s: %s" % (key, str(value)))
    print("\nLanguages:")
    print("----------")
    for x in list(character.languages):
        print(x)
    if character.skills:
        print("\nSkills:")
        print("-------")
        for x in list(character.skills):
            print(x)
    print("\nCombat Mods and Traits:")
    print("-----------------------")
    print("Melee: %s;  Ranged: %s;  AC: %s" % (str(character.melee), str(character.range), str(character.ac)))
    print("\nRestrictions:")
    print("--------------------")
    for x in list(character.restrictions):
        print(x)
    print("\nTraits and Abilities:")
    print("--------------------")
    for x in list(character.traits):
        print(x)
    print("\nMy Weapons:")
    print("-----------")
    for x in list(character.weapons):
        print(x)
    print("\nMy Armour:")
    print("----------")
    for x in list(character.armour):
        print(x)
    print("\nMy Gear:")
    print("--------")
    for x in list(character.gear):
        print(x)
    if character.caster:
        print("\nSpells Known:")
        print("-------------")
        if character.num_spells <= 0:
            print("I have no spells because I am the worst %s ever!" % character.long)
        else:
            for i in list(character.spells):
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
        print("m81 = Microlite81")
        print("tnu = The Nightmares Underneath")
        print()
        game_sys = input("Enter the system abbreviation from above: ")
    for i in range(args.number_of_characters):
        print_character(game_sys)
