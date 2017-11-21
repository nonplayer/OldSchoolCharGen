import random
from random import choice as ch

import dice

'''
All weapons are marked with WEAPON: at the beginning
All armours are marked with ARMOUR: at the beginning
I'm considering doing the same for MAGIC: but haven't added it yet
these tags will be used to pull them from the gear dump and separate into their own categories
'''

wretched = {
    'gear1': [
        'WEAPON: a pistol that spits forth the concentrated fury of a dead age, long buried and forgotten. It never needs to be reloaded'],
    'gear2': [
        'ARMOUR: a magical cloak that allows you to sneak around like a thief and also protects you as if it were heavy armour, though it weighs nothing'],
    'gear3': ['a 2-person tent', '4 wooden stakes', '12 iron spikes',
              'a set of tools (for the profession of your choice)', 'a small hammer, two days of food',
              'a plump wineskin', ch(['WEAPON: a dagger', 'ARMOUR: a shield (AC+1)']),
              ch(['WEAPON: a club', 'WEAPON: 3 feet of iron chain, with broken manacles on one end'])],
    'gear4': ['a backpack', '6 torches', 'three days worth of food',
              ch(['WEAPON: a club', 'WEAPON: a one-handed melee weapon of your choice']),
              ch(['ARMOUR: a leather jerkin (Light Armour, AC:13, Enc:1)', 'ARMOUR: a shield (AC+1)'])],
    'gear5': ['WEAPON: an axe', 'WEAPON: a dagger', 'WEAPON: a spear', 'a military flag (yours or someone else\'s)',
              'a lantern (but no oil)',
              'a pouch of tobacco (but no pipe)', ch(
            ['a stolen purse with ' + str(random.randint(13, 16)) + ' silver coins (worth 1c each)',
             '2 bottles of your choice of alcoholic beverage'])],
    'gear6': ['a lantern', '2 flasks of oil', 'a flying carpet'],
    'gear7': [str(dice.roll(1,6)) + ' doses of drugs (your choice what type)', 'WEAPON: a club',
              'a mask that lets you see ghosts, spirits, and invisible things'],
    'assassin': [ch(['WEAPON: a dagger', 'a vial of poison'])],
    'bard': ['a cheap, dog-eared, old spellbook, but you may not have more than a single weapon'],
    'champ_chaos': ['a slave collar that you have yet to remove',
                    'a cheap, dog-eared, old spellbook, but you may not have more than a single weapon'],
    'champ_evil': ['a slave collar that you have yet to remove'],
    'champ_good': ['a slave collar that you have yet to remove'],
    'champ_law': ['a slave collar that you have yet to remove'],
    'cultist': ['an inexpensive symbol of your faith, made of ' + ch(['cloth', 'wood']),
                'a cheap, dog-eared, old spellbook, but you may not have more than a single weapon'],
    'scholar': ['a cheap, dog-eared, old spellbook, but you may not have more than a single weapon'],
    'wizard': ['a cheap, dog-eared, old spellbook, but you may not have more than a single weapon'],
}

peasant = {
    'gear1': [
        '50 feet of silk rope', 'a grappling hook', 'a backpack',
        'the preserved hand of a murderer recently hanged',
        ch([['WEAPON: an axe', 'ARMOUR: a shield (AC+1)'], ['WEAPON: any pole arm', 'one vial of holy water']])
    ],
    'gear2': ['WEAPON: a club', 'ARMOUR: a leather jerkin (Light Armour, AC:13, Enc:1)',
              '6 torches', 'a sack', 'a small bouquet of flowers', 'your master\'s dog'],
    'gear3': ['a bedroll', 'WEAPON: a club', 'WEAPON: a short bow and a quiver containing 12 arrows',
              'an empty wineskin', '2 weeks worth of rations', ch(['a human skull', '2 nice, fat ducks'])],
    'gear4': ['a backpack', 'a bedroll', '2 weeks worth of rations', 'a small hammer', '12 iron spikes',
              'a handful of caltrops', '6 torches', 'a tinderbox', 'WEAPON: the close combat weapon of your choice'],
    'gear5': [
        'WEAPON: brass knuckles', 'WEAPON: a sling with 12 good rocks', '12 candles', 'a box of matches',
        ch(['WEAPON: an axe', 'WEAPON: a musket with 12 bullets and a powder horn']), ch(['', 'ARMOUR: a shield (AC+1)'])
    ],
    'gear6': ['WEAPON: a dagger',
              '4 healing potions that, when drunk, will restore '
              + str(dice.roll(1,6) + 1) + 'points of lost Health or allow you to re-roll your Disposition'],
    'gear7': [
        ch(['', 'WEAPON: a 2-handed sword']),
        ch(['', 'WEAPON: a long bow, quiver, and 24 arrows']),
        ch(['', 'ARMOUR: a chainmail hauberk (Heavy Armour, AC:15, Enc:2)']),
        ch(['', 'a backpack with 50 feet of rope and climbing gear']),
        ch(['', '2 weeks worth of rations']),
        ch(['', 'a lantern with 2 flasks of oil']),
        ch(['', 'a  mule', 'empty saddlebags']),
        ch(['', 'All of your gear is stolen']),
    ],
    'bard': [ch(['a carved flute', 'a drum']),
             'a spellbook and up to 2 other books concerning non-magical subjects'],
    'champ_chaos': ['the symbol of your lands or master on your clothes',
                    'a spellbook and up to 2 other books concerning non-magical subjects'],
    'champ_evil': ['the symbol of your lands or master on your clothes'],
    'champ_good': ['the symbol of your lands or master on your clothes'],
    'champ_law': ['the symbol of your lands or master on your clothes'],
    'cultist': ['an inexpensive symbol of your faith, made of ' + ch(['cloth', 'wood']),
                'a spellbook and up to 2 other books concerning non-magical subjects'],
    'scholar': ['a spellbook and up to 2 other books concerning non-magical subjects'],
    'thief': [str(dice.roll(1,6)) + ' doses of drugs (your choice what type)'],
    'wizard': ['a spellbook and up to 2 other books concerning non-magical subjects'],
}

poor = {
    'gear1': ['WEAPON: an axe', 'WEAPON: 3 daggers', 'WEAPON: a mace', 'WEAPON: a pole arm', 'WEAPON: a sword',
              '6 torches', 'a tinderbox', 'ARMOUR: wicker armour (Light Armour, AC:13, Enc:1)', 'a brand somewhere on your body'],
    'gear2': ['a backpack', 'a bedroll', 'a lucky charm amulet', 'a wineskin', 'a week of rations', 'a spyglass',
              'a quiver', ch(['WEAPON: a light crossbow with 24 crossbow bolts',
                              'WEAPON: a short bow with 24 arrows'])],
    'gear3': ['a backpack', 'a bedroll',
              'a written license allowing you to practice the profession of bounty hunter',
              str(random.randint(6,8)) + 'cyphers',
              ch(['', 'WEAPON: a club']),
              ch(['', 'WEAPON: a net']),
              ch(['', 'WEAPON: a sword']),
              ch(['', 'ARMOUR: a chainmail shirt (Light Armour, AC:13, Enc:1)']),
              ch(['', 'ARMOUR: a shield (AC+1)']),
              ],
    'gear4': [
        'a backpack', ch(['WEAPON: a club', 'WEAPON: a dagger']), '2 weeks worth of rations',
        ch(['', 'an animal trap']), ch(['', 'a compass']), ch(['', 'ARMOUR: a leather jerkin (Light Armour, AC:13, Enc:1)']),
        ch(['', 'a pack of marked cards']), ch(['', 'WEAPON: a pole arm']), ch(['', 'ARMOUR: a shield (AC+1)']),
    ],
    'gear5': ['a bank note worth ' + str(random.randint(13, 15)) + ' cyphers', 'WEAPON: a dagger',
              'a random hireling', 'a shoulder bag', 'a set of tools (for the profession of your choice)',
              'a walking stick', 'a wineskin', ch(['a wheel of cheese', '2 days worth of dried meat jerky'])],
    'gear6': ['a large sack', 'WEAPON: the close combat weapon of your choice', 'a book you can\'t read',
              'a stolen bag of coins worth 20 cyphers', 'a fire in your heart that the nobility can never quench'],
    'gear7': ['WEAPON: a stolen bastard sword', 'ARMOUR: a stolen chainmail hauberk (Heavy Armour, AC:15, Enc:2)',
              'a stolen lantern', '2 stolen flasks of oil', 'a stolen mule with saddlebags', 'a stolen treasure map'],
    'assassin': ['WEAPON: an extra close combat weapon'],
    'bard': ['an innocuous spellbook', 'a travel memoir describing the local area'],
    'champ_chaos': [ch(['a banner', 'a flag']) + ' on a pole', 'an innocuous spellbook',
                    'a travel memoir describing the local area'],
    'champ_evil': [ch(['a banner', 'a flag']) + ' on a pole'],
    'champ_good': [ch(['a banner', 'a flag']) + ' on a pole'],
    'champ_law': [ch(['a banner', 'a flag']) + ' on a pole'],
    'cultist': ['an inexpensive symbol of your cult', 'a piece of clothing that signifies your faith',
                'an innocuous spellbook', 'a travel memoir describing the local area'],
    'scholar': ['you always have at least 2 scholarly books', 'an innocuous spellbook',
                'a travel memoir describing the local area'],
    'wizard': ['an innocuous spellbook', 'a travel memoir describing the local area'],
}

middle = {
    'gear1': ['WEAPON: a dagger', 'a sack', 'spectacles',
              'a ring that makes you immune to  ' + ch(
                  ['acid', 'cold', 'fire and heat']) + ' when you wear it'],
    'gear2': ['a magnificent riding horse and gear', 'saddlebags', 'WEAPON: a sword', 'a week of rations',
              'a silver locket with a miniature painting of a dead girl inside it'],
    'gear3': [str(dice.roll(1,6)) + ' flasks of oil', str(dice.roll(1,6)) + ' vials of acid', 'WEAPON: a crowbar',
              'a hand mirror', 'ARMOUR: a leather jerkin (Light Armour, AC:13, Enc:1)', '6 torches', 'a tinderbox',
              'a set of tools (for the profession of your choice)',
              'and a small collection of hand-drawn pornography'],
    'gear4': ['2 bottles of wine', 'WEAPON: a dagger', 'a hammer', '12 iron spikes', 'a 2-person tent',
              '4 wooden stakes', 'a set of tools (for the profession of your choice)',
              'ARMOUR: a lamellar cuirass (Light Armour, AC:13, Enc:1)', '6 torches',
              'a sack', 'a tinderbox', str(dice.roll(1,6)) + ' cyphers worth of small coins in your pockets'],
    'gear5': ['an abacus', 'bank notes worth 20 cyphers', 'a small box of cigars', 'a box of matches',
              'WEAPON: a dagger', 'WEAPON: a sword', 'a map of the region', 'a random hireling',
              'a set of scales', 'a vial of holy water', 'a letter addressed to your father'],
    'gear6': [str(dice.roll(1,6)) + ' throwing axes', ch(['WEAPON: a flail', 'WEAPON: a morningstar']),
              'a pair of wineskins', 'ARMOUR: strange wooden armour (Heavy Armour, AC:15, Enc:2)', 'a pronounced foreign accent'],
    'gear7': ['6 books', 'a shoulderbag', 'WEAPON: a dagger', 'a lantern', 'a flask of oil', 'a magnifying glass',
              'WEAPON: a rapier',
              'a set of tools (for the academic profession of your choice)', 'a letter from home',
              '3 glass vials containing unknown chemicals'],
    'bard': ['1 musical instrument of your choice', 'a mask', 'a small, innocuous spellbook'],
    'champ_chaos': ['a book explicating your ideology', 'a small, innocuous spellbook'],
    'champ_evil': ['a book explicating your ideology'],
    'champ_good': ['a book explicating your ideology'],
    'champ_law': ['a book explicating your ideology'],
    'cultist': ['an inexpensive symbol of your cult', 'a piece of clothing that signifies your faith',
                'a small, innocuous spellbook'],
    'fighter': ['WEAPON: an extra close combat weapon of your choice', '2 weeks worth of rations'],
    'scholar': ['you always have at least 2 scholarly books', 'a small, innocuous spellbook'],
    'wizard': ['a small, innocuous spellbook'],
}

lesser = {
    'gear1': ['3 books about animals', 'WEAPON: a dagger', 'a man trap', 'a shoulderbag',
              'WEAPON: a short bow with 24 arrows', 'a quiver',
              'a magnificent cloak (made of feathers, perhaps) that soothes your wounded pride'],
    'gear2': [str(dice.roll(1,6)) + ' doses of antitoxin', '4 bombs', 'a tinderbox', '12 candles',
              'a handful of caltrops', '12 pieces of chalk', 'WEAPON: a dagger', 'a pot of glue',
              '12 heretical posters', 'a shoulderbag',
              'a heart made of stone, which anyone can see, if they look in your eyes'],
    'gear3': ['WEAPON: ' + str(dice.roll(1,6)) + ' throwing knives', '50 feet of rope, a grappling hook',
              'a set of tools (for the profession of your choice)', 'a purse of coins worth 25 cyphers',
              ch(['WEAPON: a well-crafted sword', 'ARMOUR: a heavy leather jerkin (Light Armour, AC:13, Enc:1)'])],
    'gear4': ['50 feet of silk rope', 'a backpack', 'WEAPON: a bastard sword', 'a book', 'a hand mirror',
              'a jar of beard oil',
              'manacles', 'ARMOUR: a shield (AC+1)', 'WEAPON: a silver dagger', 'a week of rations'],
    'gear5': [str(dice.roll(1,6)) + ' doses of poison', 'a bottle of expensive wine', 'WEAPON: a dagger',
              'WEAPON: a long bow with 24 arrows', 'a quiver', 'a make up kit',
              'a vial of perfume', 'a bad reputation'],
    'gear6': [str(dice.roll(1,6)) + ' doses of drugs', '12 sticks of incense', 'a lantern', '2 flasks of oil',
              'a tinderbox', 'a small hammer', '12 iron spikes', 'WEAPON: a sword cane', '6 pencils',
              'a notebook containing an earnest young man\'s surprisingly eloquent poetry'],
    'gear7': ['a compass', 'a hand mirror', 'a lantern', '2 flasks of oil', 'a tinderbox',
              'WEAPON: a magnificent-looking sword',
              'a notebook', '6 pencils', 'a pair of dice', 'dark, tousled hair',
              'the love of a foolish young maiden, smitten by that crown of thorns you wear', 'a bastard child'],
    'bard': [str(dice.roll(1,2)) + ' musical instruments', 'a book (on the topic of your choice)',
             'a well-made spellbook'],
    'champ_chaos': ['a fancy helmet', 'a well-made spellbook'],
    'champ_evil': ['a fancy helmet'],
    'champ_good': ['a fancy helmet'],
    'champ_law': ['a fancy helmet'],
    'cultist': ['an expensive symbol of your faith', 'a well-made spellbook'],
    'fighter': ['ARMOUR: Heavy Armour of your Choice except plate (Heavy Armour, AC:15, Enc:2)'],
    'scholar': ['a shoulderbag', '3 tomes devoted to obscure philosophical subjects', 'a well-made spellbook'],
    'thief': ['thieves\' tools'],
    'wizard': ['a well-made spellbook'],
}

greater = {
    'gear1': ['compromising letters intended for blackmail', 'WEAPON: a short sword',
              'a staff with a glowing globe on the top of it', 'a signet ring',
              'a bottle of ' + ch(['brandy', 'gin', 'rum']),
              'a terrible, pervasive ennui crushing your soul'],
    'gear2': ['a mule', 'a cart', ch(['WEAPON: a flail', 'WEAPON: a warhammer']), 'ARMOUR: a shield (AC+1)', 'a pipe',
              'a box of matches',
              'a bag of tobacco (or some other weed, your choice)', 'more regrets than you can count',
              'a dead man in your cart'],
    'gear3': ['WEAPON: a composite bow with 24 arrows', 'a quiver', 'a riding horse', 'riding horse gear',
              'light barding', 'a signet ring', 'WEAPON: a sword', 'a week of rations', 'a prominent scar'],
    'gear4': ['a backpack', '6 torches', 'a week of rations', ch(['WEAPON: a mace', 'WEAPON: a pole arm']),
              ch(
                  ['ARMOUR: a steel breastplate and helmet (Heavy Armour, AC:15, Enc:2)', 'a riding horse and riding gear'])],
    'gear5': [str(dice.roll(1,6)) + ' books', 'WEAPON: ' + str(dice.roll(1,6)) + ' pistols',
              '24 bullets and a powder horn', 'a \'magical\' amulet bought from a fortune teller',
              'a make up kit', 'a shoulderbag', 'a wineskin',
              'a wooden case with a vial of ink, 12 pieces of paper, and 12 quills in it'],
    'gear6': ['a backpack', 'a bedroll', 'a fishing pole', 'a pound of lard', 'a random hireling', 'WEAPON: a rifle',
              '24 bullets and a powder horn', 'a letter reminding you how disappointed in you your family is'],
    'gear7': ['WEAPON: the close combat weapon of your choice', '6 bandages', '12 candles', 'a tinderbox', 'a pony',
              'a saddle',
              'a ring that was a handsome young man\'s gift (to you or someone else, your choice)'],
    'assassin': ['WEAPON: a light crossbow with 24 bolts', 'a quiver'],
    'bard': ['up to 3 books (on the topics of your choice)', 'a large and ostentatious spellbook'],
    'champ_chaos': ['a signet ring', 'a large and ostentatious spellbook'],
    'champ_evil': ['a signet ring'],
    'champ_good': ['a signet ring'],
    'champ_law': ['a signet ring'],
    'cultist': ['an expensive symbol of your faith and a few pieces of clothing that reveal your cult allegiance',
                'a large and ostentatious spellbook'],
    'fighter': ['WEAPON: an ornate mace', ch(['WEAPON: a dagger', 'WEAPON: a throwing knife'])],
    'scholar': ['a large and ostentatious spellbook'],
    'thief': ['you are missing your ' + ch(
        ['pinky', 'ring finger', 'middle finger', 'index finger', 'thumb']) + 'on your ' + ch(
        ['left', 'right']) + 'hand'],
    'wizard': ['a large and ostentatious spellbook'],
}

royal = {
    'gear1': ['WEAPON: 3 pistols', '24 bullets and a powder horn', 'a signet ring',
              'a flouncy shirt that shows off your chest',
              'WEAPON: a poisoned dagger you took from the man who tried to kill you yesterday'],
    'gear2': [str(dice.roll(1,6)) + ' doses of antitoxin', '3 vials of holy water',
              'WEAPON: a light crossbow with 24 bolts', 'a quiver', 'a lantern', '2 flasks of oil',
              'a shovel', 'a small hammer', '12 iron spikes', 'a very fancy chess set'],
    'gear3': ['WEAPON: an axe', 'WEAPON: a dagger', 'WEAPON: a pole arm',
              str(dice.roll(1,6)) + ' doses of drugs (your choice of type)',
              '2 books (on the topics of your choice)', 'ARMOUR: a chainmail shirt (Light Armour, AC:13, Enc:1)', 'a signet ring',
              'a small, untrained monkey'],
    'gear4': ['some bandages', 'a book', 'a bottle of wine', 'WEAPON: a dagger', 'a pouch of coins worth 15 cyphers',
              'a riding horse', 'riding horse gear', 'saddlebags', 'a signet ring', 'WEAPON: a sword',
              'a vial of perfume', 'a musical instrument of your choice'],
    'gear5': ['a belt pouch with a bundle of wolfsbane in it', 'WEAPON: a mace', 'ARMOUR: a shield (AC+1) with heraldry on it',
              'a warhorse',
              'warhorse gear (not barding)', 'a beautiful lock of hair tied in a ribbon'],
    'gear6': [str(dice.roll(1,6)) + ' doses of antitoxin', str(dice.roll(1,6)) + ' doses of drugs (your choice of type)',
              'WEAPON: the close combat weapon of your choice', 'WEAPON: a short bow with 12 arrows', 'a quiver',
              'a shoulderbag', '6 torches', 'a week of nasty-tasting rations', 'eyes that are different colours'],
    'gear7': ['a signet ring', 'WEAPON: a jewelled dagger', 'WEAPON: 2 weapons of your choice',
              'ARMOUR: the armour of your choice', 'an armoured warhorse', '2 weeks worth of rations',
              '50 feet of silk rope', 'a bedroll', 'a grappling hook',
              'a letter from the nightmare realm offering you a crown of your own should you agree to betray your royal kin'],
    'assassin': ['a trained dog', 'the blood of one of your relatives on your conscience'],
    'bard': ['a book of ' + ch(['songs', 'speeches']),
             'a spellbook' + ch([' bound in human skin', ' made of metal'])],
    'champ_chaos': ['a prophetic birth mark',
                    'a spellbook' + ch([' bound in human skin', ' made of metal'])],
    'champ_evil': ['a prophetic birth mark'],
    'champ_good': ['a prophetic birth mark'],
    'champ_law': ['a prophetic birth mark'],
    'cultist': ['a very expensive symbol of your faith', 'a holy book' + ch(
        [' bound in human skin', ' made of metal']) + ' which also contains your spells',
                'a fancy ceremonial costume'],
    'scholar': ['a spellbook', 'the journal of a famous ' + ch(['architect', 'heretic', 'philosopher']),
                'a spellbook' + ch([' bound in human skin', ' made of metal'])],
    'thief': [
        'a cursed item. You say what the item is and the GM decides what the horrible curse is. You cannot get rid of it.'],
    'wizard': ['a spellbook' + ch([' bound in human skin', ' made of metal'])],
}

'''
# to be added
feyknight = {}
halfling = {}
berserker = {}
disciple = {}s
'''

gearSets = {
    'wretched': wretched,
    'peasant': peasant,
    'poor': poor,
    'middle': middle,
    'lesser': lesser,
    'greater': greater,
    'royal': royal,
}

def gear_tier(roll):
    if roll == 18:
        tier = 'gear7'
    elif roll >= 16:
        tier = 'gear6'
    elif roll >= 13:
        tier = 'gear5'
    elif roll >= 9:
        tier = 'gear4'
    elif roll >= 6:
        tier = 'gear3'
    elif roll >= 4:
        tier = 'gear2'
    else:
        tier = 'gear1'
    return tier

def get_gear(prof, status):
    index = dice.roll(3, 6)
    tier = gear_tier(index)
    gearList = list(filter(None, gearSets[status][tier]))
    if prof in gearSets[status]:
        bonusGear = list(gearSets[status][prof])
        for each in bonusGear:
            gearList.append(each)
    return gearList

'''
# how to remove empty items from a list
newtestlist = list(filter(None, testlist))
'''

if __name__ == "__main__":
    prof = ch(['assassin', 'bard', 'champ_chaos', 'champ_evil', 'champ_good', 'champ_law', 'cultist', 'fighter', 'scholar', 'thief', 'wizard'])
    status = ch(['wretched', 'peasant', 'poor', 'middle', 'lesser', 'greater', 'royal'])
    myList = get_gear(prof, status)
    weapons = list(filter(lambda x: x.startswith('WEAPON: '), myList))
    armour = list(filter(lambda x: x.startswith('ARMOUR: '), myList))
    print(prof)
    print(status)
    for x in weapons:
        print(x)
        myList.remove(x)
    for x in armour:
        print(x)
        myList.remove(x)
    for x in myList:
        print(x)


