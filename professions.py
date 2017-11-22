"""
FLAGS:
note that some are one-or-the-other pairs
these are pulled together into a special new list during initial class generator
checks are made against that list "if word in list, then do sub-function" etc

(required)
base/advanced   = designates what source material the class is from
human/demi      = are they human or demihuman (for "race as class" games

(optional)
caster          = designates the class as starting with magic
subclass        = has special subclass stuff, like with demihumans
haspa           = class has psychic armor

alignments options:
'chaos', 'evil', 'good', 'law', 'neutral'

"attacksAs" options:
best    = best bonuses in the game              (+17 bnt, +23 dd)
mid-hi  = just above mid-ter for some games     (+15 bnt)
mid     = mid-tier attack bonuses               (+13 bnt, +18 dd)
mid-lo  = just below mid-tier for some games    (+9 bnt)
worst   = worst bonuses in the game             (+7 bnt, +8 dd)
none    = absolutely no level-based bonuses! to combat!
NOTE!: at least in base TNU, characters all use either best or none
NOTE2: My long term plan if I add level selector is to work some code wizardry which is based on
automagically spreading the bonuses out across the base system's total levels.

Weapon/Armor selection options:
clr = selects as cleric
hlf = selects as halfling
mag = selects as mage
mnk = selects as monk
rog = selects as rogue
war = selects as warrior

"""

import random
# import systems

skills = {
    'bnt': [
        'Balance (DEX)',
        'Bend bars (STR)',
        'Break down doors (STR)',
        'Climb sheer surfaces (STR)',
        'Decipher codes (INT)',
        'Escape bonds (DEX)',
        'Find secret doors (INT)',
        'Find traps (INT)',
        'Hide in shadows (DEX)',
        'Jump (STR)',
        'Listen at doors (WIS)',
        'Move silently (DEX)',
        'Open locks (DEX)',
        'Pick pockets (DEX)',
        'Remove traps (DEX)',
        'Riding (DEX)',
        'Survival (WIS)',
        'Swimming (STR)',
        'Tracking (WIS)',
        'Trickery (CHA)'
    ],
    'dd': [
        'Arcane Lore (Int)',
        'Balance (Dex)',
        'Bluff (Cha)',
        'Cooking (Wis)',
        'Craft (Choice of Medium) (Dex)',
        'Diplomacy (Cha)',
        'Disguise (Cha)',
        'Engineering (Int)',
        'Escape Artist (Dex)',
        'Etiquette (Choice of Culture) (Cha)',
        'First Aid (Wis)',
        'Gambling (Cha)',
        'Geography (Int)',
        'History (Int)',
        'Intimidation (Str or Cha)',
        'Jumping (Str)',
        'Language (Choice) (Special)',
        'Laws (Choice of Culture) (Int)',
        'Lip Reading (Wis)',
        'Magical Engineering (Int)',
        'Nature Lore (Int)',
        'Navigating (Wis)',
        'Performance (Choice of Medium) (Cha)',
        'Religious Lore (Int)',
        'Riding (Choose Animal) (Dex)',
        'Sense Motive (Wis)',
        'Swimming (Str)',
        'Tracking (Wis)'
    ]
}

bnt_profs = {
    'default': {
        'short': 'default',                     # STR: class name for references
        'long': 'Default Class name',           # STR: class name for display
        'flags': ['base'],                      # LIST of flags for different effects
        'level': 1,                             # INT: right now only used for # of spells mastered
        'nextXP': '2000',                       # STR: amount of XP needed for next level
        'hd': 6,                                # INT: The Hit Die of the class
        'primAttr': [],                         # LIST of one or two stats for high stat roll assignments
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],    # LIST of allowed alignments for random choice
        'attacksAs': 'mid',                     # STRING: what category of combat bonuses
        'weapons': 'war',                       # STR: Category of weapons allowed as choices
        'armour': 'war',                        # STR: Category of armours allowed as choices
        'spellChooseAs': '',                    # STRING: if caster, usually = short
        'spellsPerLvl': 0,                      # INT: if caster, how many spell choices per level
        'cantrips': False,                      # either False or INT: num of cantrips at first level
        'casterStat': '',                       # STRING: stat used for spells, if a caster
        'saves': [15, 13, 15],                  # LIST of 3 integers, in order
        'skills': ['Placeholder for Skills'],   # LIST of skills for the class
        'restrictions': ['Placeholder for Restrictions'],   # Unsure, placeholder
        'special': ['Placeholder for Special Abilities'],   # Unsure, placeholder
        'extragear': False,                     # either False or LIST: some professions have extra gear, put it here
        'extraspells': False,                   # either False or some magicians get free spells plus their choices
    },
    'assassin': {
        'short': 'assassin',
        'long': 'Assassin',
        'flags': ['advanced'],
        'nextXP': '1500',
        'primAttr': ['DEX', 'INT'],
        'alignAllowed': ['chaos', 'evil', 'law', 'neutral'],
        'weapons': 'rog',
        'armour': 'rog',
        'skills': ['Climb sheer surfaces (STR)', 'Decipher codes (INT)', 'Escape bonds (DEX)',
                   'Hide in shadows (DEX)', 'Listen at doors (WIS)', 'Move silently (DEX)', 'Trickery (CHA)'],
    },
    'barbarian': {
        'short': 'barbarian',
        'long': 'Barbarian',
        'flags': ['advanced'],
        'hd': 10,
        'primAttr': ['STR', 'CON'],
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'attacksAs': 'mid-hi',
        'weapons': 'war',
        'armour': 'war',
        'saves': [13, 13, 15],
        'skills': ['Bend bars (STR)', 'Break down doors (STR)', 'Climb sheer surfaces (STR)', 'Jump (STR)',
                   'Survival (WIS)', 'Swimming (STR)'],
    },
    'bard': {
        'short': 'bard',
        'long': 'Bard',
        'flags': ['advanced'],
        'nextXP': '1500',
        'primAttr': ['CHA', 'INT'],
        'attacksAs': 'mid',
        'weapons': 'rog',
        'armour': 'rog',
        'spellChooseAs': 'bard',
        'cantrips': 4,
        'casterStat': 'CHA',
        'saves': [15, 13, 13],
        'extragear': ['a musical instrument of choice'],
        'skills': ['Decipher codes (INT)', 'Listen at doors (WIS)', 'Pick pockets (DEX)', 'Trickery (CHA)'],
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'nextXP': '2000',
        'primAttr': ['WIS'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law'],
        'attacksAs': 'mid',
        'weapons': 'clr',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 1,
        'cantrips': 3,
        'casterStat': 'WIS',
        'saves': [13, 15, 13],
        'extragear': ['a Holy Symbol of your Faith'],
        'skills': ['Decipher codes (INT)', 'Riding (DEX)'],
    },
    'duelist': {
        'short': 'duelist',
        'long': 'Duelist',
        'flags': ['advanced'],
        'hd': 8,
        'primAttr': ['DEX', 'INT'],
        'attacksAs': 'best',
        'armour': 'rog',
        'skills': ['Balance (DEX)', 'Jump (STR)'],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'skills': ['Bend bars (STR)', 'Break down doors (STR)', 'Riding (DEX)'],
    },
    'mu': {
        'short': 'magic-user',
        'long': 'Magic-User',
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['INT'],
        'attacksAs': 'worst',
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 1,
        'cantrips': 3,
        'casterStat': 'INT',
        'saves': [15, 15, 13],
        'extragear': ['a Spell Book'],
        'extraspells': ['Read Magic'],
        'skills': ['Decipher codes (INT)', 'Find secret doors (INT)'],
    },
    'paladin': {
        'short': 'paladin',
        'long': 'Paladin',
        'flags': ['advanced'],
        'nextXP': '2500',
        'hd': 8,
        'primAttr': ['STR', 'WIS', 'CHA'],
        'alignAllowed': ['good', 'law'],
        'attacksAs': 'mid-hi',
        'saves': [12, 14, 12],
        'skills': ['Riding (DEX)'],
    },
    'ranger': {
        'short': 'ranger',
        'long': 'Ranger',
        'flags': ['advanced'],
        'nextXP': '2500',
        'hd': 8,
        'primAttr': ['STR', 'WIS'],
        'alignAllowed': ['good', 'law', 'neutral'],
        'attacksAs': 'mid-hi',
        'saves': [13, 13, 15],
        'skills': ['Climb sheer surfaces (STR)', 'Hide in shadows (DEX)', 'Move silently (DEX)',
                   'Survival (WIS)', 'Swimming (STR)', 'Tracking (WIS)'],
    },
    'sorc': {
        'short': 'sorcerer',
        'long': 'Sorcerer',
        'flags': ['advanced'],
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['CHA'],
        'attacksAs': 'worst',
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 3,
        'cantrips': 5,
        'casterStat': 'CHA',
        'saves': [15, 15, 13],
        'extraspells': ['Read Magic'],
        'skills': ['Trickery (CHA)'],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'nextXP': '1500',
        'primAttr': ['DEX'],
        'weapons': 'rog',
        'armour': 'rog',
        'extragear': ['Thieves\' Tools'],
        'skills': ['Climb sheer surfaces (STR)', 'Decipher codes (INT)', 'Escape bonds (DEX)',
                   'Find secret doors (INT)', 'Find traps (INT)', 'Hide in shadows (DEX)',
                   'Listen at doors (WIS)', 'Move silently (DEX)', 'Open locks (DEX)',
                   'Pick pockets (DEX)', 'Remove traps (DEX)'],
    },
}

dd_profs = {
    'default': {
        'short': 'default',                     # STR: class name for references
        'long': 'Default Class name',           # STR: class name for display
        'flags': ['base', 'human'],             # LIST of flags for different effects
        'level': 1,                             # INT: right now only used for # of spells mastered
        'nextXP': '2000',                       # STR: amount of XP needed for next level
        'hd': 6,                                # INT: The Hit Die of the class
        'primAttr': [],                         # LIST of one or two stats for high stat roll assignments
        'alignAllowed': ['chaos', 'law', 'neutral'],    # LIST of allowed alignments for random choice
        'attacksAs': 'mid',                     # STRING: what category of combat bonuses
        'wps': 2,                               # INT: How many starting Weapon Proficiencies
        'weapons': 'war',                       # STR: Category of weapons allowed as choices
        'armour': 'war',                        # STR: Category of armours allowed as choices
        'spellChooseAs': '',                    # STRING: if caster, usually = short
        'spellsPerLvl': 0,                      # INT: if caster, how many spell choices per level
        'casterStat': '',                       # STRING: stat used for spells, if a caster
        'cantrips': False,                      # either False or INT: num of cantrips at first level
        'saves': [12, 13, 14, 15, 16],          # LIST of 5 integers, in order
        'skills': list(random.sample(skills['dd'], 4)),     # LIST of skills chosen from the core book
        'restrictions': ['Placeholder for Restrictions'],   # Unsure, placeholder
        'special': ['Placeholder for Special Abilities'],   # Unsure, placeholder
        'extragear': False,                     # either False or LIST: some professions have extra gear, put it here
        'extraspells': False,                   # either False or some magicians get free spells plus their choices
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '1500',
        'primAttr': ['WIS'],
        'weapons': 'clr',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 2,
        'casterStat': 'WIS',
        'saves': [11, 12, 14, 16, 15],
        'extragear': ['a Holy Symbol'],
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'flags': ['base', 'demi'],
        'nextXP': '2200',
        'hd': 8,
        'primAttr': ['CON', 'STR'],
        'attacksAs': 'best',
        'wps': 4,
        'saves': [8, 9, 10, 13, 12],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'flags': ['base', 'demi', 'caster'],
        'nextXP': '4000',
        'primAttr': ['STR', 'INT'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [12, 13, 13, 15, 15],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'wps': 4,
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'CON'],
        'weapons': 'hlf',
        'saves': [8, 9, 10, 13, 12],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['INT'],
        'attacksAs': 'worst',
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [13, 14, 13, 16, 15],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'flags': ['base', 'human'],
        'nextXP': '1200',
        'hd': 4,
        'primAttr': ['DEX'],
        'weapons': 'rog',
        'armour': 'rog',
        'saves': [13, 14, 13, 16, 15],
        'extragear': ['a Set of Thieves\' Tools'],
    },
}

pla_profs = {}

tnu_profs = {
    'default': {
        'short': 'default',                     # STR: short name for frequent use in this code
        'long': 'Default Class Name',           # STR: Display Name
        'flags': [],                            # LIST of flags for different effects
        'level': 1,                             # INT: right now only used for # of spells mastered
        'hd': 8,                                # INT: hit dice for calculations
        'primAttr': [],                         # LIST of one or two stats for high stat roll assignments
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],    # LIST of allowed alignments for random choice
        'attacksAs': 'none',                    # STRING: what category fo combat bonuses
        'spellChooseAs': '',                    # STRING: if caster, usually = short
        'spellsPerLvl': 0,                      # INT: if caster, how many spell choices per level
        'casterStat': '',                       # STRING: stat used for spells, if a caster
        'cantrips': False,                      # either False or INT: num of cantrips at first level
        'skills': ['Placeholder for Skills'],   # Unsure, placeholder as I figure out skills. Might go unused.
        'restrictions': ['Placeholder for Restrictions'],   # Unsure, placeholder
        'special': ['Placeholder for Special Abilities'],   # Unsure, placeholder
        'extragear': False,                     # either False or LIST: some professions have extra gear, put it here
        'extraspells': False,                   # either False or some magicians get free spells plus their choices
    },
    'assassin': {
        'short': 'assassin',
        'long': 'Assassin',
        'primAttr': ['DEX', 'FER'],
        'alignAllowed': ['chaos', 'evil', 'law', 'neutral'],
        'attacksAs': 'best',
        'special': [
            'Add your level to your attack rolls.',
            'When you take someone by surprise or attack them from behind, you automatically hit and '
            'inflict your damage twice, as if you had made two successful attacks.',
            'You may add your Dexterity modifier to surprise rolls you make, instead of your '
            'Intelligence modifier, if it is higher.',
            'Your Armour rating is equal to 10 + your level, as long as you wear no armour.',
        ],
    },
    'bard': {
        'short': 'bard',
        'long': 'Bard',
        'flags': ['base', 'human', 'caster'],
        'hd': 6,
        'primAttr': ['CHA', 'HEA'],
        'alignAllowed': ['chaos', 'good', 'law', 'neutral'],
        'spellChooseAs': 'bard',
        'spellsPerLvl': 1,
        'casterStat': 'CHA',
        'special': [
            'As a complicated combat action, you may give your Disposition away to your allies. For each '
            'point of Disposition you lose, one other character who can see, hear, or touch you gains 2 '
            'points of Disposition. However much Disposition you choose to lose, up to your total current '
            'score, you may distribute amongst other characters as you see fit.',
            'When you re-roll your Disposition, any allies who also re-roll their Disposition get advantage. '
            'You may decide who is an ally and who is not at any time.',
            'You are a Spellcaster. When you cast a spell that you have mastered, roll against your Charisma '
            'score instead of your Intelligence in order to control it (when casting a spell from a formula '
            'you have not mastered, roll against Intelligence as normal).',
        ],
    },
    'champ_chaos': {
        'short': 'champ_chaos',
        'long': 'Champion of Chaos',
        'flags': ['base', 'human', 'caster'],
        'primAttr': ['HEA', 'INT'],
        'alignAllowed': ['chaos'],
        'attacksAs': 'best',
        'spellChooseAs': 'champ_chaos',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'extragear': ['RANDOM_d6 doses of hallucinogenic cactus'],
        'special': [
            'Add your level to your attack rolls.',
            'During a rest, you can give anyone else who shares your alignment advantage when they '
            're-roll their Disposition or Psychic Armour.',
            'You always know when magic in your presence requires or targets your alignment.',
            'You always know when someone in your presence shares your alignment.',
            'You are a Spellcaster. You are unable to cast, master, or memorize spells from the school of Law.',
        ],
    },
    'champ_evil': {
        'short': 'champ_evil',
        'long': 'Champion of Evil',
        'flags': ['base', 'human'],
        'primAttr': ['HEA', 'FER'],
        'alignAllowed': ['evil'],
        'attacksAs': 'best',
        'extragear': ['WEAPON: an additional close combat weapon from your special list'],
        'special': [
            'Add your level to your attack rolls.',
            'During a rest, you can give anyone else who shares your alignment advantage when they '
            're-roll their Disposition or Psychic Armour.',
            'You always know when magic in your presence requires or targets your alignment.',
            'You always know when someone in your presence shares your alignment.',
            'Choose one type of weapon from the following list for each level you have: axes, bows and arrows, '
            'clubs and maces, daggers and knives, firearms, garrotes, picks and hammers, pole arms and spears, '
            'swords, and thrown weapons (other categories do not include thrown weapons of the same type). '
            'When you attack with a weapon of your chosen type, you inflict your damage twice, as if you had '
            'made two successful attacks.',
        ],
    },
    'champ_good': {
        'short': 'champ_good',
        'long': 'Champion of Good',
        'flags': ['base', 'human'],
        'primAttr': ['HEA', 'CHA'],
        'alignAllowed': ['good'],
        'attacksAs': 'best',
        'extragear': ['RANDOM_d6 doses of antitoxin', 'RANDOM_d6 uses of bandages'],
        'special': [
            'Add your level to your attack rolls.',
            'During a rest, you can give anyone else who shares your alignment advantage when they '
            're-roll their Disposition or Psychic Armour.',
            'You always know when magic in your presence requires or targets your alignment.',
            'You always know when someone in your presence shares your alignment.',
            'As a complicated combat action, you may give your Disposition away to your allies. '
            'For each point of Disposition you lose, one other character who can see, hear, or touch you '
            'gains 2 points of Disposition. However much Disposition you choose to lose, up to your total '
            'current score, you may distribute amongst other characters as you see fit.',
        ],
    },
    'champ_law': {
        'short': 'champ_law',
        'long': 'Champion of Law',
        'flags': ['base', 'human'],
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['law'],
        'attacksAs': 'best',
        'extragear': ['a written copy of The Law'],
        'special': [
            'Add your level to your attack rolls.',
            'During a rest, you can give anyone else who shares your alignment advantage when they '
            're-roll their Disposition or Psychic Armour.',
            'You always know when magic in your presence requires or targets your alignment.',
            'You always know when someone in your presence shares your alignment.',
            'You have a spiritual enemy, that you may banish from your presence as a simple action. '
            'Choose one of the following: beasts, dwellers in the deep, faeries, golems, '
            'or the undead (See p. 73 TNU).',
        ],
    },
    'cultist': {
        'short': 'cultist',
        'long': 'Cultist',
        'flags': ['base', 'human', 'caster'],
        'hd': 6,
        'primAttr': ['HEA', 'WIL'],
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'attacksAs': 'best',
        'spellChooseAs': 'cultist',
        'spellsPerLvl': 2,
        'casterStat': 'WIL',
        'special': [
            'You are a Spellcaster.',
            'Add your level to your attack rolls (unless you are using a restricted weapon or '
            'wearing restricted armour).',
            'You have a spiritual enemy, that you may banish from your presence as a simple action. '
            'Choose one of the following: beasts, dwellers in the deep, faeries, golems, humans, '
            'or the undead (See p. 73 TNU).',
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'primAttr': ['FER', 'HEA'],
        'attacksAs': 'best',
        'special': [
            'Add your level to your attack rolls.',
            'Armour does not count as encumbering items to you, as long as you are wearing it (but shields do).',
            'When you attack an enemy, if your attack roll is a miss, you still inflict your damage as normal, '
            'and if your attack roll is good enough to hit, you inflict your damage twice, as if you had made '
            'two successful attacks.',
        ],
    },
    'scholar': {
        'short': 'scholar',
        'long': 'Scholar',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'hd': 4,
        'primAttr': ['CHA', 'INT'],
        'alignAllowed': ['evil', 'good', 'law', 'neutral'],
        'spellChooseAs': 'scholar',
        'spellsPerLvl': 1,
        'casterStat': 'INT',
        'special': [
            'You are a Spellcaster.',
            'During a short or long rest, you may heal another person, restoring 1d4 points to one of their '
            'attributes that has been temporarily reduced. You may not treat the same person again until they '
            'are harmed again, but you may treat a total number of people each day equal to your level (if you '
            'spend an hour on each).',
            'You always find hidden things when you spend a turn searching a dungeon of your level or lower, '
            'and you always roll against your full Dexterity score when you search a higher-level dungeon '
            '(instead of half your Dexterity).',
            'You can use any magic item and gain its full benefits, regardless of alignment, profession, '
            'or other restrictions.',
            'You have Psychic Armour. Roll a number of Hit Dice (d4s) equal to your level and add them together '
            'to determine your Psychic Armour score, just as you do for Disposition. You are not required to '
            're-roll this score when you take a rest, but you may, if you like.',
        ],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'hd': 6,
        'primAttr': ['DEX'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'special': [
            'When you search an area in haste, if the dungeon level is equal to your level or lower, '
            'you must roll equal to or lower than your Dexterity score on a d20 to find hidden things. '
            'If the dungeon level is higher than your own, you must roll equal to or lower than half your '
            'Dexterity score, rounded down, on a d20 to find hidden things.',
            'You always find hidden things when you spend a turn searching a dungeon of your level or lower, '
            'and you always roll against your full Dexterity score when you search a higher-level dungeon '
            '(instead of half your Dexterity).',
        ],
    },
    'wizard': {
        'short': 'wizard',
        'long': 'Wizard',
        'flags': ['base', 'human', 'caster', 'haspa'],
        'hd': 4,
        'primAttr': ['INT', 'WIL'],
        'spellChooseAs': 'wizard',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'special': [
            'You are a Spellcaster.',
            'When you cast a spell and fail to control it, you may choose to ignore your failed roll and lose '
            '1d4 points of Willpower instead. If this does not reduce your Willpower to zero, you retain control '
            'over your spell.',
            'When you cast a spell, whether you retain control or not, you may roll to keep it in your memory, '
            'instead of forgetting it. To remember a spell of your level or lower, you must roll equal to or '
            'lower than your Willpower score on a d20. To remember a spell of a level higher than your character, '
            'you must roll equal to or lower than half your Willpower score, rounded down, on a d20.',
            'You have Psychic Armour. Roll a number of Hit Dice (d4s) equal to your level and add them together to '
            'determine your Psychic Armour score, just as you do for Disposition. You are not required to '
            're-roll this score when you take a rest, but you may, if you like.',
        ],
    },
}


'''
fey_knight = {}
halfling = {}
berserker = {}
disciple = {}

TO ADD:
tnu racial_profs = [fey_knight, halfling]
tnu optional_profs = [berserker, disciple]
'''


base_profs_tnu = [
    'assassin', 'bard',
    'champ_chaos', 'champ_evil', 'champ_good', 'champ_law',
    'cultist', 'fighter', 'scholar', 'thief', 'wizard'
]


# I don't do druids or monks, they're a pain in the ass
proflists = {
    'bnt': {
        'choices': [
            'assassin', 'barbarian', 'bard', 'cleric', 'duelist',
            'fighter', 'mu', 'paladin', 'ranger', 'sorc', 'thief',
        ],
        'dict': bnt_profs,
    },
    'dd': {
        'choices': [
            'cleric', 'elf', 'dwarf', 'fighter', 'halfling', 'mu', 'thief'
        ],
        'dict': dd_profs,
    },
    'tnu': {
        'choices': [
            'assassin', 'bard',
            'champ_chaos', 'champ_evil', 'champ_good', 'champ_law',
            'cultist', 'fighter', 'scholar', 'thief', 'wizard'
        ],
        'dict': tnu_profs,
    },
    'template': {
        'choices': [],
        'dict': '',
    },
}


# this returns a random character profession and all its base data
def get_profession(system='tnu'):
    my_list = proflists[system]['choices']
    my_dict = proflists[system]['dict']
    prof_data = my_dict['default']
    prof_spec = my_dict[random.choice(my_list)]
    prof_data.update(prof_spec)
    return prof_data


'''
def get_system_prefs(system='tnu'):
    sysprefs = dict(systems['default'])
    specific = dict(systems[system.lower()])
    sysprefs.update(specific)
    return sysprefs
'''


'''
for key, value in dict.items(get_profession()):
    print(key, ":", value)
'''


if __name__ == "__main__":
    for key, value in dict.items((get_profession('dd'))):
        print(key, ":", value)
