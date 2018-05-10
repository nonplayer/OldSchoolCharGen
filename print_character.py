"""
Extracted from the core generator.
This does nothing but call the character generator and print it locally.
"""

import argparse
import generator

parser = argparse.ArgumentParser(description='Get Game System')
parser.add_argument('-g', '--game_system', type=str, required=True, choices=['bnt', 'bntx', 'dd', 'ham', 'm81', 'tnu'],
                    help='The abbreviated Game System (bnt, bntx, dd, ham, m81, tnu)')
parser.add_argument('-n', '--number_of_characters', type=int, action='store', default=1,
                    help='How many character to generate.')
args = parser.parse_args()

supported_systems = [
    'dd', 'bnt', 'bntx', 'ham', 'm81', 'tnu'
]


def print_character(character):
    print()
    print("A new random character for " + str(character.system_fullname))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    if character.system == 'tnu':
        print("Profession: %s;  Level: %s;  Race: %s" % (character.long, str(character.lvl), character.race))
    else:
        print("Profession: %s;  Level: %s;  Race: %s;  Hit Die: %sd%s + %s mod" %
              (character.long, str(character.lvl), character.race, str(character.lvl), str(character.hd),
               str(character.hps_mod)))
    print("Alignment: %s;  Age: %s;  Looks: %s" % (character.align.title(), character.age, character.looks))
    print("Trait: %s;  Background: %s;  Social Status: %s (%s)" %
          (character.personality, character.background, character.soc_class, str(character.soc_mod)))
    if character.system == 'tnu':
        print("Disposition: %sd%s;  Psychic Armour: %s" % (str(character.lvl), str(character.hd), str(character.pa)))
    print("---------------")
    print("\nAttribute Scores:")
    print("-----------------")
    for key, value in dict.items(character.stats):
        if int(value['val']) < 10 and int(value['mod']) < 0:
            print("%s:  %s (%s): Affects %s" % (key, str(value['val']), str(value['mod']), str(character.affects[key])))
        elif int(value['val']) < 10 and int(value['mod']) >= 0:
            print("%s:  %s (+%s): Affects %s" % (key, str(value['val']), str(value['mod']),
                                                 str(character.affects[key])))
        elif int(value['val']) > 9 and int(value['mod']) >= 0:
            print("%s: %s (+%s): Affects %s" % (key, str(value['val']), str(value['mod']), str(character.affects[key])))
        else:
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
    if character.system == 'ham':
        print("# of Attack Dice: %s;  Melee: %s;  Ranged: %s;  AC: %s" %
              (int(character.number_of_attacks), str(character.melee), str(character.range), str(character.ac)))
    else:
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
            for s in list(character.spells):
                print(s)
    print("--------------------")


if __name__ == "__main__":
    game_sys = args.game_system
    while game_sys not in supported_systems:
        print("\nGame System choice is missing or invalid. Please enter one of the following systems:\n")
        print("bnt  = Blood & Treasure (1st Edition)")
        print("bntx = Blood & Treasure 1st Edition with Expanded Monster Races")
        print("dd   = Dark Dungeons")
        print("m81  = Microlite81")
        print("ham  = HAMMERCRAWL!")
        print("tnu  = The Nightmares Underneath")
        print()
        game_sys = input("Enter the system abbreviation from above: ")
    for n in range(args.number_of_characters):
        new_character = generator.generate(game_sys.lower())
        print_character(new_character)
        new_character = None
