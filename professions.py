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
    'wps': False,                           # INT: How many starting Weapon Proficiencies
    'weapons': 'war',                       # STR: Category of weapons allowed as choices
    'armour': 'war',                        # STR: Category of armours allowed as choices
    'spellChooseAs': '',                    # STRING: if caster, usually = short
    'spellsPerLvl': 0,                      # INT: if caster, how many spell choices per level
    'cantrips': False,                      # either False or INT: num of cantrips at first level
    'casterStat': '',                       # STRING: stat used for spells, if a caster
    'extraspells': False,                   # either False or some magicians get free spells plus their choices
    'saves': False,                         # FALSE or else a LIST of integers, in order
    'extragear': False,                     # either False or LIST: some professions have extra gear, put it here
    'extralangs': [],                       # LIST if any bonus languages come with the class
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
        'saves': [12, 13, 14, 15, 16],
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
        'saves': [11, 12, 14, 16, 15],
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
        'saves': [8, 9, 10, 13, 12],
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
        'saves': [12, 13, 13, 15, 15],
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
        'saves': [8, 9, 10, 13, 12],
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
        'saves': [13, 14, 13, 16, 15],
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
        'saves': [13, 14, 13, 16, 15],
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

ham_profs = {
    'default': {
        'flags': ['base', 'human'],
        'race': 'human',
        'hd': 6,
        'alignAllowed': ['chaos', 'evil', 'good', 'law', 'neutral'],
        'attacksAs': 'mid',
        'skills': 'RANDOM',
        'weapons': 'war',
        'armour': 'war',
        'saves': [0, 1, 1, 0, 0, 0],
    },
    'cleric': {
        'short': 'cleric',  # STR: class name for references
        'long': 'Cleric',  # STR: class name for display
        'flags': ['base', 'human', 'caster'],
        'alignAllowed': ['chaos', 'evil', 'good', 'law'],
        'primAttr': ['WIS', 'CHA'],
        'saves': [0, 0, 0, 1, 0, 1],
        'weapons': 'clr',
        'casterStat': 'WIS',  # STRING: stat used for spells, if a caster
        'spellsPerLvl': 2,
        'spellChooseAs': 'cleric',  # STRING: if caster, usually = short
        'extragear': ['A visible Symbol of your Holy Faith'],
        'restrictions': ['Can use all weapons, shields, and armour that are not otherwise prohibited by your deity.',
                         'You cannot be of Neutral Alignment'],
        'special': [
            '(Class) You cast spells from the Cleric spell list. You begin the game with a holy prayerbook which '
            'contains a chance for randomly-determined clerical prayers. At each new level you add two (2) new '
            'prayers to your book, and you can add more by sanctifying, converting, and transcribing prayers to '
            'other gods found on scrolls and books in dungeons. At level 1 you can only cast level 1 spells. This '
            'maximum spell level increases by +1 at every odd-numbered level of experience.',
            '(Class) Once per Day per Level of Experience, you can hold aloft your holy symbol and turn back '
            'undead, devils, demons, and any others that the \'Smith deems to be enemies of your faith. Opponents '
            'must make Mind saves based on the difference in Level/HD Tiers. Targets who fail this save must cower, '
            'flee, or possibly even take damage or be destroyed.',
        ],
    },
    'dwarf': {
        'short': 'dwarf',  # STR: class name for references
        'long': 'Dwarven Defender',
        'race': 'dwarf',
        'hd': 8,
        'primAttr': ['STR', 'CON'],
        'flags': ['base', 'demi'],  # LIST of flags for different effects
        'attacksAs': 'best',
        'extralangs': ['Dwarf'],
        'restrictions': ['Can use all weapons, shields, and armour except longbows.'],
        'special': [
            '(Class) If wearing Medium or heavier armour you do not suffer AC penalties from low DEX. Heavy armour '
            'never reduces your movement speed.',
            '(Class) You are never lost when underground with solid earth or stone beneath their feet. You know the '
            'local grades and depth, and can feel air flow naturally. You have a 50% chance of detecting '
            'hidden stonework just by passing, and automatically find them if you spend a turn searching.',
            '(Class) You have a bonus melee attack die at first level (total of two), and gain a new one at '
            'levels 5, 10, and 15. When attacking, declare target(s) and then roll all of your attack dice, but only '
            'one damage die. Each hit applies the same amount of damage.',
            '(Class) You have advantage on all Body and Death Saves.',
            '(Class) You can use a Shield Bash with any one of your successful attack dice. As a Dwarf You do not '
            'lose the AC bonus of the shield when using the bash.',
        ],
    },
    'elf': {
        'short': 'elf',  # STR: class name for references
        'long': 'Elven Exemplar',
        'race': 'elf',
        'flags': ['base', 'demi', 'caster'],  # LIST of flags for different effects
        'hd': 8,
        'primAttr': ['DEX', 'INT'],
        'saves': [0, 0, 1, 0, 1, 0],
        'casterStat': 'INT',  # STRING: stat used for spells, if a caster
        'spellsPerLvl': 1,
        'spellChooseAs': 'mu',  # STRING: if caster, usually = short
        'extralangs': ['Elf'],
        'extraspells': ['Level 1: Read Magic'],
        'restrictions': ['Can use all weapons, shields, and armour. Armour may limit spellcasting.'],
        'special': [
            '(Class) Immune to sleep, charm, slow, haste, aging, and energy drain effects, except from another Elf.',
            '(Class) Cast spells from the magic-user list. Starting spellbook contains Read Magic and randomly-'
            'determined bonus spells. At each new level gain 1 new spell from ongoing experimentation. You can add '
            'more from scrolls and texts found in dungeons. At level 1 you can only cast level 1 spells. Max spell '
            'level increases +1 at every odd-numbered level.',
            '(Class) You can cast in armour. You suffer no chance of spell failure in Light, and a 25%/50%/75% '
            'chance in medium/heavy/plate, respectively. Failed spells are forgotten.',
            '(Class) You can fight with two weapons. Roll one extra attack die, but lower the damage die by one step '
            '(to a d6) for the action. At level 9, this increases to two extra attack dice.',
            '(Class) At second level, you gain a second attack die when using normal Bows, and a third at level 10. '
            'Each die requires ammo. Declare target(s) and then roll all of the attack dice, but only one damage die.',
            '(Class) 50% chance of noticing concealed non-stonework features simply by passing near them, and '
            'automatically if you spend a turn searching.',
            '(Class) Bonus melee attack die at first level, and gain a new one at levels 5, 10, and 15. When '
            'attacking, declare target(s) and roll all of your dice, but only one damage die.',
        ],
    },
    'fighter': {
        'short': 'fighter',  # STR: class name for references
        'long': 'Fighter',  # STR: class name for display
        'hd': 8,
        'attacksAs': 'best',
        'primAttr': ['STR', 'CON'],
        'saves': [0, 1, 1, 0, 0, 1],
        'restrictions': ['You can use all weapons, shields, and armour.'],
        'special': [
            '(Class) You have a bonus melee attack die at first level (total of two), and gain a new one at levels '
            '3, 6, 9, 12, and 15. When attacking, declare target(s) and then roll all of the attack dice, but only '
            'one damage die. Each hit applies the same amount of damage.',
            '(Class) *Not Today!* At first level and each level after, you gain a single use of "Not Today!" When '
            'you would take damage (from any source) that would reduce your HP from positive to Zero or below, you '
            'can spend a use and instead remain at 1 HP and negate the rest of the damage from that attack. These '
            'uses accumulate with each level, but each use is permanently lost upon spending.',
            '(Class) You have advantage on all Hit Dice rolls, and reroll all 1s on Hit Dice.',
            '(Class) You can use a Shield Bash with any one of your successful attack dice, losing the shield AC '
            'bonus until your next turn in combat.',
            '(Class) When using a two-handed weapon, roll an extra damage die with your attacks, applying the '
            'total result to all attacks that hit.',
        ],
    },
    'halfling': {
        'short': 'halfling',  # STR: class name for references
        'long': 'Halfling Burglar',
        'race': 'halfling',
        'flags': ['base', 'demi'],  # LIST of flags for different effects
        'primAttr': ['DEX', 'CHA'],
        'saves': [1, 1, 1, 1, 1, 1],
        'weapons': 'hlf',
        'armour': 'hlf',
        'extralangs': ['Halfling'],
        'restrictions': ['Can use all small weapons one-handed, or medium two-handed, and shields. Cannot use '
                         'two-handed human-sized weapons.'],
        'special': [
            '(Class) You gain a bonus melee attack die at levels 4, 8, and 12. When attacking, declare your target(s) '
            'and then roll all your attack dice, but only one damage die. Each hit applies the same amount of damage.',
            '(Class) You have the following Thief Skills: Lockpicking, Perception, Stealth (with Advantage), '
            'Thief-Climbing, and Trap-Finding (with Disadvantage).',
            '(Class) Unless you have proven to be an obvious threat, or your opponents are otherwise specifically '
            'predisposed against you, you are always attacked last.',
            '(Class) You can draw from inner strength for a sudden display of unexpected fierceness. By spending 1 '
            'Hit Point rolling your attacks, you increase the damage die for your attacks this round by one step.',
            '(Class) You roll with advantage on Tactical Attacks.',
        ],
    },
    'halfogre': {
        'short': 'halfogre',  # STR: class name for references
        'long': 'Half-Ogre Berzerker',  # STR: class name for display
        'race': 'halfogre',  # STR: race name of "RANDOM" to trigger the random race function
        'flags': ['base', 'demi'],  # LIST of flags for different effects
        'attacksAs': 'best',
        'alignAllowed': ['chaos', 'evil', 'good', 'neutral'],
        'hd': 10,
        'primAttr': ['STR', 'CON'],
        'armour': 'brb',
        'extralangs': ['Ogre'],
        'restrictions': ['Can use all weapons and shields. Armour must be custom made. You cannot be Law aligned.'],
        'special': [
            '(Class) You are built like an icehouse. All armour must be custom made at increased costs and time, '
            'and only Halfling-sized creatures or smaller can move through your occupied space.',
            '(Class) When you take damage, make a Mind save (target: 12) or go into an uncontrollable violent fury. '
            'During this rage, take advantage on melee and thrown damage dice rolls, immunity to critical fumbles, '
            'and disadvantage on all saves except Body and Death. Your actions must follow a specific course (ask '
            'the \'Smith). You can voluntarily fail either save and willingly let the rage happen and/or knock '
            'you unconscious afterward. You can also trigger it on your own by causing yourself 1 point of damage '
            'with a weapon.',
            '(Class) You get a bonus attack die at first level (total of two), and gain a new one at levels 5, 10, '
            'and 15. When attacking, declare target(s) and then roll all your attack dice, but only one damage '
            'die. Each hit applies the same amount of damage.',
            '(Class) When using a two-handed weapon, roll d12 damage dice with your attacks (instead of d10), '
            'applying the result to all attacks that hit.',
        ],
    },
    'mu': {
        'short': 'mu',  # STR: class name for references
        'long': 'Magic-User',  # STR: class name for display
        'flags': ['base', 'human', 'caster', 'mu-weapons'],
        'attacksAs': 'none',
        'hd': 4,
        'primAttr': ['INT'],
        'saves': [0, 0, 0, 0, 1, 0],
        'weapons': 'mag',
        'armour': 'mag',
        'casterStat': 'INT',  # STRING: stat used for spells, if a caster
        'spellsPerLvl': 2,
        'spellChooseAs': 'mu',  # STRING: if caster, usually = short
        'extragear': ['a Spellbook'],
        'extraspells': ['At Will: Read Magic'],
        'restrictions': ['Can not use two-handed weapons except staves. Can not wear heavy armour or use shields. '
                         'Other armour can cause spell failure.'],
        'special': [
            '(Class) Cannot wear Heavy armour, and suffer a chance of spell failure while wearing other. '
            'Chance is 50%/75% in Light/Medium, respectively. Failed spells are forgotten.',
            '(Class) Cast magic-user spells. Start with a spellbook containing Read Magic and other randomly bonus '
            'spells. At each level you add 2 new spells from experimentation, and you can add more from scrolls '
            'magical texts found in dungeons. At level 1 you can safely cast level 1 spells. Max spell level '
            'increases by +1 at every odd-numbered level of experience. ',
            '(Class) You can prepare and try to cast spells of higher level than your normal Max, if you have a copy '
            'of the spell in your book. Casting requires permanent loss of INT equal to the difference in allowed '
            'levels. Spells cast this way are always immediately forgotten.',
            '(Class) You can choose to take damage instead of forgetting spells. The amount is equal to the level of '
            'spell just cast. If below Zero HP, this burns CON instead.',
            '(Class) You can cast *Read Magic* freely and at will, no prep required.',
            '(Class) You can use special mage-only weapons: The Wand and The Staff.',
        ],
    },
    'thief': {
        'short': 'thief',  # STR: class name for references
        'long': 'Thief',  # STR: class name for display
        'attacksAs': 'worst',
        'primAttr': ['DEX', 'INT'],
        'saves': [1, 0, 0, 1, 0, 0],
        'weapons': 'rog',
        'armour': 'rog',
        'extragear': ['a Set of Thieves\' Tools'],
        'extralangs': ['Thieves\' Cant'],
        'restrictions': ['You can use any weapons and armour that the Hammersmith deems to be suitably sneaky.'],
        'special': [
            '(Class) *Stabbity!* When using a melee weapon to attack a foe against which you either have attack '
            'advantage or are hidden from perception, double your total damage against that foe on a successful hit. '
            'This multiple increases by +1 at levels 3, 6, 9, 12, and 15.',
            '(Class) You have access to special Thief-Only skills: Deciphering (INT), Lockpicking (DEX), Perception '
            '(WIS), Stealth (DEX), Thief-climbing (STR), Tracking (WIS), Trap-finding (INT), and Trap-breaking (DEX). '
            'At first level you must randomly determine one Thief Skill to be your Bailiwick, and one to be your '
            'Failing. You get advantage on checks related to your Bailiwick, and disadvantage on checks related to '
            'your Failing,  Once per adventure per experience level, you can attempt to reroll a failed Thief Skill '
            'check. This count resets upon Returning to Town.',
            '(Class) You roll with advantage on Tactical Attacks.',
            '(Class) You have advantage on all Saves against the effects of Traps.',
        ],
    },
}

m81_profs = {
    'default': {
        'hd': 6,
        'alignAllowed': ['chaos', 'law', 'neutral'],
        'wps': 0,
        'saves': [12, 13, 14, 15, 16],
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
        'casterStat': 'MIND',
        'saves': [11, 12, 14, 16, 15],
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
        'saves': [8, 9, 10, 13, 12],
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
        'primAttr': ['MIND'],
        'restrictions': ['Elves can wear any armour or shield, and can use any weapon.'],
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'MIND',
        'saves': [12, 13, 13, 15, 15],
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
        'saves': [8, 9, 10, 13, 12],
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
        'primAttr': ['MIND'],
        'saves': [13, 13, 13, 16, 14],
        'attacksAs': 'worst',
        'restrictions': ['Magic-users may not wear armour and may only use daggers, staves, and slings as weapons.'],
        'weapons': 'mag',
        'armour': 'mag',
        'spellChooseAs': 'mu',
        'spellsPerLvl': 2,
        'casterStat': 'MIND',
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
        'saves': [14, 15, 13, 16, 14],
    },
}

pla_profs = {}

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
        'restrictions': [
            'You can\'t hide or be stealthy in a suit of plate or when you are encumbered.',
            'You must roll to search like any other character when you wear a suit of plate.',
        ],
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

base_profs_tnu = [
    'assassin', 'bard',
    'champ_chaos', 'champ_evil', 'champ_good', 'champ_law',
    'cultist', 'fighter', 'scholar', 'thief', 'wizard'
]

base_profs_bnt = [
    'assassin', 'barbarian', 'bard', 'cleric', 'duelist',
    'fighter', 'mu', 'paladin', 'ranger', 'sorc', 'thief',
]

base_profs_dnd = [
    'cleric', 'elf', 'dwarf', 'fighter', 'halfling', 'mu', 'thief'
]

base_profs_ham = [
    'cleric', 'elf', 'dwarf', 'fighter', 'halfogre', 'halfling', 'mu', 'thief'
]

# I don't do druids or monks, they're a pain in the ass
proflists = {
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
    'ham': {
        'choices': base_profs_ham,
        'dict': ham_profs,
    },
    'm81': {
        'choices': base_profs_dnd,
        'dict': m81_profs,
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


# this returns a random character profession and all its base data
def get_profession(system='tnu'):
    game_professions_choices = proflists[system]['choices']
    game_professions_dict = proflists[system]['dict']
    profession_data = baseline
    system_defaults = game_professions_dict['default']
    profession_data.update(system_defaults)
    my_random_profession = game_professions_dict[random.choice(game_professions_choices)]
    profession_data.update(my_random_profession)
    return profession_data


# this returns a random character profession and all its base data
def get_hammerclass(classroll, subroll):
    if classroll >= 17:
        hammercrawl_profession = 'halfogre'
    elif classroll >= 14:
        hammercrawl_profession = 'halfling'
    elif classroll >= 8:
        humans = ['cleric', 'fighter', 'mu', 'thief']
        hammercrawl_profession = humans[subroll - 1]
    elif classroll >= 5:
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
