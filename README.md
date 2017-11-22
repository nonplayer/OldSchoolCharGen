# About this Project

This is a Python-based tool to generate random first-level characters for "old school" D&D-like tabletop role-playing games.

## Systems Compatibility

Currently this tool can only create characters for [The Nightmares Underneath, by Johnstone Metzger](http://www.drivethrurpg.com/product/195355/The-Nightmares-Underneath). However, I've already begun laying the groundwork for extended compatibility with a number of other games. Top of my list for expansion are:

* [Dark Dungeons](http://www.drivethrurpg.com/product/177410/Dark-Dungeons)
* [Blood & Treasure 1st Edition](http://www.drivethrurpg.com/product/124972/Blood--Treasure-Complete) (I just don't like the 2nd Edition changes at all)
* [Microlite Platinum](https://archive.4plebs.org/dl/tg/image/1406/96/1406960963325.pdf)
* And further out...
	- Beyond the Wall
	- The Black Hack
	- Kaigaku
	
I know, everyone has their favorite systems, but these specifically are mine, and thus what I'm developing for. My hope is that I add more systems and automate more of the decisions, adding in more systems will be eventually be as simple as adding a new set of system prefs and hitting go.

### Mechanics Notes

Since the dawn of my gaming career as a wee lad, there are three things I've always *hated* as both a player and a GM:

1. Level Maximums for non-humans
2. Attribute minimums for classes
3. ...I forgot the third one because I am drinking currently but I know it's important and I'll get back here when I remember.

As such, I'm not guaranteeing compatibility with systems that enforce these things. Even with Dark Dungeons and Blood & Treasure, I've chosen to allow characters that don't 100% meet class stat minimums.

This also means that should I ever decide to let this app create characters of higher levels, I won't be adapting this to account for systems which limit the advancement of the non-human classes.

### Equipment Lists

For The Nightmares Underneath, I'm of course using that game's *amazing* built-in random gear generator, which is based upon rolls that determine a character's Social Class. The results are pretty wonderful, and just looking at a character's stats and list of starting gear can inspire instant story. The gear lists from that system have been recreated here with about 99% faithful translation (a *very* small handful of choices had to be tweaked for simplicity of coding at my new skill level).

For the others, I'm using my own ground-up home-brew system, pulling from a glommed-together list of gear from a variety of OSR games. Instead of using starting character money rolls, I'm basing the lists off of the average of the character's initial six stats - the better their stat rolls, the fewer gear options they start with. The result is a rough "starting balance of survivability" wherein characters with higher stats have higher mechanical chances of excelling, while those with lower stats have more potential gear-based options for survival.

For the sake of simplicity, with *most* of the other D&D-like games I'm planning to use the same weapon and gear lists and options. This will result in characters not 100% accurate to their game variant's core gear lists, but still "acceptably playable" in adventures using that game's engine. *Dark Dungeons* and *Blood & Treasure* don't have exactly the same armour types, for example, but there's enough similarity that the lists are basically interchangeable.

### Spell Lists

First off, note that in OSR games I always automatically give all "arcane" type casters the Red Magic spell *in addition to* other spell choices. Frankly I think that making it a slot-requiring spell at all is complete bullshit, but to satisfy basic system conventions I still add it in as a free spell, just in case.

Clerics and other divine-type casters have their *initial* spell lists prepared so you can just jump into the dungeon and start playing. For all other casters, initial spell lists represent the spells in your caster's initial spellbook.


## How to Use

### Random Characters

1. [Install Python](https://www.python.org/downloads/).
2. Run the `generator.py` file.
3. Repeat step 2 to get new characters.

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

* **Random Character Generator:** a one-click chargen for Old School games (currently only TNU)
* **Random Monster Treasure Roller:** an app to quickly roll on monster treasure tables (currently only Dark Dungeons/BECMI supported)

### Future Plans

* add attacks and modifiers
* Add character class extended features
* Add skills
* Add saves
* Add random names, traits, and descriptions
* Compatibility for additional game systems and house rules
    * Bonus Goal: Support for *Microlite Platinum* and it's awesome sci-fi derivative *"Robot Hack"*
* Develop a functional web app version

### About the Code

This is my first even code project, and I've been using it to teach myself the Python language. Initially I had thoughts of just forking and modifying another current chargen program I'd been using a lot, to tweak it for my own games, but after a bit of futzing around I just decided to start from scratch and learn more about coding on my own.

I'm sure there are far better ways to do what I'm doing here, but I'm a noob to this, so please forgive the crap code as I learn more.

### Requirements and Compatibility

This program is written using Python 3.6.3 on Windows 10, MacOS, and Linux Mint 18, using the [PyCharm](https://www.jetbrains.com/pycharm/download/) IDE. I have not tested much outside of those environment parameters.
