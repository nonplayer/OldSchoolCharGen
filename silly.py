"""
a collection of silly optional descriptors added to the game
"""

silly = {
    'gear': [
        'crippling apathy', 'twitchy eyes', 'a Certain "je ne sais quoi"', 'a love of horrible puns',
        'a feeling of general loathing for everyone around you', 'a case of the wiggles', 'wanderlust in your heart',
        'an independent streak', 'the first love letter anyone every wrote you', 'a sack full of bandit ears',
        'a regrettable haircut', 'chronic silent but deadly gas', 'curious pocket lint', 'inappropriate laughing',
        'a first edition manuscript of "Winter\'s Sullen Cry"', 'all of your nail clippings, ever',
        'an irritable tabby cat', 'a map to an island that doesn\'t exist', 'a pure white badger pelt',
        'a set of pornographic goblin trading cards', 'a single strip of slightly used sandpaper',
        'a petrified dragon egg', 'a lock of hair from your mother or father', 'a fake beard',
        'rusted nipple clamps', 'two weird puppets', '1D6 commemorative plates',
        'a bottle of freshly-harvested llama milk', 'a free drink coupon for the Inn, but it expires soon...',
        'a tendency to insert yourself into conversations', 'unsettling memories from last night',
        'a strong distrust for the government', 'an unsettlingly sexy facial scar',
        'a free spirit that cannot be shackled by despair', 'an obviously fake accent',
        'a feeling like you forgot something very important before heading out...',
        'a case of the wiggles', 'a recently-unlocked chastity belt',
        'a letter of recommendation from someone important', 'a tourist brochure for the dungeon',
        'a signed Maseym\'s Bears Base-Ball', 'an undislodgeable wedgie',
        'a very nice fitted suit', 'a scrap of finely-groomed gnoll hair',
        'a visible tattoo that you deeply regret', 'a massive debt of back rent',
        'an unbreakable padlock that can never be opened once clicked (currently open)',
        'shame, so much shame', 'the constant doting of your parents',
        'the knowledge that you recently betrayed someone in the party', 'a conspicuously dead parrot',
        'a strong craving for pot pies', 'a rock in a sock', 'a student loan disbursement check (requires Bank)',
    ],
    'langs': [
        'Gibberish', 'Esperanto', 'Pidgin (Pick 2)', 'Pigeon', 'Teenager',
    ],
    'skills': [
        'Art Criticism (INT)', 'Being Drunk Before Noon (CON)', 'Being Forgotten (CHA)',
        'Birdwatching (WIS)', 'Blathering (CHA)', 'Bobsledding (STR)',
        'Bonsai (DEX)', 'Bovine Husbandry (INT)', 'Busking (CHA)', 'Cat Facts (INT)',
        'Chess (INT)', 'Dog Grooming (DEX)', 'Doomsaying (WIS)', 'Dramatic Flexing (STR)',
        'Equine Husbandry (INT)', 'Feline Husbandry (INT)', 'Food Cart Management (INT)',
        'Food Tasting (CON)', 'Freestyle Beats (CHA)', 'Funny Walks (DEX)',
        'Getting Picked Last (CHA)', 'Gourmand (INT)', 'Hookah Repair (DEX)', 'Horsehair Braiding (DEX)',
        'Hullabaloo (CHA)', 'Landscaping (STR)', 'Limericks (CHA)',
        'Looking Conspicuous (CHA)', 'Milk (WIS)', 'Mime (DEX)',
        'Miniature Equine Aficionado (INT)', 'Multi-Level Marketing (INT)', 'Poison-Making (INT)',
        'Pouting (CHA)', 'Puppetry (DEX)', 'Selfies (CHA)',
        'SEO (INT)', 'Skiing (STR)', 'Spotlight Stealing (CHA)',
        'Squaredancing (DEX)', 'Stone-Skipping (DEX)', 'Surfing (DEX)',
        'Sword-Swallowing (CON)', 'The Heimlich Maneuver (STR)', 'Tightrope-Walking (DEX)',
        'Ursine Husbandry (CON)', 'Useless Card Tricks (DEX)',
    ]
}


def get_silly_gear():
    gear_list = list(silly['gear'])
    return gear_list


def get_silly_skills():
    skills_list = list(silly['skills'])
    return skills_list


def get_silly_langs():
    langs_list = list(silly['langs'])
    return langs_list


def get_silly():
    silly_data = {
        'gear': get_silly_gear(),
        'skills': get_silly_skills(),
        'langs': get_silly_langs(),
    }
    return silly_data


if __name__ == "__main__":
    print(get_silly())
