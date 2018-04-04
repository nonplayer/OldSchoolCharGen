import random
# from random import choice as ch


spells_basic = {
    'cleric': [
        'Level 1: Cure Light Wounds (R)', 'Level 1: Detect Evil', 'Level 1: Detect Magic',
        'Level 1: Light (R)', 'Level 1: Protection From Evil', 'Level 1: Purify Food And Water (R)',
        'Level 1: Remove Fear (R)', 'Level 1: Resist Cold ',
    ],
    'mu': [
        'Level 1: Charm Person', 'Level 1: Detect Magic', 'Level 1: Floating Disc',
        'Level 1: Hold Portal', 'Level 1: Light (R)', 'Level 1: Magic Missile', 'Level 1: Protection From Evil',
        'Level 1: Read Languages', 'Level 1: Shield', 'Level 1: Sleep', 'Level 1: Ventriloquism',
    ],
}

spells_dd = {
    'cleric': [
        'Level 1: Cure Light Wounds (R)', 'Level 1: Detect Evil', 'Level 1: Detect Magic',
        'Level 1: Light (R)', 'Level 1: Protection From Evil', 'Level 1: Purify Food And Water (R)',
        'Level 1: Remove Fear (R)', 'Level 1: Resist Cold ',
    ],
    'mu': [
        'Level 1: Analyse', 'Level 1: Charm Person', 'Level 1: Detect Magic', 'Level 1: Floating Disc',
        'Level 1: Hold Portal', 'Level 1: Light (R)', 'Level 1: Magic Missile', 'Level 1: Protection From Evil',
        'Level 1: Read Languages', 'Level 1: Shield', 'Level 1: Sleep', 'Level 1: Ventriloquism',
    ],
}

spells_bnt = {
    'bard': [
        'Level 1: Alarm', 'Level 1: Animate Rope', 'Level 1: Cause Fear', 'Level 1: Change Self',
        'Level 1: Charm Person', 'Level 1: Comprehend Languages', 'Level 1: Cure Light Wounds',
        'Level 1: Detect Secret Doors', 'Level 1: Erase', 'Level 1: Expeditious Retreat', 'Level 1: Feather Fall',
        'Level 1: Fool’s Gold', 'Level 1: Foretelling', 'Level 1: Grease', 'Level 1: Hideous Laughter',
        'Level 1: Hypnotism', 'Level 1: Identify', 'Level 1: Magic Aura', 'Level 1: Magic Mouth',
        'Level 1: Obscure Object', 'Level 1: Phantasmal Force', 'Level 1: Remove Fear', 'Level 1: Sleep',
        'Level 1: Summon Monster I', 'Level 1: Undetectable Alignment',
        'Level 1: Unseen Servant', 'Level 1: Ventriloquism',
    ],
    'cleric': [
        'Level 1: Bane', 'Level 1: Bless', 'Level 1: Bless Water ', 'Level 1: Cause Fear', 'Level 1: Command',
        'Level 1: Comprehend Languages', 'Level 1: Cure Light Wounds', 'Level 1: Curse Water ', 'Level 1: Deathwatch',
        'Level 1: Detect Evil', 'Level 1: Detect Undead', 'Level 1: Divine Favor', 'Level 1: Doom',
        'Level 1: Endure Elements', 'Level 1: Entropic Shield', 'Level 1: Inflict Light Wounds',
        'Level 1: Invisibility to Undead', 'Level 1: Magic Stone', 'Level 1: Magic Weapon', 'Level 1: Obscuring Mist',
        'Level 1: Protection from Evil/Good', 'Level 1: Random Action', 'Level 1: Remove Fear', 'Level 1: Sanctuary',
        'Level 1: Shield of Faith', 'Level 1: Summon Monster I',
    ],
    'druid': [
        'Level 1: Animal Friendship', 'Level 1: Calm Animals', 'Level 1: Charm Animal', 'Level 1: Cure Light Wounds',
        'Level 1: Detect Animals or Plants', 'Level 1: Detect Snares and Pits', 'Level 1: Elemental Weapon',
        'Level 1: Endure Elements', 'Level 1: Entangle', 'Level 1: Faerie Fire', 'Level 1: Goodberry',
        'Level 1: Hide from Animals', 'Level 1: Jump', 'Level 1: Longstrider', 'Level 1: Magic Fang',
        'Level 1: Magic Stone', 'Level 1: Obscuring Mist', 'Level 1: Pass without Trace', 'Level 1: Produce Flame',
        'Level 1: Shillelagh', 'Level 1: Speak with Animals', 'Level 1: Summon Nature’s Ally I',
    ],
    'mu': [
        'Level 1: Alarm [A]', 'Level 1: Animate Rope [T]', 'Level 1: Burning Hands [EV]', 'Level 1: Cause Fear [N]',
        'Level 1: Change Self [I]', 'Level 1: Charm Person [EN]', 'Level 1: Chill Touch [N]',
        'Level 1: Color Spray [I]', 'Level 1: Comprehend Languages [D]', 'Level 1: Detect Secret Doors [D]',
        'Level 1: Detect Undead [D]', 'Level 1: Elemental Weapon [T]', 'Level 1: Endure Elements [A]',
        'Level 1: Energy Missile [EV]', 'Level 1: Enlarge Person [T]', 'Level 1: Erase [T]',
        'Level 1: Expeditious Retreat [T]', 'Level 1: Feather Fall [T]', 'Level 1: Floating Disk [EV]',
        'Level 1: Fool’s Gold [T]', 'Level 1: Grease [C]', 'Level 1: Hold Portal [A]', 'Level 1: Hypnotism [EN]',
        'Level 1: Identify [D]', 'Level 1: Ill Omen [EN]', 'Level 1: Jump [T]', 'Level 1: Mage Armor [C]',
        'Level 1: Magic Aura [I]', 'Level 1: Magic Missile [EV]', 'Level 1: Magic Weapon [T]',
        'Level 1: Mind Thrust [EV]', 'Level 1: Mount [C]', 'Level 1: Obscuring Mist [C]',
        'Level 1: Phantasmal Force [I]', 'Level 1: Precognition [D]', 'Level 1: Protection from Evil [A]',
        'Level 1: Protection from Good [A]', 'Level 1: Ray of Enfeeblement [N]', 'Level 1: Reduce Person [T]',
        'Level 1: Shield [A]', 'Level 1: Shocking Grasp [EV]', 'Level 1: Sleep [EN]', 'Level 1: Summon Monster I [C]',
        'Level 1: True Strike [D]', 'Level 1: Unseen Servant [C]', 'Level 1: Ventriloquism [I]',
    ],
}

cantrips_bnt = {
    'bard': [
        'Cantrip: Audible Glamer', 'Cantrip: Dancing Lights', 'Cantrip: Daze', 'Cantrip: Detect Magic',
        'Cantrip: Flare', 'Cantrip: Know Direction', 'Cantrip: Light', 'Cantrip: Lullaby',
        'Cantrip: Mage Hand', 'Cantrip: Mending', 'Cantrip: Message', 'Cantrip: Open/Close',
        'Cantrip: Prestidigitation', 'Cantrip: Resistance', 'Cantrip: Summon Instrument',
    ],
    'cleric': [
        'Cantrip: Create Water', 'Cantrip: Cure Minor Wounds', 'Cantrip: Detect Magic',
        'Cantrip: Detect Poison', 'Cantrip: Guidance', 'Cantrip: Inflict Minor Wounds',
        'Cantrip: Light', 'Cantrip: Mending', 'Cantrip: Purify Food and Drink',
        'Cantrip: Read Magic', 'Cantrip: Resistance', 'Cantrip: Virtue',
    ],
    'druid': [
        'Cantrip: Create Water', 'Cantrip: Cure Minor Wounds', 'Cantrip: Detect Magic',
        'Cantrip: Detect Poison', 'Cantrip: Discern Aura', 'Cantrip: Flare', 'Cantrip: Guidance',
        'Cantrip: Know Direction', 'Cantrip: Light', 'Cantrip: Mending', 'Cantrip: Purify Food and Drink',
        'Cantrip: Read Magic', 'Cantrip: Resistance', 'Cantrip: Virtue',
    ],
    'mu': [
        'Cantrip: Acid Splash', 'Cantrip: Audible Glamer', 'Cantrip: Dancing Lights', 'Cantrip: Daze',
        'Cantrip: Detect Magic', 'Cantrip: Detect Poison', 'Cantrip: Disrupt Undead',
        'Cantrip: Flare', 'Cantrip: Light', 'Cantrip: Mage Hand', 'Cantrip: Mending', 'Cantrip: Message',
        'Cantrip: Open/Close', 'Cantrip: Prestidigitation', 'Cantrip: Ray of Frost',
        'Cantrip: Resistance', 'Cantrip: Smoke Image', 'Cantrip: Touch of Fatigue', 'Cantrip: Wizard Mark',
    ],
}

spells_pla = {
    'wiz': [],
    'clr': [],
    'wit': [],
    'war': [],
    'min': [],
}

spells_match = {
    'bnt': spells_bnt,
    'ham': spells_dd,
    'dd': spells_dd,
    'm81': spells_basic,
    'pla': spells_pla,
}

cantrips_match = {
    'bnt': cantrips_bnt,
}


def get_cantrips(gamesystem, prof, count):
    c_choices = cantrips_match[gamesystem][prof]
    my_cants = list(set(random.sample(list(c_choices), count)))
    return sorted(my_cants)


# let's generate some spells!
def get_spells(gamesystem, prof, count):
    s_choices = spells_match[gamesystem][prof]
    my_spells = list(set(random.sample(list(s_choices), count)))
    return sorted(my_spells)


# test it out
def main():
    for each in get_cantrips('bnt', 'cleric', 3):
        print(each)


if __name__ == "__main__":
    main()
