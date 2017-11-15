# About this Project

This is a Python-based tool to generate random first-level characters for "old school" D&D-like tabletop role-playing games. While I'd like to eventually extend it to allow different game systems and customizations, currently it is focused entirely on creating characters for [The Nightmares Underneath, by Johnstone Metzger](http://www.drivethrurpg.com/product/195355/The-Nightmares-Underneath).

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

* Calculate AC
* add attacks and modifiers
* Add character class extended features
* Add skills
* Add saves
* Add random names, traits, and descriptions
* Compatibility for additional game systems and house rules
* Develop a functional web app version

### About the Code

This is my first even code project, and I've been using it to teach myself the Python language. Initially I had thoughts of just forking and modifying another current chargen program I'd been using a lot, to tweak it for my own games, but after a bit of futzing around I just decided to start from scratch and learn more about coding on my own.

I'm sure there are far better ways to do what I'm doing here, but I'm a noob to this, so please forgive the crap code as I learn more.

### Requirements and Compatibility

This program is written using Python 3.6.3 on Windows 10, MacOS, and Linux Mint 18, using the [PyCharm](https://www.jetbrains.com/pycharm/download/) IDE. I have not tested much outside of those environment parameters.
