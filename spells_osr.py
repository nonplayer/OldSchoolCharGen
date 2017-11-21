import random
from random import choice as ch


spells_dd = {
    'cleric': [
        'Cure Light Wounds (R)', 'Detect Evil', 'Detect Magic', 'Light (R)',
        'Protection From Evil', 'Purify Food And Water', 'Remove Fear (R)', 'Resist Cold ',
    ],
    'mu': [
        'Analyse', 'Charm Person', 'Detect Magic', 'Floating Disc', 'Hold Portal', 'Light (R)',
        'Magic Missile', 'Protection From Evil', 'Read Languages', 'Shield', 'Sleep', 'Ventriloquism',
    ],
}


spells_bnt = {
    'cleric': [],
    'druid': [],
    'mu': [],
    'pal': [],
    'ranger': [],
    'sorc': [],
}


cantrips_bnt = {
    'bard': [
        'Audible Glamer', 'Dancing Lights', 'Daze', 'Detect Magic', 'Flare', 'Know Direction', 'Light', 'Lullaby',
        'Mage Hand', 'Mending', 'Message', 'Open/Close', 'Prestidigitation', 'Resistance', 'Summon Instrument',
    ],
    'cleric': [],
    'druid': [],
    'mu': [],
    'sorc': [],
}



spells_pla = {
    'wiz': [],
    'cle': [],
    'wit': [],
    'war': [],
    'min': [],
}


systems_match = {
    'bnt': spells_bnt,
    'dd': spells_dd,
    'pla': spells_pla,
}


def get_cantrips():
    return


# let's generate some spells!
def get_spells(gamesystem, prof, count):
    myChoices = systems_match[gamesystem][prof]
    mySpells = list(set(random.sample(list(myChoices), count)))
    return sorted(mySpells)


# test it out
def main():
    for each in get_spells('dd', 'cleric', 3):
        print(each)


if __name__ == "__main__":
    main()