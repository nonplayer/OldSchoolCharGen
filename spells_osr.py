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
    'bard': [
        'Alarm', 'Animate Rope', 'Cause Fear', 'Change Self', 'Charm Person', 'Comprehend Languages',
        'Cure Light Wounds', 'Detect Secret Doors', 'Erase', 'Expeditious Retreat', 'Feather Fall', 'Fool’s Gold',
        'Foretelling', 'Grease', 'Hideous Laughter', 'Hypnotism', 'Identify', 'Magic Aura', 'Magic Mouth',
        'Obscure Object', 'Phantasmal Force', 'Remove Fear', 'Sleep', 'Summon Monster I', 'Undetectable Alignment',
        'Unseen Servant', 'Ventriloquism',
    ],
    'cleric': [
        'Bane', 'Bless', 'Bless Water ', 'Cause Fear', 'Command', 'Comprehend Languages', 'Cure Light Wounds',
        'Curse Water ', 'Deathwatch', 'Detect Evil', 'Detect Undead', 'Divine Favor', 'Doom', 'Endure Elements',
        'Entropic Shield', 'Inflict Light Wounds', 'Invisibility to Undead', 'Magic Stone', 'Magic Weapon',
        'Obscuring Mist', 'Protection from Evil/Good', 'Random Action', 'Remove Fear', 'Sanctuary',
        'Shield of Faith', 'Summon Monster I',
    ],
    'druid': [
        'Animal Friendship', 'Calm Animals', 'Charm Animal', 'Cure Light Wounds', 'Detect Animals or Plants',
        'Detect Snares and Pits', 'Elemental Weapon', 'Endure Elements', 'Entangle', 'Faerie Fire', 'Goodberry',
        'Hide from Animals', 'Jump', 'Longstrider', 'Magic Fang', 'Magic Stone', 'Obscuring Mist',
        'Pass without Trace', 'Produce Flame', 'Shillelagh', 'Speak with Animals', 'Summon Nature’s Ally I',
    ],
    'mu': [
        'Alarm [A]', 'Animate Rope [T]', 'Burning Hands [EV]', 'Cause Fear [N]', 'Change Self [I]',
        'Charm Person [EN]', 'Chill Touch [N]', 'Color Spray [I]', 'Comprehend Languages [D]',
        'Detect Secret Doors [D]', 'Detect Undead [D]', 'Elemental Weapon [T]', 'Endure Elements [A]',
        'Energy Missile [EV]', 'Enlarge Person [T]', 'Erase [T]', 'Expeditious Retreat [T]', 'Feather Fall [T]',
        'Floating Disk [EV]', 'Fool’s Gold [T]', 'Grease [C]', 'Hold Portal [A]', 'Hypnotism [EN]', 'Identify [D]',
        'Ill Omen [EN]', 'Jump [T]', 'Mage Armor [C]', 'Magic Aura [I]', 'Magic Missile [EV]', 'Magic Weapon [T]',
        'Mind Thrust [EV]', 'Mount [C]', 'Obscuring Mist [C]', 'Phantasmal Force [I]', 'Precognition [D]',
        'Protection from Evil [A]', 'Protection from Good [A]', 'Ray of Enfeeblement [N]', 'Reduce Person [T]',
        'Shield [A]', 'Shocking Grasp [EV]', 'Sleep [EN]', 'Summon Monster I [C]', 'True Strike [D]',
        'Unseen Servant [C]', 'Ventriloquism [I]',
    ],
}


cantrips_bnt = {
    'bard': [
        'Audible Glamer', 'Dancing Lights', 'Daze', 'Detect Magic', 'Flare', 'Know Direction', 'Light', 'Lullaby',
        'Mage Hand', 'Mending', 'Message', 'Open/Close', 'Prestidigitation', 'Resistance', 'Summon Instrument',
    ],
    'cleric': [
        'Create Water', 'Cure Minor Wounds', 'Detect Magic', 'Detect Poison', 'Guidance', 'Inflict Minor Wounds',
        'Light', 'Mending', 'Purify Food and Drink', 'Read Magic', 'Resistance', 'Virtue',
    ],
    'druid': [
        'Create Water', 'Cure Minor Wounds', 'Detect Magic', 'Detect Poison', 'Discern Aura', 'Flare', 'Guidance',
        'Know Direction', 'Light', 'Mending', 'Purify Food and Drink', 'Read Magic', 'Resistance', 'Virtue',
    ],
    'mu': [
        'Acid Splash', 'Audible Glamer', 'Dancing Lights', 'Daze', 'Detect Magic', 'Detect Poison', 'Disrupt Undead',
        'Flare', 'Light', 'Mage Hand', 'Mending', 'Message', 'Open/Close', 'Prestidigitation', 'Ray of Frost',
        'Read Magic', 'Resistance', 'Smoke Image', 'Touch of Fatigue', 'Wizard Mark',
    ],
}



spells_pla = {
    'wiz': [],
    'clr': [],
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