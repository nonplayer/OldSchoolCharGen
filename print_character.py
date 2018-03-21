"""
Extracted from the core generator.
This does nothing but call the character generator and print it locally.
"""

import argparse
import generator

parser = argparse.ArgumentParser(description='Get Game System')
parser.add_argument('-g', '--game_system', type=str, required=True, choices=['bnt', 'bntx', 'dd', 'm81', 'tnu'],
                    help='The abbreviated Game System (bnt, bntx, dd, m81, tnu)')
parser.add_argument('-H', '--hammercrawl', action='store_true',
                    help='Enable HAMMERCRAWL! extended features (currently disabled)')
parser.add_argument('-n', '--number_of_characters', type=int, action='store', default=1,
                    help='How many character to generate.')
args = parser.parse_args()

supported_systems = [
    'tnu', 'dd', 'bnt', 'bntx', 'm81',
]


def print_character(game_system):
    game_system = game_system.lower()
    character = generator.generate(game_system)
    print("\nA new random character for " + str(character.system_fullname))
    print("-----------------------------------------------------")
    # print("Raw Data Print: ", gen_data)
    print("Profession: %s;  Level: %s;  Race: %s" % (character.long, str(character.lvl), character.race))
    print("Alignment: %s;  Age: %s;  Looks: %s" % (character.align.title(), character.age, character.looks))
    print("Trait: %s;  Background: %s;  Social Status: %s (%s)" %
          (character.personality, character.background, character.soc_class, str(character.soc_mod)))
    if game_system == 'tnu':
        print("Disposition: %sd%s;  Psychic Armour: %s" % (str(character.lvl), str(character.hd), str(character.pa)))
    elif character.stats[character.hps_mod]['mod'] > 0:
        print("Hit Die: %sd%s+%s;  Psychic Armour: %s" %
              (str(character.lvl), str(character.hd), str(character.stats[character.hps_mod]['mod']*character.lvl),
               str(character.pa)))
    elif character.stats[character.hps_mod]['mod'] < 0:
        print("Hit Die: %sd%s%s;  Psychic Armour: %s" %
              (str(character.lvl), str(character.hd), str(character.stats[character.hps_mod]['mod']*character.lvl),
               str(character.pa)))
    else:
        print("Hit Die: %sd%s;  Psychic Armour: %s" % (str(character.lvl), str(character.hd), str(character.pa)))
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
            for s in list(character.spells):
                print(s)
    print("")


if __name__ == "__main__":
    game_sys = args.game_system
    if args.hammercrawl:
        print("HAMMERCRAWL TIME!!!!! Okay this currently does nothing, but stay tuned for more...")
    while game_sys not in supported_systems:
        print("\nGame System choice is missing or invalid. Please enter one of the following systems:\n")
        print("bnt  = Blood & Treasure (1st Edition)")
        print("bntx = Blood & Treasure 1st Edition with Expanded Monster Races")
        print("dd   = Dark Dungeons")
        print("m81  = Microlite81")
        print("tnu  = The Nightmares Underneath")
        print()
        game_sys = input("Enter the system abbreviation from above: ")
    for n in range(args.number_of_characters):
        print_character(game_sys)
