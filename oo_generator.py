"""
converting the generator.py code to a class
"""

import random
import argparse

import dice
import equipment_osr
import equipment_tnu
import professions
import spells_osr
import spells_tnu
import systems

parser = argparse.ArgumentParser(description='Get Game System')
parser.add_argument('-g', '--game_system', type=str, required=True, choices=['bnt', 'dd', 'tnu'],
                    help='The abbreviated Game System (bnt, dd, tnu)')
parser.add_argument('-H', '--hammercrawl', action='store_true',
                    help='Enable HAMMERCRAWL! extended features (currently disabled)')
args = parser.parse_args()

supported_systems = [
    'tnu', 'dd', 'bnt'
]
