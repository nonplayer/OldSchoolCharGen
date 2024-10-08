"""
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use short instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
"""

import random
# import re

import dice
from dice import roll as die
import equipment_tnu
import gear_ddh
import gear_dnd
import gear_ham
import professions
import setting
import silly
import spells
import spells_tnu
import systems
import wizweaps


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
    elif prefs['acSystem'] == 'dd':
        if any('Suit Armour' in x for x in armour):
            ac_mod += 9
        elif any('Plate Mail' in x for x in armour):
            ac_mod += 7
        elif any('Banded Mail' in x for x in armour):
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
    elif prefs['acSystem'] == 'dnd':
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
    if prefs['acSystem'] != ['pla']:
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
    def __init__(self, game_system, prefs, silly=False):
        self.prefs = prefs
        if silly:
            self.silly = True
            self.init_silly()
        else:
            self.silly = False
        #
        # Although HAM used 3d6 for class by default, I've skewed
        # to use 1d20 here to offset the lack of true randomness
        if game_system == 'ham':
            classroll = die(1, 20)
            subroll = die(1, 4)
            self.profession = dict(professions.get_hammerclass(classroll, subroll))
        else:
            self.profession = dict(professions.get_profession(game_system))

        super(Character, self).__init__()

        self.load_prefs_data()
        self.gen_setting_data()
        #
        # let's get that juicy character data and break it out!
        self.load_profession_data()
        self.racedata = self.init_race_and_languages()
        self.race = self.racedata['label']
        self.traits = self.traits + self.racedata['traits']
        self.languages = self.racedata['core_languages']
        self.racemods = self.racedata['mods']
        primes = list(self.profession['primAttr'])
        spread = list(self.prefs['spread'])
        method = self.prefs['method']
        if method == 'standard':
            numbs = int(self.racedata['stat_dice_numbs'])
            sides = int(self.racedata['stat_dice_sides'])
            rolls = len(spread)
            array = dice.stats(rolls, numbs, sides)
        else:
            array = self.prefs['roll_array']
        self.stats = dice.get_standard_spread(array, spread, primes, self.prefs['modRange'], self.racemods)
        self.init_skills()
        #
        # get stats average, for reasons now deprecated:
        # stat_values = [int(value['val']) for key, value in dict.items(self.stats)]
        # stats_avg = int(round(sum(stat_values) / len(stat_values)))
        #
        # get languages
        self.init_bonus_languages()
        #
        # get social status
        if 'SOC' in self.stats:
            soc_score = self.stats['SOC']['val']
        else:
            soc_score = int(dice.roll(3, 6))
        my_class = dict(gen_social(soc_score))
        self.soc_class = my_class['title']
        self.soc_mod = str(my_class['mod'])
        #
        # time to get those saving throws
        if self.prefs['saves']:
            self.saves = self.init_saves()
        else:
            self.saves = False
        #
        # let's get that basic combat data:
        self.init_combat(game_system)
        #
        # now for gear:
        self.init_emcumbrance()
        if self.system == 'tnu':
            self.my_gear_dump = self.get_gear_tnu(my_class)
        else:
            self.my_gear_dump = self.get_gear_dnd(soc_score, self.system)
        #
        # pull out the weapons and armour into their own lists
        my_weapons = list(filter(lambda wep: wep.startswith('WEAPON: '), self.my_gear_dump))
        my_armour = list(filter(lambda arm: arm.startswith('ARMOUR: '), self.my_gear_dump))
        my_weaponlist = []
        my_armourlist = []
        for w in my_weapons:
            self.my_gear_dump.remove(w)
            my_weaponlist.append(str.title(w[8:]))
        for a in my_armour:
            self.my_gear_dump.remove(a)
            my_armourlist.append(str.title(a[8:]))
        if 'mu-weapons' in self.profession['flags']:
            my_weaponlist.append(wizweaps.generate())
        self.weapons = sorted(my_weaponlist)
        self.armour = sorted(my_armourlist)
        self.gear = sorted(self.my_gear_dump)
        # now to generate the character's armour class
        self.ac = gen_ac(self.prefs, my_armourlist)
        #if self.prefs['acSystem'] == 'dnd':
        if self.prefs['acSystem'] in ['dnd', 'dd']:
            if self.prefs['acType'] == 'descend':
                self.ac -= self.stats['DEX']['mod']
            else:
                self.ac += self.stats['DEX']['mod']
        #
        # and finally, we conclude with spells and magic:
        self.init_magic()

    def get_gear_tnu(self, my_class):
        my_gear_collection = list(equipment_tnu.get_gear(self.short, my_class['label']))
        return my_gear_collection

    def get_gear_dnd(self, social, system):
        weapon_cls = self.profession['weapons']
        armour_cls = self.profession['armour']
        if self.profession['wps']:
            free_wps = self.profession['wps']
        else:
            free_wps = 2
        gear_bonus = []
        if social <= 4:
            wps_choices = basic_choices = advanced_choices = 1
            weapon_cls = armour_cls = 'fuckall'
            money = [str(die(1, 6)) + ' assorted coin shavings']
            gear_bonus = gear_bonus + ['a half-eaten turkey leg from a disgusting place we won\'t mention,',
                                       'the bloody tooth of someone - or something - recently deprived of its '
                                       'favorite tooth']
        elif social <= 8:
            wps_choices = free_wps
            basic_choices = 4
            advanced_choices = 2
            if system == 'ham':
                money = [str(die(1, 6)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' silver coins']
        elif social <= 12:
            wps_choices = free_wps
            basic_choices = 5
            advanced_choices = 4
            if system == 'ham':
                money = [str(die(4, 8)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' gold coins']
        elif social <= 15:
            wps_choices = free_wps
            basic_choices = 8
            advanced_choices = 6
            if system == 'ham':
                money = [str(die(10, 10)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' platinum coins']
        elif social <= 17:
            wps_choices = free_wps
            basic_choices = 8
            advanced_choices = 8
            if system == 'ham':
                money = [str(die(20, 20)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' platinum coins']
        else:
            wps_choices = 1
            weapon_cls = armour_cls = 'holyfuckingshit'
            basic_choices = advanced_choices = 10
            money = [str(die(10, 6)) + ' assorted gems']
        if system == 'ham':
            gearlist = gear_ham.get_gearlist(weapon_cls, armour_cls)
        elif system == 'ddh':
            gearlist = gear_ddh.get_gearlist(weapon_cls, armour_cls)
        else:
            gearlist = gear_dnd.get_gearlist(weapon_cls, armour_cls)
        gear_wps = list(random.sample(gearlist['weapons'], wps_choices))
        gear_arm = [random.choice(gearlist['armour'])]
        gear_base = list(random.sample(gearlist['basic'], basic_choices))
        gear_advanced = list(random.sample(gearlist['advanced'], advanced_choices))
        gear_bonus = gear_bonus + list(gearlist['free'])
        my_gear_collection = gear_base + gear_advanced + gear_wps + gear_arm + gear_bonus + money
        if self.silly:
            gear_silly = random.sample(self.silly_gear, 1)
            my_gear_collection = my_gear_collection + gear_silly
        bonus_class_gear = list(self.profession['extragear'])
        if len(bonus_class_gear) > 0:
            for g in bonus_class_gear:
                my_gear_collection.append(g)
        return my_gear_collection

    def init_emcumbrance(self):
        if self.prefs['encumbrance'] == 'ham':
            self.encumbrance = int(self.stats['INT']['val'] + self.stats['STR']['mod'])
        else:
            self.encumbrance = False

    def init_silly(self):
        silly_prefs = dict(silly.get_silly())
        self.silly_skills = silly_prefs['skills']
        self.silly_gear = silly_prefs['gear']
        self.silly_langs = silly_prefs['langs']

    #        for key in silly_prefs:
    #            if key in prefs:
    #                prefs[key] = prefs[key] + silly_prefs[key]
    #            else:
    #                pass
    #        return prefs

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
                    spells.get_cantrips(self.system, self.profession['spellChooseAs'],
                                        self.profession['cantrips']))
            if self.num_spells > 0:
                my_spells = []
                if self.system == 'tnu':
                    my_spells = spells_tnu.get_spells(self.profession['spellChooseAs'], self.align, self.num_spells)
                elif self.system in ['bnt', 'dd', 'ddh', 'ham', 'm81']:
                    my_spells = spells.get_spells(self.system, self.profession['spellChooseAs'], self.num_spells)
                if self.profession['extraspells']:
                    my_extra_spells = [s for s in list(self.profession['extraspells'])]
                    my_spells = my_spells + my_extra_spells
                sorted(my_spells)
                self.spells = my_spells + self.spells
        else:
            self.caster = False

    def init_combat(self, game_system):
        # time for the combat data. Right now it's just level 1 hacking,
        # but I might update if I ever get around to multi-level generation
        # (but admittedly this is unlikely)
        #
        if game_system in ['dd', 'ddh']:
            combat_mod = 1
        elif self.profession['attacksAs'] in ['best', 'mid-hi']:
            combat_mod = 1
        else:
            combat_mod = 0
        self.number_of_attacks = self.profession['numAttacks']
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

    def init_saves(self):
        # saves_array = {}
        # if self.system == 'ham':
        prof_mods = list(self.profession['saves'])
        stat_mods_array = []
        for val in list(self.prefs['saves']['mods']):
            prof_mod = int(prof_mods.pop(0))
            if val != 'None':
                if self.prefs['save_style'] == 'descend':
                    stat_mod = prof_mod - int(self.stats[val]['mod'])
                else:
                    stat_mod = int(self.stats[val]['mod']) + prof_mod
            else:
                stat_mod = prof_mod
            stat_mods_array.append(stat_mod)
        saves_array = dict(zip(self.prefs['saves']['names'], stat_mods_array))
        # elif self.prefs['saves']:
        #     saves_array = dict(zip(self.prefs['saves'], self.profession['saves']))
        return saves_array

    def init_skills(self):
        if self.profession['skills'] == 'RANDOM':
            self.skills = []
            my_list = list(self.prefs['skill_choices'])
            if self.silly:
                #my_list = my_list + self.silly_skills
                my_list = self.silly_skills
            my_num_skills = self.stats[self.prefs['skills_mod']]['mod'] + 4
            if my_num_skills < 1:
                my_num_skills = 1
            self.skills = [s for s in list(random.sample(my_list, my_num_skills))]
            self.skills = sorted(self.skills)
        elif self.profession['skills']:
            self.skills = list(sorted(self.profession['skills']))
        else:
            self.skills = self.profession['skills']

    def init_race_and_languages(self):
        if self.profession['race'] == 'RANDOM':
            spec_race = random.choice(list(self.prefs['race_choices']))
        else:
            spec_race = self.profession['race']
        my_race = dict(self.prefs['race_data']['default'])
        new_race = dict(self.prefs['race_data'][spec_race])
        my_race.update(new_race)
        return my_race

    def load_prefs_data(self):
        self.system = self.prefs['system_name']
        self.system_fullname = self.prefs['system_fullname']
        self.setting = self.prefs['setting']
        self.affects = dict(self.prefs['affects'])
        self.hps_mod = self.prefs['HPsMod']

    def init_bonus_languages(self):
        self.languages = self.languages + self.prefs['core_languages'] + self.profession['extralangs']
        new_languages = self.prefs['language_choices']
        if self.silly:
            new_languages = new_languages + self.silly_langs
        for lang in self.languages:
            if lang in new_languages:
                new_languages.remove(lang)
        if self.prefs['bonus_langs']:
            bonus_lang_choices = self.stats[self.prefs['bonus_langs_stat']]['mod']
        else:
            bonus_lang_choices = 0
        while bonus_lang_choices > 0 and len(new_languages) > 0:
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
        self.hd = self.profession['hd']
        if 'haspa' in self.profession['flags']:
            self.pa = 'Yes'
        else:
            self.pa = 'None'

    def gen_setting_data(self):
        setting_data = setting.get_setting_data(self.setting)
        self.personality = random.choice(setting_data['personality'])
        self.background = random.choice(setting_data['background'])
        self.age = random.choice(setting_data['age'])
        self.looks = random.choice(setting_data['looks'])


def generate(game_system='def', silly=False):
    #
    # first let's load those system prefs, to accommodate multiple game variants
    prefs = dict(systems.get_system_prefs(game_system.lower()))
    return Character(game_system, prefs, silly)


if __name__ == "__main__":
    character = generate('ddh')
    print(character.__dict__)
