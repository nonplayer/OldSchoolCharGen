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
mu-weapons      = (Hammercrawl) Generate a Magic-User Weapon for this character

alignments options:
'chaos', 'evil', 'good', 'law', 'neutral'

"attacksAs" options:
best    = best bonuses in the game              (+17 bnt, +23 dd, +15 ham)
mid-hi  = just above mid-ter for some games     (+15 bnt)
mid     = mid-tier attack bonuses               (+13 bnt, +18 dd, +7 ham)
mid-lo  = just below mid-tier for some games    (+9 bnt)
worst   = worst bonuses in the game             (+7 bnt, +8 dd, +5 ham)
none    = absolutely no level-based bonuses! to combat!     (+0 ham)
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
from random import choice as ch
from dice import roll as die

baseline = {
    'short': 'default',                     # STR: class name for references
    'long': 'Default Class name',           # STR: class name for display
    'race': 'human',                        # STR: lowercase name, or "RANDOM" to trigger the random race function
    'level': 1,                             # INT: right now only used for # of spells mastered
    'hd': 6,                                # INT: The Hit Die of the class
    'primAttr': [],                         # LIST of one or two stats for high stat roll assignments
    'flags': ['base', 'human'],             # LIST of flags for different effects
    'nextXP': '2000',                       # STR: amount of XP needed for next level
    'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],    # LIST of allowed alignments for random choice
    'attacksAs': 'mid',                     # STRING: what category of combat bonuses
    'skills': [],                           # LIST of skills for the class
    'restrictions': ['Placeholder for Restrictions'],               # Unsure, placeholder
    'special': ['Placeholder for Special Abilities'],               # Unsure, placeholder
    'numAttacks': 1,                        # INT: number of attacks at first level
    'wps': False,                           # INT: How many starting Weapon Proficiencies
    'weapons': 'war',                       # STR: Category of weapons allowed as choices
    'armour': 'war',                        # STR: Category of armours allowed as choices
    'spellChooseAs': '',                    # STRING: if caster, usually = short
    'spellsPerLvl': 0,                      # INT: if caster, how many spell choices per level
    'cantrips': False,                      # either False or INT: num of cantrips at first level
    'casterStat': '',                       # STRING: stat used for spells, if a caster
    'extraspells': False,                   # either False or some magicians get free spells plus their choices
    'saves': False,                         # FALSE or else a LIST of integers, in order
    'extragear': [],                        # either False or LIST: some professions have extra gear, put it here
    'extralangs': [],                       # LIST if any bonus languages come with the class
}

def_profs = {
    'default': {},
    'fighter': {}
}

bnt_profs = {
    'default': {
        'flags': ['base'],
        'race': 'RANDOM',
        'saves': [15, 13, 15],
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
        'special': [
            '(Class) Trained in Poison use',
            '(Class) Advantage on Poison Saves.',
            '(Class) Backstab (x2 damage; can be ranged if less than 30 ft.)',
        ],
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
        'special': [
            '(Class) Land Speed base is +10 ft over racial.',
            '(Class) Rage 1x/Day (2 attacks, -2 AC, +2 Save vs Mind/Holds, lasts up to 6 rounds, fatigued after)',
            '(Class) Sixth Sense (no additional effects from surprise, flanking, attacks, or invisible attacks)',
        ],
    },
    'bard': {
        'short': 'bard',
        'long': 'Bard',
        'flags': ['advanced', 'caster'],
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
        'special': [
            '(Class) Spellcaster (Bard List, must prepare, can learn)',
            '(Class) Bard Knowledge (Will save, learns about local notables, legendary items or noteworthy places).',
            '(Class) Bard Music 1x/day (Fascination Effect)',
        ],
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['caster'],
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
        'special': [
            '(Class) Spellcaster (Cleric List, must prepare, must pray)',
            '(Class) Turn/Rebuke Undead (based on alignment)',
        ],
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
        'special': [
            '(Class) Specialist Weapon, One of Choice (2x damage on all attacks, tactical advantage)',
            '(Class) Add INT mod to AC if using one-handed melee weapon.',
            '(Class) Fight Defensively: +4 AC instead of usual +2',
            '(Class) +2 to Initiative Rolls',
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'skills': ['Bend bars (STR)', 'Break down doors (STR)', 'Riding (DEX)'],
        'special': [
            '(Class) Steadfast Defense Action: Give self +2 to savea and AC, deflect missiles, '
            'immunity to being moved/prone, but cannot move.',
        ],
    },
    'mu': {
        'short': 'magic-user',
        'long': 'Magic-User',
        'flags': ['caster'],
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
        'extraspells': ['Cantrip: Read Magic'],
        'skills': ['Decipher codes (INT)', 'Find secret doors (INT)'],
        'special': [
            '(Class) Spellcaster (Mage list, must prepare, can learn new)',
        ],
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
        'special': [
            '(Class) Cast "Detect Evil" at will.',
            '(Class) Smite Evil/Chaos 3x/day (2x damage, or 3x if target is a chaotic outsider)',
        ],
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
        'special': [
            '(Class) Sworn Foe: 2x Damage, +3 to Track Against ' + ch([
                'Animals', 'dragons', 'elementals', 'fey', 'giants', 'oozes', 'outsiders', 'plants',
                'undead', 'goblins', 'magical beasts', 'aberrations', 'monstrous humanoids',
                ch([
                    'bulettes', 'rust monsters', 'beholders', 'dinosaurs',
                    'dragons', 'unicorns', 'constructs', 'tarrasques',
                ]),
            ]),
        ],
    },
    'sorc': {
        'short': 'sorcerer',
        'long': 'Sorcerer',
        'flags': ['advanced', 'caster'],
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
        'skills': ['Trickery (CHA)'],
        'special': [
            '(Class) Spellcaster (Mage list, no preparation, cannot learn new).',
        ],
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
        'special': [
            '(Class) Backstab (x2 damage; can be ranged if less than 30 ft.)',
        ],
        'extralangs': ['Thieves\' Cant'],
    },
}

dd_profs = {
    'default': {
        'alignAllowed': ['chaos', 'law', 'neutral'],
        'wps': 2,
        'saves': [12, 13, 14, 15, 16, 16],
        'skills': 'RANDOM',
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '1500',
        'primAttr': ['WIS'],
        'restrictions': ['Clerics may wear any armour or shield, but may only use blunt weapons.'],
        'weapons': 'clr',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 1,
        'casterStat': 'WIS',
        'saves': [11, 12, 14, 16, 15, 15],
        'extragear': ['a Holy Symbol'],
        'special': [
            '(Class) Spellcaster (Cleric List)',
            '(Class) Turn Undead (based on Level, uses a 2d6 roll)',
        ],
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'race': 'dwarf',
        'flags': ['base', 'demi'],
        'nextXP': '2200',
        'hd': 8,
        'primAttr': ['CON', 'STR'],
        'attacksAs': 'best',
        'restrictions': ['Dwarves can wear any armour or shield, and can use any small or medium weapon. '
                         'They cannot use large weapons due to their stature.'],
        'wps': 4,
        'saves': [8, 9, 10, 13, 12, 12],
        'special': [
            '(Class) Heatvision',
            '(Class) Stonelore (1d6 roll, 2 or less finds details)',
        ],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'race': 'elf',
        'flags': ['base', 'demi', 'caster'],
        'nextXP': '4000',
        'primAttr': ['STR', 'INT'],
        'restrictions': ['Elves can wear any armour or shield, and can use any weapon.'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [12, 13, 13, 15, 15, 15],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'special': [
            '(Class) Spellcaster (Mage list)',
            '(Class) Heatvision',
            '(Class) Elfsight (find secret and hidden doors)',
            '(Class) Ghoul/Ghast Paralysis Immunity',
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'restrictions': ['Fighters can wear any armour or shield, and can use any weapon.'],
        'wps': 4,
        'special': [
            '(Class) Can use All Weapons and Armour without restriction',
        ],
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'race': 'halfling',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'CON'],
        'restrictions': ['Halflings can wear any armour or shield, and can use any small weapon. They cannot use '
                         'medium or large weapons due to their small stature.'],
        'weapons': 'hlf',
        'armour': 'hlf',
        'saves': [8, 9, 10, 13, 12, 12],
        'special': [
            '(Class) Small: -2 AC bonus vs creatures larger than humans.',
            '(Class) Nimble: +1 initiative, and +1 attack with ranged weapons.',
            '(Class) Unobtrusive: with proper cover and remaining still, 90%/33% chance to hide outdoors/indoors.',
        ],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['INT'],
        'attacksAs': 'worst',
        'restrictions': ['Magic-users may not wear armour or use shields and may not use most weapons. '
                         'The only weapons they may use are daggers, staves, slings, whips, pistols, '
                         'nets and blowguns.'],
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [13, 14, 13, 16, 15, 15],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'special': [
            '(Class) Spellcaster (Mage list)',
        ],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'flags': ['base', 'human'],
        'nextXP': '1200',
        'hd': 4,
        'primAttr': ['DEX'],
        'restrictions': ['Thieves may use any one-handed weapon, and may use leather armour. Since they must '
                         'travel lightly in order to use their abilities they may not use two-handed weapons '
                         'or shields. Thieves may use any missile weapon.'],
        'weapons': 'rog',
        'armour': 'rog',
        'saves': [13, 14, 13, 16, 15, 15],
        'extragear': ['a Set of Thieves\' Tools'],
        'special': [
            '(Class) Sneak Attack: +4 attack, x2 damage',
            '(Class) Thiefskill: Open Locks: 15',
            '(Class) Thiefskill: Find Traps: 10',
            '(Class) Thiefskill: Remove Traps: 10',
            '(Class) Thiefskill: Climb Walls: 87',
            '(Class) Thiefskill: Move Silently: 20',
            '(Class) Thiefskill: Hide in Shadows: 10',
            '(Class) Thiefskill: Pick Pockets: 20',
            '(Class) Thiefskill: Hear Noise: 30',
        ],
        'extralangs': ['Thieves\' Cant'],
    },
}

ddh_profs = {
    'default': {
        'alignAllowed': ['chaos', 'law', 'neutral', 'good', 'evil'],
        'wps': 2,
        'saves': [8, 7, 6, 5, 4, 4],
        'nextXP': '2000',
        'skills': 'RANDOM',
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster'],
        'primAttr': ['WIS'],
        'restrictions': ['Can use all weapons, shields, and armour that are not otherwise prohibited by your deity.',
                         'You cannot be of Neutral Alignment'],
        'weapons': 'clr',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 2,
        'casterStat': 'WIS',
        'saves': [9, 8, 6, 4, 5, 5],
        'extragear': ['a Holy Symbol'],
        'special': [
            '>>(Class) Spellcaster (Cleric List)',
            '>>(Class) Turn Undead (based on Level, see p. 25-27 DDX)',
        ],
    },
    'clock': {
        'short': 'clock',
        'long': 'Clockwork',
        'race': 'clockwork',
        'flags': ['base', 'demi', 'construct'],
        'primAttr': ['CON', 'STR'],
        'hd': 8,
        'wps': 4,
        'attacksAs': 'best',
        'saves': [12, 11, 10, 7, 8, 8],
        'restrictions': ['Clockworks cannot wear any armour..'],
        'armour': 'nil',
        'special': [
            '>>(Class) Artificial Body: Never sleeps; Immune to sleep, poison, fatigue, paralysis, nausea, and '
            'exhaustion. Does not naturally heal, instead requiring repairs or magic.',
            '>>(Class) Armoured: base natural AC of 7. Can be improved with time and money.',
            '>>(Class) Metal Fists: considered Armed at all times. Can be improved with time and money.',
        ],
    },
    'drawf': {
        'short': 'drawf',
        'long': 'Drawf',
        'race': 'drawf',
        'flags': ['base', 'demi'],
        'hd': 8,
        'primAttr': ['CON', 'STR'],
        'attacksAs': 'best',
        'restrictions': ['Can use all weapons, shields, and armour except longbows.'],
        'wps': 4,
        'saves': [12, 11, 10, 7, 8, 8],
        'extralangs': ['Drawf'],
        'special': [
            '>>(Class) Darkvision (B&W)',
            '>>(Class) Stonelore (special check to find details)',
        ],
    },
    'druid': {
        'short': 'druid',
        'long': 'Druid',
        'primAttr': ['WIS', 'CHA'],
        'flags': ['base', 'human', 'caster'],
        'restrictions': ['Druids may only wear leather armour, and only use weapons or shields made of wood '
                         'or other natural materials.'],
        'weapons': 'drd',
        'armour': 'rog',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 2,
        'casterStat': 'WIS',
        'saves': [9, 8, 6, 4, 5, 5],
        'extragear': ['a Symbol of Nature'],
        'special': [
            '>>(Class) Spellcaster (Druid List)',
            '>>(Class) Control Animals (based on Level, see p. 32-33 DDX)',
        ],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'race': 'elf',
        'flags': ['base', 'demi', 'caster'],
        'primAttr': ['DEX', 'INT'],
        'restrictions': ['Can use all weapons, shields, and armour. You suffer spell failure chances when armoured.'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [8, 7, 7, 5, 5, 5],
        'extragear': ['a Spellbook'],
        'extraspells': ['Red Magic'],
        'extralangs': ['Elf'],
        'special': [
            '>>(Class) Spellcaster (Mage list)',
            '>>(Class) Elfsight (find secret and hidden doors)',
            '>>(Class) Ghoul/Ghast Paralysis Immunity',
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR', 'CON'],
        'attacksAs': 'best',
        'restrictions': ['You can use all weapons, shields, and armour.'],
        'wps': 4,
        'special': [
            '>>(Class) *Not Today!* (one use) When you would take damage that would kill you, you can say "NOT TODAY!" '
            'and negate all of the damage from that attack. Gain more uses as you gain levels',
            '>>(Class) When leveling up, you reroll your Hit Points twice, and keep the best result.',
            '>>(Class) Bonus Proficiency: A Fighter begins play at "Skilled" mastery in two of their randomly '
            'rolled starting weapons.',
        ],
    },
    'halfogre': {
        'short': 'halfogre',
        'long': 'Half-Ogre Berzerker',
        'race': 'halfogre',
        'flags': ['base', 'demi'],
        'attacksAs': 'best',
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'hd': 8,
        'wps': 4,
        'primAttr': ['STR', 'CON'],
        'armour': 'brb',
        'saves': [6, 5, 4, 3, 2, 2],
        'extralangs': ['Ogre'],
        'restrictions': ['Can use all weapons and shields. Armour cannot be higher than Scale mail, and must be '
                         'custom made at 2x cost. You cannot be Law aligned.'],
        'special': [
            '>>(Class) Murderous Rage: Taking damage can activate Rage Mode (see house rules doc)',
            '>>(Class) You have heatvision, but only when in Rage Mode.',
            '>>(Class) Saves on the Fighter table at -2 (already calc\'d)',
            '>>(Class) Hungry: Requires twice as much food/rations as a normal character for all related purposes.',
            '>>(Class) Outcasts: Frequently socially ostracized in major civilised areas, often chased out of town.',
        ],
    },
    'hobbert': {
        'short': 'hobbert',
        'long': 'Hobbert',
        'race': 'hobbert',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'CON'],
        'restrictions': ['Can use all small weapons one-handed, or medium two-handed, and shields. Cannot use '
                         'two-handed human-sized weapons. All items are one size greater for Encumbrance limits. '
                         'Can wear any armor.'],
        'weapons': 'hlf',
        'armour': 'hlf',
        'saves': [12, 11, 10, 7, 8, 8],
        'extralangs': ['Hobbert'],
        'special': [
            '>>(Class) Small: -2 AC bonus vs creatures larger than humans.',
            '>>(Class) Nimble: +1 initiative to the team, and +1 attack with ranged weapons.',
            '>>(Class) Thiefskill: Move Silently: +3 (and an add. +10 when outdoors)',
            '>>(Class) Thiefskill: Hide in Shadows: +1 (and an add. +10 when outdoors)',
            '>>(Class) Thiefskill: Hear Noise: +5',
        ],
    },
    'lup': {
        'short': 'lup',
        'long': 'Lupine',
        'race': 'lupine',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'WIS'],
        'restrictions': ['Can use any weapon, but neither armour nor sheilds are allowed.'],
        'armour': 'nil',
        'extralangs': ['Lupine'],
        'special': [
            '>>(Class) Claws: 1d4 Damage, naturally proficient, leveled automatically, does not also Knockout.',
            '>>(Class) Base movement 40',
            '>>(Class) Thiefskill: Find Traps: +1',
            '>>(Class) Thiefskill: Remove Traps: +1',
            '>>(Class) Thiefskill: Climb Walls: +17',
            '>>(Class) Thiefskill: Move Silently: +3',
            '>>(Class) Thiefskill: Hide in Shadows: +1',
        ],
    },
    'mounte': {
        'short': 'mounte',
        'long': 'Mountebank',
        'primAttr': ['DEX', 'INT'],
        'flags': ['base', 'human', 'caster'],
        'restrictions': ['Can use all missile weapons, all 1-handed weapons, leather armour, bucklers, '
                         'and small shields. Wearing armour restricts spellcasting by adding a chance of failure. '
                         'Leather starts at 10%. Magic armour can reduce this.'],
        'weapons': 'rog',
        'armour': 'rog',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 1,
        'casterStat': 'INT',
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'special': [
            '>>(Class) Spellcaster (ALL lists, but Cleric/Druid spells are considered 1 level higher in learning)',
            '>>(Class) Weak Magic: caster level is considered 1/2 (up) for determining spell effects.',
            '>>(Class) Item use: can make use of any magical item usable by any mortal, without class restriction.',
            '>>(Class) Thiefskill: Climb Walls: +17',
            '>>(Class) Thiefskill: Move Silently: +3',
            '>>(Class) Thiefskill: Hide in Shadows: +1',
            '>>(Class) Thiefskill: Pick Pockets: +3',
            '>>(Class) Thiefskill: Bluff (NEW): +1',
            '>>(Class) Thiefskills: divide 2 more points among the above.',
        ],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster'],
        'hd': 4,
        'primAttr': ['INT', 'SOC'],
        'attacksAs': 'worst',
        'restrictions': ['Can not use two-handed weapons except staves. Can not wear armour or use shields.'],
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'saves': [7, 6, 7, 4, 5, 5],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'special': [
            '>>(Class) Spellcaster (Mage list)',
        ],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'flags': ['base', 'human'],
        'hd': 6,
        'primAttr': ['DEX'],
        'restrictions': ['Can use all missile weapons, all 1-handed weapons, leather armour, bucklers, '
                         'and small shields.'],
        'weapons': 'rog',
        'armour': 'rog',
        'saves': [7, 6, 7, 4, 5, 5],
        'extragear': ['a Set of Thieves\' Tools'],
        'special': [
            '>>(Class) Sneak Attack: +4 attack, x2 damage',
            '>>(Class) Thiefskill: Open Locks: +2',
            '>>(Class) Thiefskill: Find Traps: +1',
            '>>(Class) Thiefskill: Remove Traps: +1',
            '>>(Class) Thiefskill: Climb Walls: +17',
            '>>(Class) Thiefskill: Move Silently: +3',
            '>>(Class) Thiefskill: Hide in Shadows: +1',
            '>>(Class) Thiefskill: Pick Pockets: +3',
            '>>(Class) Thiefskill: Hear Noise: +5',
            '>>(Class) Thiefskill: Bluff (NEW): +1',
            '>>(Class) Thiefskills: divide 5 more points among the above, max of 3 more in any 1 thiefskill.',
            '>>(Class) Lucky: roll with advantage on all saving throw checks.',
        ],
        'extralangs': ['Thieves\' Cant'],
    },
}

ddx_profs = {
    'default': {
        'alignAllowed': ['chaos', 'law', 'neutral'],
        'wps': 2,
        'saves': [7, 6, 7, 4, 5, 5],
        'skills': 'RANDOM',
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'primAttr': ['WIS', 'CHA'],
        'saves': [9, 8, 6, 4, 5, 5],
    },
    'clock': {
        'short': 'clock',
        'long': 'Clockwork',
        'race': 'clockwork',
        'primAttr': ['STR', 'CON'],
        'saves': [12, 11, 10, 7, 8, 8],
    },
    'druid': {
        'short': 'druid',
        'long': 'Druid',
        'primAttr': ['WIS', 'CHA'],
        'saves': [9, 8, 6, 4, 5, 5],
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'race': 'dwarf',
        'primAttr': ['CON', 'STR'],
        'saves': [12, 11, 10, 7, 8, 8],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'race': 'elf',
        'primAttr': ['INT', 'DEX'],
        'saves': [8, 7, 7, 5, 5, 5],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR', 'DEX'],
        'saves': [8, 7, 6, 5, 4, 4],
        'attacksAs': 'best',
        'restrictions': ['Fighters can wear any armour or shield, and can use any weapon.'],
        'wps': 4,
        'special': [
            '(Class) Can use All Weapons and Armour without restriction',
        ],
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'race': 'halfling',
        'primAttr': ['DEX', 'CON'],
        'saves': [12, 11, 10, 7, 8, 8],
    },
    'lup': {
        'short': 'lup',
        'long': 'Lupine',
        'race': 'lupine',
        'primAttr': ['DEX', 'WIS'],
        'saves': [8, 7, 6, 5, 4, 4],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'primAttr': ['INT', 'STR'],
    },
    'mounte': {
        'short': 'mounte',
        'long': 'Mountebank',
        'primAttr': ['CHA', 'DEX'],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'primAttr': ['DEX', 'INT'],
    },
}

ham_profs = {
    'default': {
        'flags': ['base', 'human'],
        'race': 'human',
        'hd': 6,
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'attacksAs': 'mid',
        'skills': 'RANDOM',
        'extragear': [],
        'weapons': 'war',
        'armour': 'war',
        'saves': [0, 1, 1, 0, 0, 0],
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law'],
        'primAttr': ['WIS', 'CHA'],
        'saves': [0, 0, 0, 1, 0, 1],
        'weapons': 'clr',
        'casterStat': 'WIS',
        'spellsPerLvl': 2,
        'spellChooseAs': 'cleric',
        'extragear': ['a visible Symbol of your Holy Faith (S)', 'a Prayerbook (M)'],
        'restrictions': ['Can use all weapons, shields, and armour that are not otherwise prohibited by your deity.',
                         'You cannot be of Neutral Alignment'],
        'special': [
            '>>(Class) CAST CLERIC SPELLS! Add more by leveling up, and by converting discovered prayers. Maximum '
            'spell level is 1st Level.',
            '>>(Class) Once per Day you can use your holy symbol and turn back enemies of your faith. Opponents make '
            'Mind saves. Failures must cower, flee, or possibly even take damage or be destroyed.',
        ],
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarven Defender',
        'race': 'dwarf',
        'hd': 8,
        'primAttr': ['STR', 'CON'],
        'flags': ['base', 'demi'],
        'numAttacks': 2,
        'attacksAs': 'best',
        'extralangs': ['Dwarf'],
        'extragear': ['ARMOUR: a Small Shield (1H, Size M, DEF+2)'],
        'restrictions': ['Can use all weapons, shields, and armour except longbows.'],
        'special': [
            '>>(Class) Heavy/Plate armour affects neither your DEX nor your movement speed.',
            '>>(Class) You are never lost when underground with solid earth or stone beneath their feet. You know the '
            'local grades and depth, and can feel air flow naturally. You have a 50% chance of detecting '
            'hidden stonework just by passing, and automatically find them if you spend a Beat searching.',
            '>>(Class) You have a bonus MELEE Combat die at first level (total of two).',
            '>>(Class) You have a Boon on all Body and Death Saves.',
            '>>(Class) You can Shield Bash with any one of your successful Combat dice, without losing shield DEF.',
        ],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elven Exemplar',
        'race': 'elf',
        'flags': ['base', 'demi', 'caster'],
        'numAttacks': 2,
        'hd': 6,
        'primAttr': ['DEX', 'INT'],
        'saves': [0, 0, 1, 0, 1, 0],
        'casterStat': 'INT',
        'spellsPerLvl': 1,
        'spellChooseAs': 'mu',
        'extragear': ['a spellbook (M)'],
        'extralangs': ['Elf'],
        'extraspells': ['Level 1: Red Magic'],
        'restrictions': ['Can use all weapons, shields, and armour. Armour may limit spellcasting.'],
        'special': [
            '>>(Class) Immune to sleep, charm, slow, haste, aging, and energy drain effects, except from another Elf.',
            '>>(Class) Cast Magic-User spells. Gain new spells my leveling up, and from plundered scrolls and texts. '
            'Max spell level starts is 1.',
            '>>(Class) You can cast in armour. No chance of spell failure in Light armour, and only a 25%/50% '
            'chance in heavy/plate, respectively. Failed spells are forgotten.',
            '>>(Class) You are adept at dual-wielding melee. Add the second weapon\'s Melee bonus to your DEF.',
            '>>(Class) 50% chance of noticing concealed non-stonework features simply by passing near them, automatic '
            'if you spend a Beat searching.',
            '>>(Class) Bonus Combat die at first level (for a total of two).',
        ],
    },
    'explorer': {
        'short': 'explorer',
        'long': 'Explorer',
        'attacksAs': 'worst',
        'primAttr': ['DEX', 'INT'],
        'saves': [1, 0, 0, 1, 0, 0],
        'weapons': 'rog',
        'armour': 'rog',
        'extragear': ['a Set of Dungeoneering Tools (M)', 'WEAPON: Dagger (1H, Size S, R: 10/30ft, Dmg: M+1, Thrown)'],
        'extralangs': ['Underworld'],
        'restrictions': ['All missile weapons, all 1-handed weapons, light armour, bucklers, and small shields.'],
        'special': [
            '>>(Class) *Opportunist!* On melee attacks against a foe with net Boons or you are hidden, double total '
            'damage against that foe on a successful hit.',
            '>>(Class) Dungeon skills: Appraise/Identify (INT), Break/Enter (DEX), Climb/Leap (STR), '
            'Find & Seek (WIS), Forge/Decipher (INT), Hide/Sneak (DEX), Lie/Cheat (CHA), and Snatch/Grab (DEX). At '
            'first level you must randomly determine one Dungeon Skill to be your Bailiwick (which receives a Boon), '
            'and one to be your Failing (which receives a Bane). Once per adventure per XP level, you can attempt '
            'to reroll a failed Dungeon Skill check. This count resets upon Returning to Town.',
            '>>(Class) You receive a Boon on Tactical Attacks.',
            '>>(Class) You receive a Boon on Saves against Trap effects.',
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'attacksAs': 'best',
        'numAttacks': 2,
        'primAttr': ['STR', 'CON'],
        'saves': [0, 1, 1, 0, 0, 1],
        'restrictions': ['You can use all weapons, shields, and armour.'],
        'special': [
            '>>(Class) You have a bonus Combat die at first level (total of two).',
            '>>(Class) *Not Today!* (one use) When you would take damage that would kill you, you can say "NOT TODAY!" '
            'and negate all of the damage from that attack. Gain more uses as you gain levels',
            '>>(Class) When leveling up, you reroll your Hit Points twice, and keep the best result.',
            '>>(Class) You can Shield Bash with any one of your successful Combat dice, losing the shield DEF bonus.',
            '>>(Class) When using a two-handed weapon, roll an extra damage die with your attacks, applying the '
            'total result to all attacks that hit.',
        ],
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling Burglar',
        'race': 'halfling',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX', 'CHA'],
        'saves': [1, 1, 1, 1, 1, 1],
        'weapons': 'hlf',
        'armour': 'hlf',
        'extragear': ['a set of Dungeoneering tools (M)'],
        'extralangs': ['Halfling'],
        'restrictions': ['Can use all small weapons one-handed, or medium two-handed, and shields. Cannot use '
                         'two-handed human-sized weapons. All items are one size greater for Encumbrance limits.'],
        'special': [
            '>>(Class) Dungeon Skills: Break/Enter (DEX), Climb/Leap (STR with a Bane), Find/Seek (WIS), '
            'Hide/Sneak (DEX with a Boon), and Snatch/Grab (DEX).',
            '>>(Class) Unless you have proven to be an obvious threat, or your opponents specifically hate you, '
            'you are always attacked last.',
            '>>(Class) By spending 1 Hit Point rolling your attacks, increase your damage die for your attacks this '
            'round by one step.',
            '>>(Class) You receive a Boon on Tactical Attacks.',
        ],
    },
    'halfogre': {
        'short': 'halfogre',
        'long': 'Half-Ogre Berzerker',
        'race': 'halfogre',
        'flags': ['base', 'demi'],
        'attacksAs': 'best',
        'numAttacks': 2,
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'hd': 10,
        'primAttr': ['STR', 'CON'],
        'armour': 'brb',
        'extralangs': ['Ogre'],
        'restrictions': ['Can use all weapons and shields. Armour must be custom made. You cannot be Law aligned.'],
        'special': [
            '>>(Class) You are MASSIVE. All armour must be custom made, and only small creatures can move through '
            'your occupied space.',
            '>>(Class) You can stow Huge size items for 3 Encumbrance slots.',
            '(Class) When you take damage, make a Mind save (target: 12) or go into an uncontrollable violent fury. '
            'During this rage, gain an extra Combat die, gain temporary extra HP = 1/2 your level (up), and suffer 2 '
            'Banes on all saves except Body and Death. Your actions must follow a '
            'specific course (ask the \'Smith). You can also trigger it on your own by causing yourself 1 point of '
            'damage with a weapon.',
            '>>(Class) When using a two-handed weapon, roll d12 damage dice with your attacks (instead of d10), '
            'applying the result to all attacks that hit.',
        ],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster', 'mu-weapons'],
        'attacksAs': 'none',
        'hd': 4,
        'primAttr': ['INT'],
        'saves': [0, 0, 0, 0, 1, 0],
        'weapons': 'mag',
        'armour': 'mag',
        'casterStat': 'INT',
        'spellsPerLvl': 2,
        'spellChooseAs': 'mu',
        'extragear': ['a Spellbook (M)'],
        'extraspells': ['At Will: Read Magic'],
        'restrictions': ['Can not use two-handed weapons except staves. Can not wear heavy armour or use shields. '
                         'Other armour can cause spell failure (50%/75% in Light/Medium, respectively. Failed spells '
                         'are forgotten).'],
        'special': [
            '>>(Class) Cast magic-user spells. Add new spells from leveling up, and from plundered scrolls and texts. '
            'Max "safe" spell level starts at 1. You alone can also prepare and "High Cast" higher level spells, if '
            'you have a copy of the spell, by permanent loss of INT equal to the difference in allowed levels. '
            'Spells cast this way are always immediately forgotten.',
            '>>(Class) You can choose to take damage instead of forgetting spells. The amount is equal to the level of '
            'spell just cast. If below Zero HP, this burns CON instead.',
            '>>(Class) You can cast *Read Magic* freely and at will, no prep required.',
            '>>(Class) You can use special mage-only weapons: The Wand and The Staff.',
        ],
    },
}

m81_profs = {
    'default': {
        'hd': 6,
        'alignAllowed': ['chaos', 'law', 'neutral'],
        'wps': 0,
        'saves': [14],
        'skills': 'RANDOM',
    },
    'cleric': {
        'short': 'cleric',
        'long': 'Cleric',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '1500',
        'primAttr': ['CHA'],
        'restrictions': ['Clerics may wear any armour or shield, and any weapons except edged.'],
        'weapons': 'clr',
        'spellChooseAs': 'cleric',
        'spellsPerLvl': 1,
        'casterStat': 'MND',
        'saves': [15],
        'extragear': ['a Holy Symbol'],
        'special': [
            '(Class) Spellcaster (Cleric List)',
            '(Class) Turn Undead (DC: 10 + 2x HD of Undead. # of Daily Uses: 2 + Lvl + MIND Bonus)',
        ],
    },
    'dwarf': {
        'short': 'dwarf',
        'long': 'Dwarf',
        'race': 'dwarf',
        'primAttr': ['STR'],
        'restrictions': ['Dwarves can wear any weapon, armour, or shield. They cannot use weapons over 4 feet'
                         ' in length except axes and hammers.'],
        'flags': ['base', 'demi'],
        'nextXP': '2200',
        'hd': 8,
        'attacksAs': 'best',
        'wps': 1,
        'extralangs': ['Dwarf', 'Kobold', 'Goblin', 'Gnome'],
        'special': [
            '(Class) Fighter Bonus +1 to Attacks and Damage.',
            '(Class) Choose 1 Weapon for "Good" Mastery: +2 to hit, Change damage to 1d2+2 (for 1d4), 1d3+3 (for 1d6),'
            ' 1d4+4 (for 1d8), etc.',
            '(Class) +4 Save vs Magic',
            '(Class) Can see in darkness half as well as in light.',
            '(Class) Stonelore (d20 + MIND bonus; DC 12 if carefully checking, DC 16 if in passing)',
        ],
    },
    'elf': {
        'short': 'elf',
        'long': 'Elf',
        'race': 'elf',
        'flags': ['base', 'demi', 'caster'],
        'nextXP': '4000',
        'attacksAs': 'best',
        'wps': 1,
        'primAttr': ['MND'],
        'restrictions': ['Elves can wear any armour or shield, and can use any weapon.'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'MND',
        'saves': [17],
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'extralangs': ['Elf', 'Orc', 'Hobgoblin', 'Gnoll'],
        'special': [
            '(Class) Spellcaster (Mage list)',
            '(Class) +2 Attack and Damage bonus vs Goblinoids',
            '(Class) Fighter Bonus +1 to Attacks and Damage.',
            '(Class) Choose 1 Weapon for "Good" Mastery: +2 to hit, Change damage to 1d2+2 (for 1d4), 1d3+3 (for 1d6),'
        ],
    },
    'fighter': {
        'short': 'fighter',
        'long': 'Fighter',
        'hd': 8,
        'primAttr': ['STR'],
        'attacksAs': 'best',
        'restrictions': ['Fighters can wear any armour or shield, and can use any weapon.'],
        'wps': 1,
        'special': [
            '(Class) Can use All Weapons and Armour without restriction',
            '(Class) Fighter Bonus +1 to Attacks and Damage.',
            '(Class) Choose 1 Weapon for "Good" Mastery: +2 to hit, Change damage to 1d2+2 (for 1d4), 1d3+3 (for 1d6),'
        ],
    },
    'halfling': {
        'short': 'halfling',
        'long': 'Halfling',
        'race': 'halfling',
        'flags': ['base', 'demi'],
        'primAttr': ['DEX'],
        'attacksAs': 'best',
        'restrictions': ['You can wear light or medium armor, use shields, and use any light or medium weapon. '
                         'Due to your stature, you must wield medium weapons with two hands and '
                         'cannot use a long bow.'],
        'weapons': 'hlf',
        'armour': 'hlf',
        'saves': [15],
        'special': [
            '(Class) Fighter Bonus +1 to Attacks and Damage.',
            '(Class) Choose 1 Weapon for "Good" Mastery: +2 to hit, Change damage to 1d2+2 (for 1d4), 1d3+3 (for 1d6),'
            '(Class) +4 to magic saves.',
            '(Class) +2 to hit and damage with slings and light bows.',
            '(Class) You can blend in background (d20 + DEX Bonus; DC 12 if outdoors, DC 16 if indoors).',
            '(Class) You can move silently outdoors.',
        ],
    },
    'mu': {
        'short': 'mu',
        'long': 'Magic-User',
        'flags': ['base', 'human', 'caster'],
        'nextXP': '2500',
        'hd': 4,
        'primAttr': ['MND'],
        'saves': [16],
        'attacksAs': 'worst',
        'restrictions': ['Magic-users may not wear armour and may only use daggers, staves, and slings as weapons.'],
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'MND',
        'extragear': ['a Spellbook'],
        'extraspells': ['Read Magic'],
        'special': [
            '(Class) Spellcaster (Mage list)',
        ],
    },
    'thief': {
        'short': 'thief',
        'long': 'Thief',
        'flags': ['base', 'human'],
        'nextXP': '1250',
        'hd': 4,
        'primAttr': ['DEX'],
        'restrictions': [
            'Thieves can wear light armor, use shields, and use any light or medium weapon.',
        ],
        'weapons': 'rog',
        'armour': 'rog',
        'extragear': ['a Set of Thieves\' Tools'],
        'special': [
            '(Class) Backstab: If a thief successfully sneaks up on a foe, they can Backstab which adds +4 to the'
            ' attack roll and does x2 damage.',
            '(Class) Thieves are specialists at urban survival as well as at picking pockets, hiding in cover,'
            ' sneaking silently, opening locks, removing traps, climbing walls, and other tasks associated'
            ' with theft.',
            '(Class) Thieves may attempt to climb sheer surfaces and hide in shadows with a successful secondary'
            ' skill roll.',
            '(Class) Thieves have special training in listening at doors and detecting traps and secret/hidden doors.',
        ],
        'extralangs': ['Thieves\' Cant'],
        'saves': [14, 15, 13, 16, 14, 14],
    },
}

pla_profs = {
    'default': {},
    'fighter': {}
}

tnu_profs = {
    'default': {
        'hd': 8,
        'attacksAs': 'none',
        'skills': ['See Background for Inspiration'],
    },
    'assassin': {
        'short': 'assassin',
        'long': 'Assassin',
        'primAttr': ['DEX', 'FER'],
        'alignAllowed': ['chaos', 'evil', 'law', 'neutral'],
        'attacksAs': 'best',
        'restrictions': [
            'You can\'t be of good alignment',
            'You can\'t hide or be stealthy in a suit of plate or when you are encumbered.',
            'You get no attack bonus while wearing a suit of plate.',
        ],
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
        'restrictions': [
            'You can\'t be of evil alignment.',
            'You can\'t cast spells when you use a shield or wear a suit of plate.',
        ],
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
        'restrictions': [
            'You can\'t be of neutral alignment.',
            'You must display your alignment prominently, or else you cannot use any of your special abilities.',
        ],
        'spellChooseAs': 'champ_chaos',
        'spellsPerLvl': 2,
        'casterStat': 'INT',
        'extragear': [str(die(1, 6)) + ' doses of hallucinogenic cactus'],
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
        'restrictions': [
            'You can\'t be of neutral alignment.',
            'You must display your alignment prominently, or else you cannot use any of your special abilities.',
        ],
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
        'restrictions': [
            'You can\'t be of neutral alignment.',
            'You must display your alignment prominently, or else you cannot use any of your special abilities.',
        ],
        'extragear': [str(die(1, 6)) + ' doses of antitoxin', str(die(1, 6)) + ' uses of bandages'],
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
        'restrictions': [
            'You can\'t be of neutral alignment.',
            'You must display your alignment prominently, or else you cannot use any of your special abilities.',
        ],
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
        'restrictions': [
            'You can\'t be of lawful alignment.',
            'You may fight with your bare hands, throw things at people, use shields, and wear light armour, '
            'plus choose two: blades, blunt weapons, firearms, garrotes, heavy armour, or missile weapons. The ones '
            'you do not choose are restricted by your cult precepts or you are not skilled at using them. While '
            'using restricted weapons or armour, you get no attack bonus, you may not banish your spiritual enemies, '
            'and you may not cast spells.',
            'You must surrender half your income to your cult, in order to gain experience points from recovering '
            'it. You may send this money as a tithe to your superiors, or spend it on establishing a shrine or '
            'temple of your own.',
        ],
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
        'restrictions': [
            'As a member of the most insolent of professions, the fighter has no restrictions. Anyone can fight - '
            'even cowards, when the brave have all been slaughtered.',
        ],
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
        'restrictions': [
            'You can\'t be of chaotic alignment.',
            'You get no damage bonus for wielding a non-magical two-handed weapon.',
            'You may not fight while wearing a non-magical suit of plate.',
            'You must roll to search like any other character while encumbered or '
            'wearing a non-magical suit of plate.',
        ],
        'spellChooseAs': 'scholar',
        'spellsPerLvl': 1,
        'casterStat': 'INT',
        'special': [
            'You are a Spellcaster.',
            'During a short or long rest, you may heal another person, restoring 1d4 points to one of their '
            'attributes that has been temporarily reduced. You may not treat the same person again until they '
            'are harmed again, but you may treat a total number of people each day equal to your level (if you '
            'spend an hour on each).',
            'You always find hidden things when you spend a Beat searching a dungeon of your level or lower, '
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
        'restrictions': [
            'You can\'t hide or be stealthy in a suit of plate or when you are encumbered.',
            'You must roll to search like any other character when you wear a suit of plate.',
        ],
        'special': [
            'When you search an area in haste, if the dungeon level is equal to your level or lower, '
            'you must roll equal to or lower than your Dexterity score on a d20 to find hidden things. '
            'If the dungeon level is higher than your own, you must roll equal to or lower than half your '
            'Dexterity score, rounded down, on a d20 to find hidden things.',
            'You always find hidden things when you spend a Beat searching a dungeon of your level or lower, '
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
        'restrictions': [
            'You can\'t fight while wearing a suit of plate.',
            'You do not receive a damage bonus for wielding a two-handed weapon.',
            'You must roll to cast spells like any other character when you are encumbered, wearing a '
            'suit of plate, or using a shield.',
        ],
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

base_profs_def = [
    'fighter'
]

base_profs_bnt = [
    'assassin', 'barbarian', 'bard', 'cleric', 'duelist',
    'fighter', 'mu', 'paladin', 'ranger', 'sorc', 'thief',
]

base_profs_ddh = [
    'cleric', 'clock', 'druid', 'elf', 'drawf', 'fighter', 'halfogre', 'hobbert', 'lup', 'mu', 'mounte', 'thief'
]

base_profs_ddx = [
    'cleric', 'clock', 'druid', 'elf', 'dwarf', 'fighter', 'halfling', 'lup', 'mu', 'mounte', 'thief'
]

base_profs_dnd = [
    'cleric', 'elf', 'dwarf', 'fighter', 'halfling', 'mu', 'thief'
]

base_profs_ham = [
    'cleric', 'elf', 'dwarf', 'explorer', 'fighter', 'halfogre', 'halfling', 'mu',
]

base_profs_pla = [
    'fighter'
]

base_profs_tnu = [
    'assassin', 'bard',
    'champ_chaos', 'champ_evil', 'champ_good', 'champ_law',
    'cultist', 'fighter', 'scholar', 'thief', 'wizard'
]

# I don't do druids or monks, they're a pain in the ass
proflists = {
    'def': {
        'choices': base_profs_def,
        'dict': def_profs,
    },
    'bnt': {
        'choices': base_profs_bnt,
        'dict': bnt_profs,
    },
    'bntx': {
        'choices': base_profs_bnt,
        'dict': bnt_profs,
    },
    'dd': {
        'choices': base_profs_dnd,
        'dict': dd_profs,
    },
    'ddh': {
        'choices': base_profs_ddh,
        'dict': ddh_profs,
    },
    'ddx': {
        'choices': base_profs_ddx,
        'dict': ddx_profs,
    },
    'ham': {
        'choices': base_profs_ham,
        'dict': ham_profs,
    },
    'm81': {
        'choices': base_profs_dnd,
        'dict': m81_profs,
    },
    'pla': {
        'choices': base_profs_pla,
        'dict': pla_profs,
    },
    'rbh': {
        'choices': base_profs_pla,
        'dict': pla_profs,
    },
    'rpt': {
        'choices': base_profs_pla,
        'dict': pla_profs,
    },
    'tnu': {
        'choices': base_profs_tnu,
        'dict': tnu_profs,
    },
    'template': {
        'choices': [],
        'dict': '',
    },
}

supported_systems = [
    'bnt', 'bntx', 'dd', 'ddh', 'ddx', 'ham', 'm81', 'pla', 'rbh', 'rpt', 'tnu'
]


# this returns a random character profession and all its base data
def get_profession(system='def'):
    if system not in supported_systems:
        system = 'def'
    game_professions_choices = proflists[system]['choices']
    game_professions_dict = proflists[system]['dict']
    profession_data = baseline
    system_defaults = game_professions_dict['default']
    profession_data.update(system_defaults)
    my_random_profession = game_professions_dict[random.choice(game_professions_choices)]
    profession_data.update(my_random_profession)
    return profession_data


#
# this returns a random HAMMERCRAWL! character profession and all its base data
# NOTE: I've skewed this greater since I'm using 1d20 instead of 3d6 here, to offset the lack of true randomness.
#
def get_hammerclass(classroll, subroll):
    if classroll >= 18:
        hammercrawl_profession = 'halfogre'
    elif classroll >= 14:
        hammercrawl_profession = 'halfling'
    elif classroll >= 8:
        humans = ['cleric', 'explorer', 'fighter', 'mu', ]
        hammercrawl_profession = humans[subroll - 1]
    elif classroll >= 4:
        hammercrawl_profession = 'dwarf'
    else:
        hammercrawl_profession = 'elf'
    game_professions_dict = proflists['ham']['dict']
    profession_data = baseline
    system_defaults = game_professions_dict['default']
    profession_data.update(system_defaults)
    my_random_profession = game_professions_dict[hammercrawl_profession]
    profession_data.update(my_random_profession)
    return profession_data


if __name__ == "__main__":
    for key, value in dict.items((get_profession('dd'))):
        print(key, ":", value)
