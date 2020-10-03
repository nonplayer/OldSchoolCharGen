# About this Project

This is a Python-based tool to generate random first-level characters for "classic old school" D&D-like tabletop role-playing games.

## Systems Compatibility

Currently this tool can create characters for the following old school games:

* [The Nightmares Underneath 1st Edition, by Johnstone Metzger](http://www.drivethrurpg.com/product/195355/The-Nightmares-Underneath).
* [Dark Dungeons](http://www.drivethrurpg.com/product/177410/Dark-Dungeons)
* [Blood & Treasure 1st Edition](http://www.drivethrurpg.com/product/124972/Blood--Treasure-Complete)
  - This includes the optional "Advanced" rules via the `bntx` command line argument.
* [Microlite81](http://www.drivethrurpg.com/product/174568/Microlite81-Complete)
* [HAMMERCRAWL!](https://github.com/nonplayer/hammercrawl/) is my own creation, and is now supported by this generator.

Additionally, I've already begun laying the groundwork for extended compatibility with a number of other games, including:

* [Microlite Platinum](https://archive.4plebs.org/dl/tg/image/1406/96/1406960963325.pdf)
  - "Robot Hack" based on a popular anime in the USA...
  - "Ruptures" based on a well-known gonzo post-apocalyptic RPG...
* And further out...
  - TNU 2nd Edition compatibility
	- Beyond the Wall
	- The Black Hack
	- Kaigaku

My hope is that as I add more systems and automate more of the decisions, adding in further systems compatibility will eventually be as simple as adding a new set of system prefs and hitting go.

### Mechanics Notes

Since the dawn of my gaming career as a wee lad, there are three things I've always *hated* as both a player and a GM:

1. Level Maximums for non-humans
2. Attribute minimums for classes
3. Attack Roll Matrices

As such, I'm not guaranteeing compatibility with systems that enforce these things. Even with Dark Dungeons and Blood & Treasure, I've chosen to allow characters that don't 100% meet class stat minimums. And any future system that I import will be brought over converted to a simple adjusted Base Attack Roll Modifier display.

This also means that should I ever decide to let this app create characters of higher levels, I won't be adapting this to account for systems which limit the advancement of the non-human classes.

### Equipment Lists

For The Nightmares Underneath, I'm of course using that game's *amazing* built-in random gear generator, which is based upon rolls that determine a character's Social Class. The results are pretty wonderful, and just looking at a character's stats and list of starting gear can inspire instant story. The gear lists from that system have been recreated here with about 99% faithful translation (a *very* small handful of choices had to be tweaked for simplicity of coding at my new skill level).

For the other systems, I'm using my own ground-up home-brew system, pulling from a glommed-together list of gear from a variety of "classic" games. Instead of using starting character money rolls, I'm basing the lists off of the character's initial randomly-rolled "Social Class" descriptor. The higher your station in life, the more money you have. thus the more gear you are able to start with.

For the sake of simplicity, with *most* of the other D&D-like games I'm planning to use the same weapon and gear lists and options. This will result in characters not 100% accurate to their game variant's core gear lists, but still "acceptably playable" in adventures using that game's engine. *Dark Dungeons* and *Blood & Treasure* don't have exactly the same armour types, for example, but there's enough similarity that the lists are basically interchangeable.

### Spell Lists

First off, note that in most of the games I always automatically give all "arcane" type casters the Read Magic spell *in addition to* other spell choices. Frankly I think that making it a slot-requiring spell at all is complete bullshit, but to satisfy basic system conventions I still add it in as a free spell, just in case.

Clerics and other divine-type casters have their *initial* spell lists prepared so you can just jump into the dungeon and start playing. For all other casters, initial spell lists represent the spells in your caster's initial spellbook.

## How to Use

### Random Characters

1. [Install Python](https://www.python.org/downloads/).
2. Run the `print_character.py` file. It has a number of flags to its use, which you can find with the helpfile. For example: `python print_character.py -h`
3. To just pop out a new character, run the script with `-g` followed by the abbreviation of the supported system. For example, run `python print_character.py -g dd` for a random 1st-level Dark Dungeons character.
4. Repeat step 3 to get new characters.

Currently the supported game systems are as follows:

* bnt = Blood & Treasure 1st Edition
* bntx = Blood & Treasure 1st Edition plus Monster Races
* dd = Dark Dungeons
* def = Generates a character using ultra-lite default placeholder settings
* ham = HAMMERCRAWL!
* m81 = Microlite81
* pla = Microlite Platinum (work in progress)
* rbh = Robot Hack (work in progress)
* rpt = Ruptures (work in progress)
* tnu = The Nightmares Underneath 1st Edition

### Silly Options

Thanks to continued development of the HAMMERCRAWL! RPG, I have included a "silly" content generator to the tool, which adds a large amount of rather ridiculous skills, languages, and gear options into the randomizers. To enable these results, just add the `-y` argument to the command line.

### Adding New Systems

As of 2020-10-03, I've made adding new game systems a lot simpler than was previously implemented. The current process is as such:

1. Add new **argparse** abbreviations to lines 11, 12, and 19 of `print_character.py`. When done the abbreviation should appear three times.
2. Add a new system with the same abbreviation to the `systems` dict in `systems.py`. Use the other systems therein as templates. I suggest start by duplicating the `def` fallback, renaming it, and working from there.
3. Add the new system abbreviation to `professions.py` as an option in both `supported_systems` and `proflists`, using the other entries there as examples.
4. To add new "professions" (aka character classes), add a new `base_profs_*` list and `*_profs` dict for the system in `professions.py`, again using the others as examples.
5. After that, begin adding your pertinent game system data following the structures of the preexisting data therein.

Each of the first four steps above is factored so that if followed exactly, there should be no execution errors after each one. After each step, try running the program with the new game system abbreviation. If a step gives errors, resolve them before moving to the next step.

For example, adding `foo` as instructed in step one, then saving, and then running the script `python print_character.py -g foo` should result in no errors. Then following step two, adding the following code to the `systems` dict should likewise result in no errors:

```
	'foo': {
			'saves': False,
	},
```

And so on. If you encounter any errors you are unable to resolve, post an issue.

### Random Treasure Table Rolls

Currently the Treasure table rolls are limited to the Dark Dungeons / BECMI tables. I'm still setting it up for command line calls. right now it returns the combined results of 12 rolls against the U treasure table. This can be changed by adjusting the variables in the final code block, passing it a different table and number of rolls:

```
if __name__ == "__main__":
    myTreasure = get_treasure('u', 'dd', 12)
    for item in myTreasure:
        print(item)
```

## Current State

This is still very much a work in progress. Currently the code runs once and returns printed output only. Right now, there are two main components I'm working on:

* **Random Character Generator:** a one-click chargen for Old School games. I'm teaching myself webapp development so I can actually make this more accessible and presentable. It's definitely a way out though.
* **Random Monster Treasure Roller:** (EXPERIMENTAL!) an app to quickly roll on monster treasure tables (currently only Dark Dungeons/BECMI supported)

### About the Code

This is my first even code project, and I've been using it to teach myself the Python language. Initially I had thoughts of just forking and modifying another current chargen program I'd been using a lot, to tweak it for my own games, but after a bit of futzing around I just decided to start from scratch and learn more about coding on my own.

I'm sure there are far better ways to do what I'm doing here, but I'm a noob to this, so please forgive the crap code as I learn more.

### Requirements and Compatibility

This program was initially written using Python 3.6.3 on Windows 10, MacOS, and Linux Mint 18, using the [PyCharm](https://www.jetbrains.com/pycharm/download/) IDE. As of October 2020 it has been refactored to meet newer Python 3.8.2 requirements. I have not tested much outside of those environment parameters.
