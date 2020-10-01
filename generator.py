"""
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use short instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
"""

import random
import re

import dice
from dice import roll as die
import equipment_tnu
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
    elif prefs['system_assumptions'] == 'dnd':
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
    def __init__(self, game_system, prefs, silly=False):
        self.prefs = prefs
        if silly:
            self.silly = True
            self.init_silly()
        else:
            self.silly = False
        if game_system == 'ham':
            classroll = die(3, 6)
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
        self.init_race_and_languages()
        primes = list(self.profession['primAttr'])
        spread = list(self.prefs['spread'])
        self.stats = dice.get_spread(spread, primes, self.prefs['modRange'], self.racemods)
        self.init_skills()
        #
        # get stats average, for reasons:
        stat_values = [int(value['val']) for key, value in dict.items(self.stats)]
        stats_avg = int(round(sum(stat_values) / len(stat_values)))
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
        if self.prefs['saves']:
            self.saves = dict(zip(self.prefs['saves'], self.profession['saves']))
        else:
            self.saves = {}
        #
        # let's get that basic combat data:
        self.init_combat(game_system)
        #
        # now for gear:
        if self.system_assumptions == 'tnu':
            self.my_gear_dump = self.get_gear_tnu(my_class)
        else:
            self.my_gear_dump = self.get_gear_dnd(stats_avg, self.system)
        #
        # pull out the weapons and armour into their own lists
        my_weapons = list(filter(lambda wep: wep.startswith('WEAPON: '), self.my_gear_dump))
        my_armour = list(filter(lambda arm: arm.startswith('ARMOUR: '), self.my_gear_dump))
        my_weaponlist = []
        my_armourlist = []
        for w in my_weapons:
            self.my_gear_dump.remove(w)
            if self.system == 'ham':
                w = re.sub(r',\sDmg:\s\d+d\d+', '', w)
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
        if self.system_assumptions == 'dnd':
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

    def get_gear_dnd(self, stats_avg, system):
        weapon_cls = self.profession['weapons']
        armour_cls = self.profession['armour']
        gear_bonus = []
        if self.profession['weapons'] in ['war', 'hlf']:
            bonus_wps = 2
        elif self.profession['weapons'] in ['mag']:
            bonus_wps = 0
        else:
            bonus_wps = 1
        #
        # the idea here is: the lower your stats, the more starting gear you get to compensate for sucking so hard
        if stats_avg >= 16:
            wps_choices = basic_choices = advanced_choices = 1
            weapon_cls = armour_cls = 'fuckall'
            money = [str(die(1, 6)) + ' assorted coin shavings']
            gear_bonus = gear_bonus + ['a half-eaten turkey leg from a disgusting place we won\'t mention,',
                                       'the bloody tooth of someone - or something - recently deprived of its '
                                       'favorite tooth']
        elif stats_avg >= 13:
            wps_choices = 0 + bonus_wps
            basic_choices = 4
            advanced_choices = 2
            if system == 'ham':
                money = [str(die(1, 6)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' silver coins']
        elif stats_avg >= 9:
            wps_choices = 1 + bonus_wps
            basic_choices = 5
            advanced_choices = 4
            if system == 'ham':
                money = [str(die(4, 8)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' gold coins']
        elif stats_avg >= 6:
            wps_choices = 2 + bonus_wps
            basic_choices = 8
            advanced_choices = 6
            if system == 'ham':
                money = [str(die(10, 10)) + ' coins']
            else:
                money = [str(die(3, 6)) + ' platinum coins']
        else:
            wps_choices = 3 + bonus_wps
            basic_choices = advanced_choices = 10
            money = [str(die(10, 6)) + ' assorted gems']
        if system == 'ham':
            gearlist = gear_ham.get_gearlist(weapon_cls, armour_cls)
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
                elif self.system in ['bnt', 'dd', 'ham', 'm81']:
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
        if game_system in ['dd']:
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

    def init_skills(self):
        if self.profession['skills'] == 'RANDOM':
            self.skills = []
            my_list = list(self.prefs['skill_choices'])
            if self.silly:
                my_list = my_list + self.silly_skills
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
            my_race = random.choice(list(self.prefs['race_choices']))
        else:
            my_race = self.profession['race']
        self.race = self.prefs['race_data'][my_race]['label']
        self.traits = self.traits + self.prefs['race_data'][my_race]['traits']
        self.languages = self.prefs['race_data'][my_race]['core_languages']
        self.racemods = self.prefs['race_data'][my_race]['mods']

    def load_prefs_data(self):
        self.system = self.prefs['system_name']
        self.system_fullname = self.prefs['system_fullname']
        self.system_assumptions = self.prefs['system_assumptions']
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
        if self.system in ['m81']:
            bonus_lang_choices = self.stats['MIND']['mod']
        elif self.system_assumptions == 'dnd':
            bonus_lang_choices = self.stats['INT']['mod']
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


def generate(game_system='tnu', silly=False):
    #
    # first let's load those system prefs, to accommodate multiple game variants
    prefs = dict(systems.get_system_prefs(game_system.upper()))
    return Character(game_system, prefs, silly)


if __name__ == "__main__":
    character = generate('tnu')
    print(character.__dict__)
