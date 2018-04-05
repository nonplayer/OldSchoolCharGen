"""
This file generates weaponry for the custom Wizard Weapons house rules.
The original idea for this was inspired by a gaming blog post which no longer exists.
The base list of options was provided by Grey Knight on Google Plus, used with their permission (CC0)
"""

import random

components = [
    'animal bone', 'birch wood',
    'brass', 'bronze',
    'copper', 'delicious candy',
    'granite', 'green glass',
    'hazel wood', 'human bone',
    'iron', 'ivory',
    'mahogany', 'maple wood',
    'marble', 'oak wood',
    'pine wood', 'petrified wood',
    'reforged blades',
    'rowan wood', 'rusted iron',
    'sandstone', 'steel',
    'terracotta', 'tin',
    'twisted and bound tentacles',
    'welded chains',
    'wicker', 'wrought iron',
]

decorations = [
    'boxes', 'bulbous lumps',
    'bumps', 'chains',
    'curlicues', 'demonic faces',
    'dots', 'edging',
    'flowers', 'hexagons',
    'rings', 'runes',
    'thin wires', 'scales',
    'smooth panels', 'spikes',
    'spirals', 'stars',
    'streaks', 'upright forks',
    'vanes', 'webs',
]

materials = [
    'aluminium', 'amber',
    'animal horn', 'coral',
    'gold', 'jade',
    'jasper', 'lead',
    'mirrored glass', 'mother-of-pearl',
    'obsidian', 'onyx',
    'platinum', 'porcelain',
    'quartz', 'shell',
    'silver', 'tortoise shell',
    'titanium', 'zinc',
]

tip_features = [
    'an agate', 'an amber',
    'an amethyst', 'a brass',
    'a clear glass', 'a diamond-studded',
    'an emerald-studded', 'a garnet-studded',
    'a golden', 'an ivory',
    'a jade', 'a mirrored',
    'a mother-of-pearl', 'a pearly',
    'a peridot', 'a porcelain',
    'a rusty', 'a sapphire-studded',
    'a silver', 'a turquoise',
]

tip_types = [
    'acorn', 'conch',
    'cube', 'dish',
    'egg-shape', 'eyeball',
    'fan', 'feather', 'fist',
    'fork', 'geometric cage',
    'grape-like cluster', 'hand',
    'orb', 'point',
    'prism', 'pyramid',
    'skull', 'snake',
    'spiral', 'star',
]

effects = [
    'a burning smell', 'a distant buzzing noise',
    'a faint glow', 'a goosing in your skin', 'a shimmering haze',
    'a slight vibration', 'a soft murmur',
    'a tickle in your palm',
    'an occasional popping noise', 'an occasional twitch',
    'an oily sheen', 'an unnatural feeling of arousal',
    'intermittent puffs of smoke',
    'intermittent sparkles', 'it balances easily on its end',
    'it is cold to the touch', 'it is damp to the touch',
    'it is warm to the touch', 'it rotates slowly by itself',
    'it writhes in your grip', 'the scent of incense',
    'the scent of minty herbs', 'the scent of old books',
    'the scent of old leather', 'the smell of sulphur',
    'the distant stink of rotting flesh',
]

energy_bases = [
    'attacks with',
    'defends by generating',
]

energy_forms = [
    'a field', 'a wavefront',
    'an intense point', 'arcs',
    'blasts', 'bolts',
    'bursts', 'clouds',
    'curling tendrils', 'discs',
    'forking lines', 'geometric lines',
    'orbs', 'pulses',
    'runic shapes', 'shooting stars',
    'skull shapes', 'waves',
    'webs', 'wisps',
]

energy_types = [
    'actinic sparks', 'arcane energy',
    'burning plasma', 'choking sand',
    'concussive force', 'crackling energy',
    'dripping blood', 'eldritch goo',
    'explosive flame', 'fearful darkness',
    'flensing particles', 'foul venom',
    'freezing cold', 'frothing water',
    'iridescent air', 'potent acid',
    'rainbow light', 'spatial distortion',
    'throbbing sound', 'vibrant lifeforce',
]


def generate():
    options = ['Wand', 'Staff']
    nature = random.choice(options)
    component = random.choice(components)
    decoration = random.choice(decorations)
    material = random.choice(materials)
    tip_feature = random.choice(tip_features)
    tip_type = random.choice(tip_types)
    effect = random.choice(effects)
    if nature == 'Staff':
        energy_base = 'defends by generating'
        mechanical = 'It functions as a +2 AC Shield when gripped with both hands for the entire round. If hit ' \
                     'with a Nat 20, it runs out of power and must be recharged by burning a spell of any level.'
    else:
        energy_base = 'attacks with'
        mechanical = 'It functions as a sling (Atk Bonus: INT mod, R: 40/80/160ft, Dmg: 1d4) with near-infinite ' \
                     'ammo. On a Natural 1 it runs out of power and must be recharged by burning a spell of any level.'
    energy_form = random.choice(energy_forms)
    energy_type = random.choice(energy_types)
    my_weapon = "A Wizard's %s made of %s, decorated with %s of %s, and tipped with %s %s. When held, you notice" \
                " %s. It %s %s of %s. %s" % (nature, component, decoration, material, tip_feature, tip_type, effect,
                                             energy_base, energy_form, energy_type, mechanical)
    return my_weapon


if __name__ == "__main__":
    print(generate())
